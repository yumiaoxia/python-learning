
# 简单打开一个文件
def demo1():
	file = open("myFile.txt")
	print(file)

demo1()

# 预定义关闭资源地打开文件

# =================================================================
def demo2():
	with open("myFile.txt") as file:
		print(file)


demo2()

# 使用 with 语句打开一个文件，在with语句结束时会自动释放文件地资源

# ==================================================================

# 读取文件

def demo3():
	try:
		with open("myFile.txt",mode = 'r', encoding = 'utf-8') as file:
			for line in file:
				print(line,end='')
	except IOError:
		print("文件读取错误")

def demo4():
	try:
		with open("myFile.txt",mode = 'r', encoding = 'utf-8') as file:
			content = file.read()
	except IOError:
		print("文件读取错误")
	else:
		print(content)

demo3()
demo4()
# 调用open()打开一个文件，可以将文件分成两种类型：一种是纯文本文件（存放文本字符）；另一种是二进制文件(图片，MP3...)
# open()的参数很多，mode 是打开文件的模式（只读，只写，读写，...); encoding指定打开文本文件的编码（gbk,utf-8,...）
# 我们一般使用utf-8读写文本文件,utf-8支持大部分语言
# 我们可以通过for循环读取文件的每一行，也可以通过file.read()直接读取
# file.read() 可以直接指定每次读取的文件的大小size