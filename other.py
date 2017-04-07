String1 = raw_input('please enter a word')
String2 = raw_input("please enter another word")
Array = []

for x in range(len(String1)):
    Array.append(String1[x])


for x in range(len(String2)):
    if String2[x] in Array:
        Array.remove(String2[x])

print len(Array)


# myDict1 = {
#     "A" : String1.count("A"),
#     "B" : String1.count("B"),
#     "C" : String1.count("C"),
#     "D" : String1.count("D"),
#     "E" : String1.count("E"),
#     "F" : String1.count("F"),
#     "G" : String1.count("G"),
#     "H" : String1.count("H"),
#     "I" : String1.count("I"),
#     "J" : String1.count("J"),
#     "K" : String1.count("K"),
#     "L" : String1.count("L"),
#     "M" : String1.count("M"),
#     "N" : String1.count("N"),
#     "O" : String1.count("O"),
#     "P" : String1.count("P"),
#     "Q" : String1.count("Q"),
#     "R" : String1.count("R"),
#     "S" : String1.count("S"),
#     "T" : String1.count("T"),
#     "U" : String1.count("U"),
#     "V" : String1.count("V"),
#     "W" : String1.count("W"),
#     "X" : String1.count("X"),
#     "Y" : String1.count("Y"),
#     "Z" : String1.count("Z")
# }
#
# myDict2 = {
#     "A" : String2.count("A"),
#     "B" : String2.count("B"),
#     "C" : String2.count("C"),
#     "D" : String2.count("D"),
#     "E" : String2.count("E"),
#     "F" : String2.count("F"),
#     "G" : String2.count("G"),
#     "H" : String2.count("H"),
#     "I" : String2.count("I"),
#     "J" : String2.count("J"),
#     "K" : String2.count("K"),
#     "L" : String2.count("L"),
#     "M" : String2.count("M"),
#     "N" : String2.count("N"),
#     "O" : String2.count("O"),
#     "P" : String2.count("P"),
#     "Q" : String2.count("Q"),
#     "R" : String2.count("R"),
#     "S" : String2.count("S"),
#     "T" : String2.count("T"),
#     "U" : String2.count("U"),
#     "V" : String2.count("V"),
#     "W" : String2.count("W"),
#     "X" : String2.count("X"),
#     "Y" : String2.count("Y"),
#     "Z" : String2.count("Z")
#
# }
#
# print myDict1['A'] - myDict2['A']
# print myDict1['B'] - myDict2['B']
# print myDict1['C'] - myDict2['C']
# print myDict1['D'] - myDict2['D']
# print myDict1['E'] - myDict2['E']
# print myDict1['F'] - myDict2['F']
# print myDict1['G'] - myDict2['G']
# print myDict1['H'] - myDict2['H']
# print myDict1['I'] - myDict2['I']
# print myDict1['J'] - myDict2['J']
# print myDict1['K'] - myDict2['K']
# print myDict1['L'] - myDict2['L']
# print myDict1['M'] - myDict2['M']
# print myDict1['N'] - myDict2['N']
# print myDict1['O'] - myDict2['O']
# print myDict1['P'] - myDict2['P']
# print myDict1['Q'] - myDict2['Q']
# print myDict1['R'] - myDict2['R']
# print myDict1["S"] - myDict2['S']
# print myDict1['T'] - myDict2['T']
# print myDict1['U'] - myDict2['U']
# print myDict1['V'] - myDict2['V']
# print myDict1['W'] - myDict2['W']
# print myDict1['X'] - myDict2['X']
# print myDict1['Y'] - myDict2['Y']
# print myDict1['Z'] - myDict2['Z']