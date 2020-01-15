def demo1():
	for line in open("myFile.txt",'r',encoding='utf-8'):
		print(line, end="")

def demo2():
	with open("myFile.txt",'r',encoding='utf-8') as f:
		for line in f:
			print(line, end='')

demo1()
demo2()
