#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato,
faça um programa que nos dê o salário bruto,
quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
Observe que Salário Bruto - Descontos = Salário Líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
	a. + Salário Bruto : R$
	b. - IR (11%) : R$
	c. - INSS (8%) : R$
	d. - Sindicato ( 5%) : R$
	e. = Salário Liquido : R$
'''

ganho = int(input("Valor ganho por hora: "))
horas = int(input("Número de horas trabalhadas por mês: "))

bruto = ganho * horas
ir = bruto * 11 / 100
inss = bruto * 8 / 100
sindicato = bruto * 5 / 100
liquido = bruto - ir - inss - sindicato

print ("O salário bruto é de R$ %.2f" %bruto)
print ("Você pagou R$ %.2f de INSS" %inss)
print ("Você pagou R$ %.2f ao Sindicato" %sindicato)
print ("O seu salário líquido é de R$ %.2f" %liquido)
#Coloquei em 4 print's diferentes pois a visualização fica melhor do que com o "\n"
