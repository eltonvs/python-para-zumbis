#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

while True:
	nota = float(input("Digite uma nota entre 0 e 10: "))
	if nota >= 0 and nota <= 10:
		break
	else:
		print ("A nota digitada é inválida!")

print ("A nota %d é válida!" %nota)
