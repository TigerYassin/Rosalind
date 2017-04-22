"""
return the slice of a string from indices num1 through num2, and num3 through num4 with space in between


working
"""


a = raw_input('what is yo string')
num1 = input('enter the first index')
num2 = input('enter the second index')
num3 = input('enter the third index')
num4 = input('enter the fourth index')

print "Your string is:", "".join(a[num1:num2 +1]), "".join(a[num3: num4 +1])