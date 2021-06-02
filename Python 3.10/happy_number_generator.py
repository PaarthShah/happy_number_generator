from time import perf_counter

LENLIST = 10_000


def happy(n: int) -> bool:
	past = set()
	while n != 1:
		n = sum(int(i) ** 2 for i in str(n))
		if n in past:
			return False
		past.add(n)
	return True


def calculate_naive():
	happy_list = []
	count = 1
	while len(happy_list) < LENLIST:
		if happy(count):
			happy_list.append(count)
			print(len(happy_list), ":\t", count)
		count += 1


def calculate_smart():
	happy_set = {1}
	sad_set = {4}

	def happy_smarter(n):
		x = sum(int(i) ** 2 for i in str(n))
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
			n = sum(int(i) ** 2 for i in str(n))
			if n in sad_set:
				sad_set.update(past)
				return False
		happy_set.update(past)
		return True

	happy_list = []
	smart_dict = {}
	smarter_dict = {}
	count = 1
	while len(smarter_dict) <= 200:
		if happy_smart(count):
			smarter_dict[len(smarter_dict) + 1] = count
			print(len(smarter_dict), ":\t", count)
		count += 1
	while len(smarter_dict) < LENLIST:
		if happy_smarter(count):
			smarter_dict[len(smarter_dict) + 1] = count
			print(len(smarter_dict), ":\t", count)
		count += 1

	# count = 1
	# while len(smart_dict) < LENLIST:
	#     if happy_smart(count):
	#         smart_dict[len(smart_dict) + 1] = count
	#         print(len(smart_dict), ":\t", count)
	#     count += 1

	# try:
	#     assert smarter_dict == smart_dict
	# except AssertionError:
	#     for i in range(1, LENLIST+1):
	#         if smarter_dict[i] != smart_dict[i]:
	#             print(f"Element {i} in smarter dict, {smarter_dict[i]}, does not match smart dict {smart_dict[i]}")
	#             break


start = perf_counter()
calculate_smart()
end = perf_counter()
print(end - start)
