
print(__name__)

def test_hello():
	print("Hello")

a = 10
_b = 20
__c = 30

# 通过下面语句可以编写一些测试代码，被引入其他模块时将不会得到执行
if __name__ == '__main__':
	test_hello()

