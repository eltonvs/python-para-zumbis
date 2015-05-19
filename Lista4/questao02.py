#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Sorteie 20 inteiros entre 1 e 100 numa lista.
Armazene os números pares na lista PAR e os números ímpares na lista IMPAR.
Imprima as três listas.
'''

import random

num, par, impar = [], [], []

for i in range(0, 20):
	num.append(random.randint(1, 100))
	if num[i] % 2 == 0:
		par.append(num[i])
	else:
		impar.append(num[i])

print ("Os números sorteados foram:", num)
print ("São pares:", par)
print ("São ímpares:", impar)
