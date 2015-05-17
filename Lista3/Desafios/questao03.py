#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Verifique se um inteiro positivo n é primo.
'''

n = int(input("Digite o número para verificar se é primo: "))
c, d = 1, 0

while c <= n:
	if n % c == 0:
		d += 1
	c += 1

if d > 2:
	print ("O número %d não é primo" %n)
else:
	print ("O número %d é primo" %n)
