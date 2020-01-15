
# 类的继承
class Animal():
	def __init__(self, name):
		self._name = name
		
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name):
		self._name =name

	def run(self):
		print(self._name + "会跑")

	def bark(self):
		print(self._name + "会叫")


class Dog(Animal):

	def __init__(self, name):
		super().__init__(name)
		self._name = name
		

	def bark(self):
		print(self._name + "会汪汪地叫")


dog = Dog("哈士奇")
print(dog.name)
dog.bark()
dog.run()


