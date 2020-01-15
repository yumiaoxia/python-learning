
# 函数是可以嵌套使用的
def demo1():
	def fn():
		print("Hello Python")
	return fn

demo1()()
f = demo1();
f()
