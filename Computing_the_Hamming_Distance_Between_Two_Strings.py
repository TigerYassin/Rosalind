"""

http://rosalind.info/problems/ba1g/
Compute the Hamming Distance Between Two Strings



Working
"""


def Calculate_Dist(String1, String2):
    count = 0

    for x in range(len(String1)):
        if not String1[x] == String2[x]:
            count += 1
    return count

String1 = raw_input('enter your first string bruh')



String2 = raw_input('enter your second String Dude')

print Calculate_Dist(String1, String2)