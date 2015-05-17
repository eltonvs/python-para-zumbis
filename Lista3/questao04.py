#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores.
Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci.
F1 = 1, F2 = 1, F3 = 2, etc.
'''

f = [1, 1]
num = int(input("Digite um número: "))
i = 0

while num > len(f):
	f.append(f[i] + f[i + 1])
	i += 1

print ('O %d° número da sequência de Fibonacci é: %d' %(num,f[num-1]))
