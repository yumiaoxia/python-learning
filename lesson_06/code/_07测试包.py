import package.__init__ as init
from package import module1

init.test()
module1.module1_fun()

# 每个包必须包含一个__init__.py 的模块，这个模块也可以被其他模块引入使用
# 包里面的模块可以相互引入，也可以被包外部的模块引入使用