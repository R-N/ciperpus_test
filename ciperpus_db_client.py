import mysql.connector
from mysql.connector.errors import *
from contextlib import closing
from functools import wraps


class ciperpus_db_client:
	def __init__(self, host="localhost", db_name="ciperpus", username="root", password=""):
		self.host = host
		self.db_name = db_name
		self.username = username
		self.password = password
		self.connection = None
		self.connection = self.connect()
	
	def require_connection(foo):
		@wraps(foo)
		def wrap(self, *args, **kwargs):
			if not self.is_connected:
				self.connect()
			return foo(self, *args, **kwargs)
		return wrap

	def connect(self):
		if not self.is_connected:
			self.connection = mysql.connector.connect(
				host=self.host,
				user=self.username,
				passwd=self.password
			)
			assert self.is_connected
		with closing(self.cursor()) as cur:
			cur.execute("use %s" % (self.db_name,))
	@require_connection
	def cursor(self, prepared=False):
		return self.connection.cursor(prepared=prepared)

	@require_connection
	def commit(self):
		return self.connection.commit()

	@require_connection
	def execute_file(self, path):
		#https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python/19473206
		sqlFile = None
		with open(path, 'r') as fd:
			sqlFile = fd.read()

		# all SQL commands (split on ';')
		sqlCommands = sqlFile.split(';')

		error = None
		# Execute every command from the input file
		with closing(self.cursor()) as cur:
			for command in sqlCommands:
				if not command or command.isspace(): 
					continue
				try:
					cur.execute(command)
				except OperationalError as ex:
					print("Command: " + command)
					raise
					error = ex
					break
				except ProgrammingError as ex:
					print("Command: " + command)
					raise
					error = ex
					break
			
			if not error:
				self.commit()

	@require_connection
	def empty(self):
		with closing(self.cursor()) as cur:
			cur.execute("DROP DATABASE IF EXISTS %s" % self.db_name)
			cur.execute("CREATE DATABASE %s" % self.db_name)
			cur.execute("USE %s" % self.db_name)
			self.commit()
	
	@require_connection
	def reset(self, path="dump.sql"):
		self.empty()
		self.execute_file(path)

	@property
	def is_connected(self):
		return self.connection is not None and self.connection.is_connected()

	def close(self):
		if self.is_connected:
			self.connection.close()
		self.connection = None

	def __enter__(self):
		if not self.is_connected:
			self.connect()
		return self
	
	def __exit__(self, exc_type, exc_value, traceback): 
		self.close()

db_client_instance = None

def get_db_client():
	global db_client_instance
	db_client_instance = db_client_instance or ciperpus_db_client()
	return db_client_instance

def get_db_cursor():
	return get_db_client().cursor()