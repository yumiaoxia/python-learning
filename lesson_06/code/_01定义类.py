class Person:
	def __init__(self,name):
		self.name = name


	def say_hello(self):
		print("你好，我是%s" %self.name)


p1 = Person("猪八戒")
p2 = Person("沙和尚")

print(p1.name)
print(p2.name)
p1.say_hello()
p2.say_hello()



# 定义类时，类名后面可以带括号，可以指定继承的父类，Python可以同时继承多个父类
# `__init__` 是类中特殊的命名空间，用来指定类的构造器
# 构造器本质上是一个特殊的方法,返回值只有None,构造器在类实例化对象时被解析器调用，调用一次创建一个新的对象
# 解析器创建一个类时，解析器会查找我们创建的类的构造器。没有则会为我们的类指定一个默认的构造器
