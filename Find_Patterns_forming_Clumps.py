"""
http://rosalind.info/problems/ba1e/
"""
String = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'

start_Int = int(input('enter an index')) + 1
end_Int = start_Int + 5
print String[start_Int:end_Int]