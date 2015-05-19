#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor,
sem usar as funções max e min.
'''

import random

maior, menor = 0, 100

for i in range(0, 10):
	num = random.randint(1, 100)
	if num > maior:
		maior = num
	if num < menor:
		menor = num

print ("O maior valor sorteado foi %d e o menor foi %d" %(maior, menor))
