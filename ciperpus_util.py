import itertools
from allpairspy import AllPairs
from csv import reader, DictReader
import os
import random

def list_to_string(list):
	return "[%s]" % ", ".join([str(x) for x in list])
	
def combine_lists(lists):
	return list(itertools.chain.from_iterable(lists))

def zip_lists(lists):
	return list(zip(*lists))
	
def pair_lists(lists):
	return AllPairs(lists)
	
	
#https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/
def read_csv_tuples(path, remove_first=True):
	# open file in read mode
	with open(path, 'r') as read_obj:
		# pass the file object to reader() to get the reader object
		csv_reader = reader(read_obj)
		# Get all rows of csv from csv_reader object as list of tuples
		list_of_tuples = list(map(tuple, csv_reader))
		if remove_first:
			list_of_tuples.pop(0)
		
		return list_of_tuples
	
 
def read_csv_dictionary(path):
	# open file in read mode
	with open(path, 'r') as read_obj:
		# pass the file object to DictReader() to get the DictReader object
		dict_reader = DictReader(read_obj)
		# get a list of dictionaries from dct_reader
		list_of_dict = list(dict_reader)
		
		return list_of_dict
		
def read_payload(path):
	lines = None
	with open(path) as f:
		lines = [line.rstrip('\n') for line in f]
	random.shuffle(lines)
	return lines
	
def mkdir(path):
	if not os.path.exists(path):
		os.makedirs(path)