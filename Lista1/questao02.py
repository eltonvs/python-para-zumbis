#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
'''

metros = float(input("Valor em metros: "))
print ("O valor em milímetros é %.2f" %(metros * pow(10, 6)))
