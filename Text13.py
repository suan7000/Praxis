# from sys import argv
import sys

# address, first, second, third, fourth = argv

"""
address = argv[0]
first = argv[1]
second = argv[2]
third = argv[3]
fourth = argv[4]
"""

"""
print "The script is called:", argv[0]
print "Your first variable is:", argv[1]
print "Your second variable is:", argv[2]
print "Your third variable is:", argv[3]
print "Your fourth variable is:", argv[4]
"""

print "The script is called:", sys.argv[0]
print "Your first variable is:", sys.argv[1]
print "Your second variable is:", sys.argv[2]
print "Your third variable is:", sys.argv[3]
print "Your fourth variable is:", sys.argv[4]

print "sys.argv[0:] is:", sys.argv[0:]
print "sys.argv[2:] is:", sys.argv[2:]
print "sys.argv[:2] is:", sys.argv[:2]

