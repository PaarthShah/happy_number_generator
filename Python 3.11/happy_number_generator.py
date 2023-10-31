import performance_print

LENLIST = 10_000


# def sum_of_squares(n: int) -> int:
# 	return sum(int(i) ** 2 for i in str(n))


def sum_of_squares(n: int) -> int:
	total_sum = 0
	while n:
		n, remainder = divmod(n, 10)
		total_sum += remainder ** 2
	return total_sum


def happy(n: int) -> bool:
	past = set()
	while n != 1:
		n = sum_of_squares(n)
		if n in past:
			return False
		past.add(n)
	return True


@performance_print.last
def calculate_naive() -> list[int]:
	happy_list = []
	count = 1
	while len(happy_list) < LENLIST:
		if happy(count):
			happy_list.append(count)
		count += 1
	return happy_list


@performance_print.last
def calculate_smart() -> list[int]:
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
	while count <= 99:
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
