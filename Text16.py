# -*-coding:utf-8-*-

# 打开一个txt文件，完成输出-删除-写入-输出操作
from sys import argv

filename = argv[1]

a = open(filename, 'r')
print "The old file %s's content is：" % filename
print a.read()
a.close()

a = open(filename, 'w')
a.truncate()
a.close()

a = open(filename, 'r')
print "The erase file %s's content is：" % filename
print a.read()
a.close()

a = open(filename, 'w')
line1 = raw_input("Enter line1: ")
line2 = raw_input("Enter line2: ")
a.write(line1 + "\n" + line2)
a.close()

a = open(filename, 'r')
print "The new file %s's content is：" % filename
print a.read()
a.close()




