# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:43:28 2023

@author: natalia
"""

dna = open("rosalind_revc.txt", 'r').read()
print(dna)

#first replace atcg with bdef and then replace bdef with tagc

first = dna.replace('A','B',).replace('T','D').replace('G','F').replace('C','E')
second = first.replace('B','T').replace('D', 'A').replace('E', 'G').replace('F','C')
print (second)
rna = second[::-1]
print (rna)