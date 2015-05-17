#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a > b and a > c:
	print ("O maior número foi %d" %a)
elif b > a and b > c:
	print ("O maior número foi %d" %b)
else:
	print ("O maior número foi %d" %c)

if a < b and a < c:
	print ("O menor número foi %d" %a)
elif b < a and b < c:
	print ("O menor número foi %d" %b)
else:
	print ("O menor número foi %d" %c)
