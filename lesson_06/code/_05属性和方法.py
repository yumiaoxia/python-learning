class A(object):

	count  = 1000;

	def __init__(self, arg):
		super(A, self).__init__()
		self.arg = arg

	@classmethod
	def test(cls):
		print("这是类方法",cls)

	@staticmethod
	def test2():
		print("这是静态方法")


a = A(10)
print(a.count)
print(A.count)
# print(A.arg)

A.test()
a.test()

A.test2()
a.test2()


# - 类属性：直接在类中的定义的属性
# 		类属性可以通过类或类的实例访问到
# 		类属性只能通过类对象来修改，无法通过实例对象修改
# 	- 实例属性：通过实例对象添加的属性属于实例属性
# 		实例属性只能通过实例对象来访问和修改，类对象无法访问修改

# 	- 实例方法：在类中定义，以 self 作为第一个参数的方法
# 		实例方法在调用时，Python 会将调用对象作为self传入
# 		实例方法可以通过实例和类去调用
# 			当通过类调用时，不会自动传self，需要我们手动将实例对象传入

# 	- 类方法：在类内部使用 @classmethod 来修饰的方法属于类方法
# 		类方法的第一个参数是cls,也会被自动传递，cls是当前的类对象
# 		类方法可以通过类对象调用，也可以通过实例对象调用

# - 静态方法： 在类内部使用 @staticmethod 来修饰的方法属于类方法
# 		静态方法不需要指定任何的默认参数
# 		静态方法可以通过类和实例去调用
# 		静态方法，基本上是一个和当前类的无关方法，只是一个保存到当前类的函数
# 		静态方法一般都是一些工具函数