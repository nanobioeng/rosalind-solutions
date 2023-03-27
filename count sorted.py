# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:28:47 2023

@author: natalia
"""

q = 'CCATGATAGTCCTAACCGCCTCGACATACACAAATAGTGGCCACACTACTCACGCAGCCGCGTAAGCGCACCCTGCCGTTGAGAACGTGCTGTCCGGTAACCAATAAGTCTATCCCTCGGCAGACATCAAGGTGGGATTAGCGCCGAAAATGTTTTTATATTGCGTCTGCTATAGAAACTGGTAGGGACGGGCATCTGTCATGTAATGTTGTACTGAAAGCGACTTTAGGCCGGACGAATCCAAAACTCTGCGGGGCTTGTCGGAAGGCCCTAAGGGATACATAACCCCAGACTTTGGAATCCGGGCGAAAATCGATAACACATCGGAGAGCAAGAGAAACAATAGAACCATCTCGCTTTTTTGCTGCTCATTGGCCCATAACTCATTGTGAGCAGCCTCACACCTAATAGACGCGTTTTATTTCATCCGATGATGATGAAGATGGGGGTGTAAAAACACAGAGTCTCACGGTGCGCATAGCCCTGGCACCCATACGCCTACGAGTGTCACGACAACGTCGTGGACAGTTTCCCTTAGGCGACGCACATGGCGACAGGTCCGGGGCCCAGAATGCCATTGTCCGAAGAGTCCTGTCCGTTCATCCTCTAGAATATGCGGCCTACACTGAAATTCCCATCCCTGTTGCAGTCGAATTTACGCCTCTCAGCAGGTAGCCAGCTTAACTGCACACCCGCGTGTCCCGTGAAGCCCAAAATGCAAAAAGCGAGGGAAGAAAGGGGTGCATACGTTTATACGTCTAAAAAAGTTCAGCAAGTAGGAACAATTTCTCCTAGAATAAGCGCACGGACTGTTATATCTTGGTGTTGTTTCGGGTCTAATTCATGCATT'
dictionary = {}

for letter in str(q):
    
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1
        
for i in sorted(dictionary.items()):
    print (i)

for key, value in sorted(dictionary.items()):
    print (value)