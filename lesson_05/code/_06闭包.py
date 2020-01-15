def demo1():
	for index in range(5):
		def fn():
			return index
	return fn


f = demo1()
print("index =",f())
print("index =",f())
print("index =",f())
print("index =",f())

# demo1函数执行时，里面的 fn 函数并没有得到执行； fn 执行时，index 变量已经到5

# 闭包的条件：
# 1. 函数嵌套
# 2. 内部函数持有外部函数的变量
# 3. 调用

