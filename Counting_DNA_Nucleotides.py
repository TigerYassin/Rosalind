"""
count how many times each DNA char appears


working
"""


def Count(String1):

    A = 0
    G = 0
    T = 0
    C = 0
    for x in String1:
        if x == 'A':
            A +=1
        if x == 'G':
            G +=1
        if x == 'T':
            T +=1
        if x == 'C':
            C +=1
    return A, C, G, T


print Count(raw_input("enter you string"))