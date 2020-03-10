import enum
from selenium import webdriver
from functools import wraps

class endpoints:
	login = "login"
	dashboard = "dashboard"
	logout = "login/logout"
	front_buku = "login/search_buku"
	front_anggota = "login/view_anggota"
	anggota = "anggota"
	anggota_add = "anggota/create"
	buku = "buku"
	buku_add = "buku/create"
	users = "users"
	users_add = "users/create"
	peminjaman = "peminjaman"
	pengembalian = "pengembalian"
	laporan_anggota = "laporan/anggota"
	laporan_buku = "laporan/buku"
	laporan_peminjaman = "laporan/peminjaman"
	laporan_pengembalian = "laporan/pengembalian"

class ciperpus_page:

	def __init__(self, client):
		self.client = client
	
	def require_login(foo):
		@wraps(foo)
		def wrap(self, *args, **kwargs):
			if not self.client.is_logged_in:
				self.client.login()
			return foo(self, *args, **kwargs)
		return wrap

	def require_logout(foo):
		@wraps(foo)
		def wrap(self, *args, **kwargs):
			if self.client.is_logged_in:
				self.client.logout()
			return foo(self, *args, **kwargs)
		return wrap

	@require_logout
	def login(self):
		self.driver.open(endpoints.login)

	@property
	def driver(self):
		return self.client.driver

	@require_login
	def dashboard(self):
		self.driver.open(endpoints.dashboard)
	
	@require_login
	def logout(self):
		self.driver.open(endpoints.logout)
	front_buku = "login/search_buku"
	front_anggota = "login/view_anggota"
	anggota = "anggota"
	anggota_add = "anggota/create"
	buku = "buku"
	buku_add = "buku/create"
	users = "users"
	users_add = "users/create"
	peminjaman = "peminjaman"
	pengembalian = "pengembalian"
	laporan_anggota = "laporan/anggota"
	laporan_buku = "laporan/buku"
	laporan_peminjaman = "laporan/peminjaman"
	laporan_pengembalian = "laporan/pengembalian"