from typing import List

import performance_print

LENLIST = 10_000


# def sum_of_squares(n: int) -> int:
# 	return sum([int(i) ** 2 for i in str(n)])


def sum_of_squares(n: int) -> int:
	r = 0
	while n:
		r, n = r + (n % 10)**2, n // 10
	return r


def happy(n: int) -> bool:
	past = set()
	while n != 1:
		n = sum_of_squares(n)
		if n in past:
			return False
		past.add(n)
		print(n)
	return True


@performance_print.last
def calculate_naive() -> List:
	happy_list = []
	count = 1
	while len(happy_list) < LENLIST:
		if happy(count):
			happy_list.append(count)
		count += 1
	return happy_list


@performance_print.all
def calculate_smart() -> List:
	happy_set = {1}
	sad_set = {4}

	def happy_smarter(n: int):
		x = sum_of_squares(n)
		if x in sad_set:
			sad_set.add(n)
			return False
		else:
			# happy_set.add(n)
			return True

	def happy_smart(n):
		past = set()
		while n != 1:
			past.add(n)
			n = sum_of_squares(n)
			if n in sad_set:
				sad_set.update(past)
				return False
		happy_set.update(past)
		return True

	happy_list = []
	count = 1
	while len(happy_list) <= sum_of_squares(99):
		if happy_smart(count):
			happy_list.append(count)
		count += 1
	while len(happy_list) < LENLIST:
		if happy_smarter(count):
			happy_list.append(count)
		count += 1
	return happy_list


if __name__ == "__main__":
	# calculate_naive()
	calculate_smart()
