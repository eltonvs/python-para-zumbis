#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá.
Exiba o total de dias.
'''

cigarros = int(input("Número de cigarros fumados por dia: "))
tempo = int(input("Há quantos anos fuma: "))

num_cigarros = cigarros * tempo * 365
dias = (num_cigarros * 10) / (60 * 24)

print ("Você já perdeu %d dias de vida" %dias)
