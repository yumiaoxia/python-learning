def demo1():
	try:
		raise NameError
	except NameError as e:
		print("An exception flew by!")

demo1()

# python 可以通过 raise 语句强制抛出指定的异常

# =====================================================

def demo2():
	try:
		raise Exception('spam','eggs')
	except Exception as e:
		print(e)

demo2()

# 抛出异常可以携带参数
# except 子句可以在异常名称后面指定一个变量。这个变量和一个异常实例绑定，它的参数存储在 instance.args 中。为了方便起见，异常实例定义了 __str__() ，因此可以直接打印参数而无需引用 .args 。也可以在抛出之前首先实例化异常，并根据需要向其添加任何属性。