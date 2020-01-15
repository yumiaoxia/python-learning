# 创建一个字典
tel = {}
print(type(tel))


person = {'p1':{'name':"张三",'age':30},'p2':{'name':"李四",'age':25}}
print(person)

# 也可使用 dict() 创建一个字典
d = dict([('sape',4139),('guido',4127),('jack',4098)])
# 等价于
d = dict(sape = 4139, guido = 4127, jack = 4098)
print(d)

# 字典推导式
dd = {x:x**2 for x in range(1,9)}
print(dd)