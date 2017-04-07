def Profile(String1, String2, String3, String4, String5, String6, String7):
    myString1 = []
    x = 0
    while(x < 7):
        myString1.append(String1[x])
        x+=1
    print ''.join(myString1)




Profile('ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT')