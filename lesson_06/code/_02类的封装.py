class Person:
	def __init__(self,name):
		self.__name = name


	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

p = Person("孙悟空")
## print(p.__name)
print(p.get_name())
print(p._Person__name)

# =======================================================================
class Book:
	def __init__(self,name):
		self._name = name


	def set_name(self, name):
		self._name = name

	def get_name(self):
		return self._name

b = Book("Python 实战")
print(b._name)

# 一般地，我们不希望向外直接暴露类的属性
# 我们可以通过`_`或者`__`将类属性生命为私有属性,并且提供get方法和set方法给外部间接访问属性，这种方式称为类的封装
# 使用`__`开头的属性，实际上可以在外部访问,一般地，我们更多使用 `_`来定义私有属性
