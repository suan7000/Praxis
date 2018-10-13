# -*-coding:utf-8-*-

# 从sys模块中提取argv列表
from sys import argv
# 将argv列表解包，赋值给变量script, filename
# script为脚本路径
# filename为txt文件全称（带后缀.txt）
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If yo do want that, hit RETURN."

print "Opening the file..."

# open（）方法用写入（'w'）方式打开filename，将返回值赋值给target
target = open(filename, 'w')

print "Truncating the file. Goodbye!"

# truncate()方法截断当前位置后面所有字符
# target.truncate()删除target文件所有内容
target.truncate()

print "Now I'm going to ask you for three lines."

# raw_input()方法输入一个字符串，并将返回值赋值给line1
line1 = raw_input("line 1: ")
# raw_input()方法输入一个字符串，并将返回值赋值给line2
line2 = raw_input("line 2: ")
# raw_input()方法输入一个字符串，并将返回值赋值给line3
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write()方法写入第一行输入
# target.write(line1)在target文件中写入line1
target.write(line1)
target.write("\n")
# write()方法写入line2
target.write(line2)
target.write("\n")
# write()方法写入line3
target.write(line3)
target.write("\n")

print "And finally, we close it."

# close()方法结束target文件
target.close()

