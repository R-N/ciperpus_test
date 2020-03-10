
import factory.fuzzy

def fuzz_string(length, count=1):
	f = factory.fuzzy.FuzzyText(length=length)
	return [f.fuzz() for x in range(0, count)]
	
def fuzz_choice(choices, count=1):
	f = factory.fuzzy.FuzzyChoice(choices=choices)
	return [f.fuzz() for x in range(0, count)]
	
def fuzz_int(min, max, count=1, step=1):
	f = factory.fuzzy.FuzzyInteger(min, max, step)
	return [f.fuzz() for x in range(0, count)]
	
def fuzz_decimal(min, max, count=1, precision=2):
	f = factory.fuzzy.FuzzyDecimal(min, max, precision)
	return [f.fuzz() for x in range(0, count)]
	
def fuzz_float(min, max, count=1):
	f = factory.fuzzy.FuzzyFloat(min, max)
	return [f.fuzz() for x in range(0, count)]
	
def fuzz_date(start, end, count=1):
	f = factory.fuzzy.FuzzyDate(start, end)
	return [f.fuzz() for x in range(0, count)]
	
def fuzz_datetime(start, end, count=1, force_year=None, force_month=None, force_day=None, force_hour=None, force_minute=None, force_second=None, force_microsecond=None):
	f = factory.fuzzy.FuzzyDateTime(start, end, force_year, force_month, force_day, force_hour, force_minute, force_second, force_microsecond)
	return [f.fuzz() for x in range(0, count)]
	
	
def fuzz_naive_datetime(start, end, count=1, force_year=None, force_month=None, force_day=None, force_hour=None, force_minute=None, force_second=None, force_microsecond=None):
	f = factory.fuzzy.FuzzyNaiveDateTime(start, end, force_year, force_month, force_day, force_hour, force_minute, force_second, force_microsecond)
	return [f.fuzz() for x in range(0, count)]
	