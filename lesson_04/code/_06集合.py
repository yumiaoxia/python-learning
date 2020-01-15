# 创建一个集合
# 集合不能包含集合
basket = {'apple','orange','apple','pear','orange','banana'}
basket2 = set(['apple','orange','banana','pear'])

print(basket)
print(basket2)

# 集合也支持推导式形式

a={x for x in 'abracadweasebse' if x not in 'abc'}
print(a)