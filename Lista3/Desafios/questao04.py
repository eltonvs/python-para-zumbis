#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Dado um número inteiro positivo,
determine a sua decomposição em fatores primos calculando também a multiplicidade de cada fator.
'''

n = int(input("Digite um número: "))

#Com Recursão
fatores = []
def fatoracao(n, j):
	while n > 1:
		if n % j == 0:
			n = n / j
			fatores.append(j)
			return fatoracao(n, 2)
		else:
			j += 1
			return fatoracao(n, j)
	return fatores

print ("A decomposição do número informado é:", fatoracao(n, 2))

#Sem Recursão
fatores = []
j = 2
while n > 1:
	if n % j == 0:
		n = n / j
		fatores.append(j)
	else:
		j += 1

print ("A decomposição do número informado é:", fatores)
