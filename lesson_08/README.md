# IO操作

## 文件IO
     open()： 调用open()打开一个文件，可以将文件分成两种类型：一种是纯文本文件（存放文本字符）；另一种是二进制文件(图片，MP3...)。open()的参数很多，mode 是打开文件的模式（只读，只写，读写，...); encoding指定打开文本文件的编码（gbk,utf-8,...）
     file.close(): 关闭一个文件（file是文件的实例）
     with open("myFile.txt") as file: with语句打开的文件会在with语句结束时释放文件资源
