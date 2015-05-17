#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Dados dois números inteiros positivos,
determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

#Sem Recursão
while n2 != 0:
	aux = n2
	n2 = n1 % n2
	n1 = aux
print ("Sem Recursão - MDC =", n1)

#Com Recursão
def mdc(x, y):
	if y == 0:
		return x
	else:
		return mdc(y, x % y)

print ("Com Recursão - MDC =", mdc(n1, n2))
