# 尝试求10的阶乘
def demo1():
    result = 10
    for index in range(1,10):
        result *= index
    return result

# 使用递归

def demo2(n):
	if(n == 1):
		return 1
	else:
		return n * demo2(n-1)

result1 = demo1();
print("result1=",result1)

result2 = demo2(10)
print("result2=",result2)

# 递归函数的两个条件
# 1. 基线条件： 问题可以被分解为最小的条件，当满足最小基线条件时，递归就不再执行了
# 2. 递归条件： 将问题继续分解的条件