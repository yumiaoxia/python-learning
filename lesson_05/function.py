# 无参函数
def demo1():
	print("Hello world")

# 调用
demo1()

# 位置参数函数
def demo2(name):
	print("name=",name)

# 调用
demo2("孙悟空")


# 默认参数函数
def demo3(name = "孙悟空"):
	print("name=",name)

# 调用默认参数函数时,默认的参数是可选的（可传可不传，不传使用默认值）
demo3()
demo3("猪八戒")

# 关键字调用
demo3(name="沙和尚")

def demo4(a,b,c):
	print("a=",a)
	print("b=",b)
	print("c=",c)

# 调用
# demo4(a = 3,6,9) 错误用法，关键字调用必须放在位置参数后面
demo4(1,b = 10,c = 5)


def demo5(number,*strings,**keys):
	print("number=",number)
	for v in strings:
		print("v=",v)
	for kw in keys:
		print(kw,":",keys[kw])

demo5(40,"山梨","凤爪",name="麒麟山",height=3197)

# 带 * 参数不是必须写在最后，但调用时带*参数后的所有参数必须以关键字的形式传递
def demo6(a,*b,c):
	print("a=",a)
	print("b=",b)
	print("c=",c)

demo6(3,2,4,6,8,9,c=10)

# 定义函数时，如果在形参开头写一个*，则要求我们所有的参数必须以关键字的形式进行传递
def demo7(*,a,b,c):
	print("a=",a)
	print("b=",b)
	print("c=",c)

demo7(a=3,b=(6,5),c=9)

def demo8(*a):
	print("a=",a)

# *形参只能接受位置参数，而不能接受关键字参数
#demo8(a=(2,5,8))
demo8(2,5,8)


def demo9(**a): 
	print("a=",a,type(a))

# **形参可以接受其他关键字参数，它会将这些参数统一保存到一个字典中，字典的 key 就是参数的名字
demo9(b = 1, c = 4, d = 8)

def demo10(a,b,c):
	print("a=",a)
	print("b=",b)
	print("c=",c)