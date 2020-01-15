class Stack:
	"""docstring fos Stack"""

	def __init__(self,arg:list):
		self.arg = arg
		
	def pop(self):
		self.arg.pop()
		return self

	def append(self, x):
		self.arg.append(x)
		return self

	def __str__(self):
		li = self.arg
		return str(li);



stack = Stack([1,3,5,7,9]);
print(stack)
stack.pop().pop()
print(stack)
print(stack.append(10))
