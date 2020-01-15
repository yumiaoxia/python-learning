
# 在一个模块中，通过 `import <模块名>` 引入外部模块。可以通过 import 引入同一个模块多次，但模块实例只有一个
# import 语句一般写在模块的开头
# 每个模块都有一个属性：__name__，通过这个属性可以获取到模块的名字
# 程序当前执行的模块称为主模块，主模块的__name__属性时：__main__
# 可以通过 `from <模块名> import <变量名>` 引入模块的部分成员
# 一般不建议使用 * 号引入外部模块的所有成员（覆盖，资源浪费）
import module1 as m1
from module1 import a,_b

print(m1.__name__)
m1.test_hello()

print(m1.a)
print(m1._b)
print(m1.__c)
print(a,_b)

