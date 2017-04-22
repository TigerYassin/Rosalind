"""
print out the fibonacci value of the index given


working
"""


a = 0
b = 1

myList = []

myNum = input("what is your number")
for x in range(myNum +1):
    myList.append(a)
    a = b
    b = a + myList[x]

print myList[myNum]