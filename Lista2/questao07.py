#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Obs.: somente são vendidos um número inteiro de latas.
'''

area = float(input("Informe a área a ser pintada [m²]: "))
litros = area / 3

if litros % 18 == 0:
	latas = litros / 18
else:
	latas = int(litros/18) + 1

print ("Número de latas de tinta usadas: %d\nValor total a ser gasto: R$ %.2f" %(latas, latas * 80))
