# -*-coding:utf-8-*-

# 做一个四则运算计算器，并运行


def add(a, b):
    print " %d + %d = %d" % (a, b, a + b)


def sub(a, b):
    print " %d - %d = %d" % (a, b, a - b)


def mul(a, b):
    print " %d * %d = %d" % (a, b, a * b)


def div(a, b):
    print " %d / %d = %d %% %d" % (a, b, a / b, a % b)


x = 10
y = 3

add(x, y)
sub(x, y)
mul(x, y)
div(x, y)