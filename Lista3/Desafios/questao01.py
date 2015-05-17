#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120.
Dado um inteiro não-negativo n, verificar se n é triangular.
'''

n = int(input("Digite o número que você quer saber se é triangular: "))
a, b, c = -2, -1, 0

while c <= pow(n, 1/2):
	d = a * b * c
	if d == n:
		triangular = "%d é um número triangular, pois %d x %d x %d = %d" %(n, a, b, c, n)
		break
	else:
		triangular = "%d não é um número triangular" %n
	a, b, c = a + 1, b + 1, c + 1

print (triangular)
