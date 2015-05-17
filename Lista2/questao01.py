#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Faça um Programa que peça os três lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''

a = int(input("Digite o valor do primeiro lado do triangulo: "))
b = int(input("Digite o valor do segundo lado do triangulo: "))
c = int(input("Digite o valor do terceiro lado do triangulo: "))

if abs(b - c) < a and a < b + c and abs(a - c) < b and b < a + c and abs(a - b) < c and c < a + b:
	print ("Os valores informados formam um triângulo")
	if a == b and b == c:
		print ("O triângulo é equilátero")
	elif a == b or b == c or a == c:
		print ("O triângulo é isósceles")
	else:
		print ("O triângulo é escaleno")
else:
	print ("Os valores informados não podem formar um triângulo")
