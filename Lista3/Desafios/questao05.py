#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Faça um programa que peça um inteiro positivo e o mostre invertido.
Ex.: 1234 gera 4321
'''

num = str(int(input("Digite o número que será invertido: ")))
array_num = []
array_num_inv = []

for digit in num:
	array_num.append(int(digit))

i = len(array_num) - 1
j = i

while i >= 0:
	array_num_inv.append(array_num[i])
	i -= 1

num_inv = ''.join(map(str, array_num_inv))

print ("O número %s ficou %s" %(num, num_inv))
#Deixei o número invertido como string para continuar com o 0 à esquerda (quando houver)
