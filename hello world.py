# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:28:47 2023

@author: natalia
"""
f = open ('rosalind_ini5.txt', 'r')
for line in f:
    if line % 2 == 1:
        print (line)