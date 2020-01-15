# 打包

def demo1(name,*food,**description):
	print("name=",name)
	print("food=",food,type(food))
	print("hobby=",description,type(description))


demo1("孙悟空","桃子","香蕉",feature="嫉恶如仇",skill=("七十二变","筋斗云"))

# 使用带 * 参数时，参数可以接收元祖或字典，可以称之为参数的打包传递

# ========================================================================

# 解包

def demo2(a,b,c):
	print("a=",a)
	print("b=",b)
	print("c=",c)


p = (10, 20, 30)

demo2(*p)
demo2(*(10, 20, 30))

d = {'a':20,'b':30,'c':40}
demo2(**d)
demo2(**{'a':20,'b':30,'c':40})

# 解包就是在调用传递实参时参数前面带上*号，该参数必须是与函数形参列表对应的元祖或者字典