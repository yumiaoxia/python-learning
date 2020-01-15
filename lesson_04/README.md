# 数据结构

## 列表的方法
- list.append(x) 在列表的末尾添加一个元素。相当于 a[len(a):] = [x]
- list.extend(iterable) 使用可迭代对象中的所有元素来扩展列表。相当于 a[len(a):] = iterable
- list.insert(i, x) 在给定位置插入一个元素。
- list.remove(x) 移除列表中第一个为 x 的元素。如果没有这样的元素则抛出 ValueError 异常
- list.pop([i]) 删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中最后的一个元素
- list.clear() 删除列表中的所有元素。相当于 del a[:]
- list.index(x[,start[,end]]) 返回列表中第一个值为 x 的元素的从0开始的索引。如果没有这样的元素则抛出 ValueError 的异常。
- list.count(x) 返回元素 x 在列表中出现的次数
- list.sort(key=None,reverse=false) 对列表中的元素进行排序
- list.reverse() 对列表中的元素进行反转
- list.copy() 返回列表的一个前拷贝


## 列表作为栈使用

栈的特点： 类比一个一段开口的筒子，后进先出，先进后出

## 列表作为队列使用

队列的特点： 类比一个水管，元素就如水管里流动的水，先进先出，后进后出
标准库： collections.deque

## 列表与栈的共同点

都是一个数据容器

## 列表推导式

## 嵌套列表推导式

## 元组和序列

**序列**： list,tuple,range
创建一个元组： t = 12,1334,3444

## 集合（Set）

集合： 集合是又不重复元素组成无序的数据集。它的基本用法包括成员检测和消除重复元素。
集合对象也支持 联合，交集，差集，对称差分等数学运算
集合也支持推导式形式

## 字典(Dict)

字典是一种映射类型的数据结构，它是以不可变类型关键字为索引的，在其它语言里可能会被叫做*联合内存* 或 *联合数组*。

字典的关键字是不可变类型，通常是字符串或者数字。如果一个元组只包含字符串、数字或者元组，那么这个元组也可以用作关键字。

理解字典最好的方式是将他看作一个 键-值 对的集合，一对 {} 可以创建一个空字典

