# -*-coding:utf-8-*-

# 从sys模组中提取argv参数
from sys import argv
# 将argv参数赋值为script， input_file
# script为文件脚本路径
# input_file为文件名
script, input_file = argv

# 定义print_all()函数，接受一个参数，打印该参数的读取内容
def print_all(f):
    print f.read()

# 定义rewind()函数，接受一个参数，将读取指针指向起点
def rewind(f):
    f.seek(0)

# 定义print_a_line()函数，接受两个参数，打印第一个参数和第二个参数的读取内容的当前行
def print_a_line(line_count, f):
    print line_count, f.readline()

# open()方法打开input_file文件，赋值给current_file
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
