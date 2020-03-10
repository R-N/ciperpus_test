import fuzzing
import itertools


def fuzz_list(func, seed, *args, **kwargs):
	count = math.ceil(count/len(seed))
	fuzzes = [func(x, *args, **kwargs) for x in seed]
	fuzzes = list(itertools.chain.from_iterable(fuzzes))
	return fuzzes
	
def fuzz_string(seed, count=1, factor=1):
	if isinstance(seed, list):
		return fuzz_list(fuzz_string_seeded, *[seed, count, factor])
	if not isinstance(seed, str):
		seed = str(seed)
	return fuzzing.fuzz_string(seed, count, factor)
	
def fuzz_int(seed, count=1, factor=1):
	if isinstance(seed, list):
		return fuzz_list(fuzz_number, seed, count, factor)
	return seed
	
def fuzz_file(seed, count=1, factor=1):
	if isinstance(seed, list):
		return fuzz_list(fuzz_file, seed, count, factor)
	return seed
	