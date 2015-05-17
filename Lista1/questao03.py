#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
'''

dias = int(input("Digite o número de dias: "))
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

horas += dias * 24
minutos += horas * 60
segundos += minutos * 60

print("O tempo total digitado em segundos é %d" %segundos)
