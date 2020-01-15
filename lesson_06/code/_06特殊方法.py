class Person(object):
	
	def __init__(self, name, age):
		super(Person, self).__init__()
		self._name = name
		self._age = age

	
	@property
	def name(self):
		return self.name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, age):
		self._age = age

	def __gt__(self, other):
		return self.age > other.age

# ================================================================================


class Book(object):
	
	def __init__(self, name, page_count):
		super(Book, self).__init__()
		self._name = name
		self._page_count = page_count

	def __str__(self):
		return 'Book [name  =%s, page_count = %d]'%(self._name,self._page_count)

	def __bool__(self):
		return self._page_count > 1000

p = Person("孙悟空",100000)
print(p)
print(str(p))
b = Book("Python 基础",788)
print(b)

# 当使用print打印一个对象时，实际上调用的是内置函数str()
# __str()__ 方法在把对象转换为字符串时调用，其返回值就是转换的结果

# ================================================================================
# 比较方法
p2 = Person("猪八戒",1000)
print(p > p2,p.age, p2.age)

# 布尔方法

print(bool(b))
# __bool__(self) 方法在将对象转换为布尔值时调用
