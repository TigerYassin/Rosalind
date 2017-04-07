a = input('select a number')
b = input('select another number') + 1
c = 0

for x in range(a, b):
    if (not x %2 == 0):
        c = c + x
print c