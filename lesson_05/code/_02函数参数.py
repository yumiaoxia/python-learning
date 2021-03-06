# 无参函数

def demo0():
	print("无参函数被调用")

demo0()

# ===========================================================

# 位置参数

def demo1(name):
	print("Hello,",name)

demo1("python")

# ==========================================================

# 默认参数

def demo2(name = "Python"):
	print("Hello,",name)

demo2()
demo1("Java")

# 默认参数实在函数定义时给定一个默认值，使用时函数的值可传可不传，不传则使用默认值

# ==========================================================

# 关键字参数

def demo3(a,b,c):
	print("a=",a)
	print("b=",b)
	print("c=",c)

demo3(2, 5, 8)
demo3(2, b = 5, c = 8)
demo3(2, 5, c = 8)
demo3(a = 2, b = 5, c = 8)

# 调用需传递多个参数时要注意传递顺序，关键字调用参数要在位置参数的后面

# ===========================================================

# 带`*`参数

def demo4(name,*food,**description):
	print("name=",name)
	print("food=",food,type(food))
	print("hobby=",description,type(description))


demo4("孙悟空","桃子","香蕉",feature="嫉恶如仇",skill=("七十二变","筋斗云"))

# 带 * 参数分为两种：带 * 的表示接受元祖参数，带 ** 的表示接收字典作为参数
# 定义时， 带 * 的参数必须写在带 ** 的参数的前面

# ============================================================

def demo5(a,*b,c):
	print("a=",a)
	print("b=",b)
	print("c=",c)

demo5(3,2,4,6,8,9,c=10)

# 带 * 参数不是必须写在最后，但调用时带*参数后的所有参数必须以关键字的形式传递

# ============================================================

def demo6(*a):
	print("a=",a)

demo6(2,5,8)

# demo6(a = (2,5,8))
# 带*参数只能以位置参数的形式进行传递,不能使用关键字的形式进行传递


# ============================================================

def demo9(**a): 
	print("a=",a,type(a))


demo9(b = 1, c = 4, d = 8)

# **形参可以接受其他关键字参数，它会将这些参数统一保存到一个字典中，字典的 key 就是参数的名字