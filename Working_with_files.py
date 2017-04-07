i = 1
f = open('/home/yassin/whatever.txt')
for line in f.readlines():
    if i % 2 == 0 :
        print line # must remove spaces from output
    i += 1