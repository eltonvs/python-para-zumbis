#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
'''

distancia = int(input("Distância Percorrida [Km]: "))
dias = int(input("Tempo de aluguel [Dias]: "))
valor = (distancia * 0.15) + (dias * 60)

print ("O valor total a pagar é de R$ %.2f" %valor)
