# 创建一个平方列表
from math import pi

def demo1():
	squares = []
	for x in range(1,10):
		squares.append(x**2)
	return squares;


def demo2():
	return [x**2 for x in range(1,10)]


def demo3():
	return [(x,y) for x in [1,3,5] for y in [5,6,8] if x != y]


# 列表推导式可以使用复杂的表达式和嵌套函数
def demo4():
	return [str(round(pi, x)) for x in range(1,6)]

print(demo1())
print(demo2())
print(demo3())
print(demo4())