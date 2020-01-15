
def demo1():
	matrix = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
	]
	return [[row[i] for row in matrix] for i in range(4)]


def demo2():
	matrix = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
	]
	return list(zip(*matrix))

print(demo1())
print(demo2())