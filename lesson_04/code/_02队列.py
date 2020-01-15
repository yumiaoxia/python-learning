class Queue:

	def __init__(self, li:list):
		self.li = li

	def pop(self):
		self.li.remove(self.li[0])
		return self

	def append(self, x):
		self.li.append(x)
		return self

	def __str__(self):
		return str(self.li)

	def size(self):
		return len(self.li)


queue = Queue([1,3,5,7,9])
print(queue)
print(queue.append(10),queue.size())
print(queue.pop(),queue.size())