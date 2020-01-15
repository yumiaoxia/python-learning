函数
-----
## 函数简介
### 函数定义形式
函数定义使用关键字`def`开头，定义形式如下：
~~~python
def <函数名>(参数列表):  # 函数签名
	代码块...			# 函数体
	return <返回值>     # 函数体
~~~
注意: 
	1. python是一门语法严格的编程语言，函数第二行缩进编写函数体。
	2. 参数列表，函数体和return语句不是必须的，但函数签名是必须的
	3. 函数名和变量命名规范一致
	4. return语句的作用是结束该函数（程序执行到return语句，函数内return后面的语句将不会执行），并将函数的的数据暴露外面调用


## 函数参数

	无参： 是指函数定义是没有指定形参列表，调用时无需传入参数
	位置参数： 是指函数定义时指定形参的参数名，调用时需传入对应的实参
	默认参数： 默认参数是在函数定义时给定一个默认值，使用时函数的值可传可不传，不传则使用默认值
	关键字参数： 是指在函数定义是指定形参的参数名，调用时需使用赋值的形式传递实参
	带 * 参数： 带 * 参数分为两种：带 * 的表示接受元祖参数，带 ** 的表示接收字典作为参数

注意：
	1. 调用需传递多个参数时要注意传递顺序，关键字调用参数要在位置参数的后面
	2. 定义带 * 参数时， 带 * 的参数必须写在带 ** 的参数的前面
	3. 带 * 参数和其他参数一起使用时，带 * 参数不是必须写在最后，但调用时带 * 参数后的所有参数必须以关键字的形式传递
	4. 带 * 参数只能以位置参数的形式进行传递,不能使用关键字的形式进行传递
	5. ** 形参可以接受其他关键字参数，它会将这些参数统一保存到一个字典中，字典的 key 就是参数的名字

## 限制符的使用

		定义函数时可以使用限制符，限制符有两种 `*`和`/`: 使用 * 号限制符，表示后面的所有参数必须以关键字参数的形式进行传递，除非遇到其他限制符或者参数列表结束; 使用 / 号限制符，表示后面的所有参数必须以位置参数的形式进行传递，除非遇到其他限制符或者参数列表结束

注意：
		1. 当使用单个限制符时，限制符可以作为形参列表的第一个
		2. 当 * 号限制符和 / 号限制符同时使用时， / 号限制符必须在 * 号限制符前面，且第一个参数不能是限制符

## 打包和解包

	**打包**： 使用带 * 参数时，参数可以接收元祖或字典，可以称之为参数的打包传递
	**解包**： 解包就是在调用传递实参时参数前面带上*号，该参数必须是与函数形参列表对应的元祖或者字典

## 函数的嵌套
	函数是可以嵌套使用的，也作为返回值返回的

## 闭包

## 文档字符串
  在定义函数时，可以在函数内部编写文档字符串，文档字符串就是函数的说明
  当我们编写了文档字符串时，就可以通过help()函数查看函数的说明
  我们一般在函数的开头编写文档字符串

  函数定义时可以建议参数的类型，返回值的类型，不是强制

 ## 作用域
 	**全局作用域**： 在程序执行时创建，在程序执行结束时结束。函数以外的区域都是全局作用域
 	**函数作用域**： 在函数调用时创建，在函数调用结束时销毁。函数每调用一次产生一个新的函数作用域
 	1. 全局作用域定义的变量都属于全局变量，函数作用域定义的变量属于局部变量，局部变量只有在该函数作用域内有效
 	2. 函数作用域中可以访问到全局变量，全局作用域不可以直接访问函数中的局部变量
 	3. 函数作用域可以嵌套
 	4. 当使用一个变量时，优先在当前作用域中寻找，如果找到就使用，如果没有则会在上一级中寻找，如果找到就使用，如果没有就继续到上一级作用于寻找,以此类推，直到找到全局作用域，如果全局作用域没有则会抛出异常
 	5. 一般情况下，函数内部不能直接修改外部的变量的值，如果希望修改，则需要使用关键字声明该作用域的范围再做修改

 ## 命名空间

  - 命名空间指的是变量存储的位置，每一个变量都需要存储到指定的命名空间中
  - 每一个作用域都会有一个它对应的命名空间
  - 命名空间实际上就是一个字典，是一个专门用来存储变量的字典
  - locals()用来获取当前作用域的命名空间
  - globals() 用来获取全局作用域的命名空间
  - 向命名空间的字典中添加一个key-value就相当于在作用域中定义了一个新的变量

## 递归函数
递归函数的两个条件：
	1. 基线条件： 问题可以被分解为最小的条件，当满足最小基线条件时，递归就不再执行了
	2. 递归条件： 将问题继续分解的条件

## 函数式编程
	在python中，函数是一等对象，一等对象一般会具有如下特点：
		1. 对象是在运行时创建的
		2. 能赋值给变量或作为数据结构中的元素
		3. 能作为参数传递
		4. 能作为返回值返回

		高阶函数
			高阶函数至少要符合以下两个特点中的一个
				1. 接受一个或多个函数作为参数
				2. 将函数作为返回值返回


## 装饰器
	1. 通过带 * 参数 和带 ** 参数结合可以匹配任何形式的参数列表
	2. 通过装饰器可以在不修改原来的函数的情况下对原函数进行扩展或增强
	3. 可以通过注解使用一个或多个装饰器，使用多个装饰器时，后面的装饰器先起作用