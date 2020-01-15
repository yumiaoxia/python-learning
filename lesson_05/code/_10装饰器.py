def add(a, b):
	return a + b

def mul(a, b):
	return a * b

# 有以上两个函数，要求根据开放关闭原则对原函数进行扩展

# 方式一

def demo(fn,*args,**keywords):
	print("开始执行运算")
	r = fn(*args,**keywords)
	print("结束运算")
	return r


print(demo(add,12,64))
print(demo(mul,12,64))

# ========================================================

def begin_end(old):
	def f(*args,**keywords):
		print("开始执行运算")
		r = old(*args,**keywords)
		print("结束运算")
		return r
	return f

f = begin_end(mul)
print(f(12,64))

# ===========================================================
@begin_end
def minus(a , b):
	return a - b

print(minus(345677,34322))
# 通过带 * 参数 和带 ** 参数结合可以匹配任何形式的参数列表
# 通过装饰器可以在不修改原来的函数的情况下对原函数进行扩展或增强
# 可以通过注解使用一个或多个装饰器，使用多个装饰器时，后面的装饰器先起作用