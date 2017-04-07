"""
http://rosalind.info/problems/ba1d/
"""


def find(String, pattern):
    x = 0
    while x < len(pattern):
        for t in range(len(String)):
            if pattern[x] == String[0]:
                print String.index(pattern[t])
        x+=1



find('sfATATATGCATATACTT', 'ATAT')