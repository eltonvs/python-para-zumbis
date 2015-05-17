#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
'''

salario = float(input("Digite o valor do salario: "))
porcentagem = int(input("Digite a porcentagem do aumento: [Digite 50 para 50%] "))
aumento = salario * porcentagem / 100

print ("O aumento foi de R$ %.2f e o seu novo salário é de R$ %.2f" %(aumento, salario + aumento))
