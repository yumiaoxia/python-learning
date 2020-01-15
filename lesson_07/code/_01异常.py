def demo1():
    try:
        raise TypeError('spam','eggs')
    except TypeError as e:
        print(e)
	

demo1()



# - 首先，执行 try 子句
# - 如果没有异常发生，则跳过 except 子句并完成 try 语句的执行。
# - 如果在执行 try 子句时发生了异常，则跳过该子句剩下的部分。然后，如果异常的类型和 except 关键字后面的异常匹配，则执行 except 子句，然后继续 执行 try 语句之后的代码。
# - 如果发生的异常和 exccept 子句中制定的异常不匹配则将其传递给 try 语句中；如果没有找到处理程序，则它是一个未处理异常，执行将停止并显示以上所示的消息

# 如果 try 语句可能有多个 except 子句，以指定不同的异常处理程序。最多会执行一个处理程序。处理程序只处理相应的 try 子句中发生的异常，而不处理同一try语句内其他处理程序中的异常。

# ===============================================================================

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

def demo2():
	for cls in [B, C, D]:
	    try:
	        raise cls()
	    except B:
	        print("B")
	    except D:
	        print("D")
	    except C:
	        print("C")

demo2()

# 如果 except 子句中的异常类有继承关系，而且 try 子句出现的异常跟异常类的子类相匹配，则哪个异常类先定义就捕获哪个异常
# ============================================================================================================

def demo3(b):
    try:
        a = 10/b
    except ZeroDivisionError as e:
        print(e)
    else:
       print(a)


demo3(0)
a = demo3(1)
print(a)

# 上面程序第一次调用发生异常了，else 语句得不到执行，第二次调用没有发生异常，程序执行完try 语句之后继续执行 else 语句

# ====================================================================================================

# finally 子句

def demo4(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print("result is: ",result)
	finally:
		print("executing finally clause")


demo4(10,2)
demo4(20,0)
# demo4('23','2')
# finally 子句我无伦在任何情况下都会被执行。except子句没有捕获的异常会在finally子句执行后被重新引发

# ===========================================================================================

