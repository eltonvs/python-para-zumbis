#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100.
Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
Imprima os três vetores.
'''

from random import randint

vet1, vet2, vet3 = [], [], []
for i in range(10):
	vet1.append(randint(1, 100))
	vet2.append(randint(1, 100))
	vet3.append(vet1[i])
	vet3.append(vet2[i])

print(vet1)
print(vet2)
print(vet3)
