"""
return a file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.



working
"""


i = 1
f = open('/home/yassin/whatever.txt')
for line in f.readlines():
    if i % 2 == 0 :
        print line # must remove spaces from output
    i += 1