# 创建一个元组：

t = 12,33,42,31,622
print(t)
print(t[0])
# t[0] = 10
# 给元组的一个元素赋值是不允许的

t2 = (12,33,42,31,622)
print(t2)

empty = ()
print(len(empty))

# 注意有且仅有一个字符串元素时
s = ('hello')
singleton = ('hello',)
print(len(s))
print(len(singleton))


# 序列解包
a,b,c,d,e = t
print(a,b,c,d,e)

