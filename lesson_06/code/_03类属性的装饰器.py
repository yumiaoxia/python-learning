class Person:
	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

p = Person("孙悟空")
print(p.name)
p.name = "沙和尚"
print(p.name)

# 我们可以在get方法和set方法上加上注解,从而可以让访问属性可以更加方便
