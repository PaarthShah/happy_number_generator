from typing import Callable, List
from time import perf_counter

calculator_types = Callable[[], List]


def all(f: calculator_types) -> calculator_types:
	def wrapper() -> List:
		start = perf_counter()
		happy_list = f()
		stop = perf_counter()
		for count, value in enumerate(happy_list, start=1):
			print(f"{count:,}:\t{value:,}")
		print(f"Took {stop - start} seconds.")
		return happy_list

	return wrapper


def last(f: calculator_types) -> calculator_types:
	def wrapper() -> List:
		start = perf_counter()
		happy_list = f()
		stop = perf_counter()
		print(f"{len(happy_list):,}:\t{happy_list[-1]:,}")
		print(f"Took {stop - start} seconds.")
		return happy_list

	return wrapper
