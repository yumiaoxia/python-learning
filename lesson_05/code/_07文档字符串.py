def demo1(a: int, b: bool, c: str='Hello') ->int:
	'''
	这是一个文档字符串示例
	函数的作用： 。。。
	a: 作用，类型，默认值
	b: 作用，类型，默认值
	c: 作用，类型，默认值
	'''
	print("a=",a)
	print("b=",b)
	print("c=",c)
	return 0

help(demo1)
demo1(1,True,"guoguo")