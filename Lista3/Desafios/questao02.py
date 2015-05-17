#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas.
Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos.
Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais,
e que nenhuma delas esteja em falta no caixa.
'''

conta = int(input("Digite o valor total da conta: "))
pago = int(input("Digite o valor pago: "))
troco = pago - conta
ced50, ced20, ced10, ced5, ced2, ced1 = 0, 0, 0, 0, 0, 0

while troco != 0:
	if troco >= 50:
		troco -= 50
		ced50 += 1
	elif troco >= 20:
		troco -= 20
		ced20 += 1
	elif troco >= 10:
		troco -= 10
		ced10 += 1
	elif troco >= 5:
		troco -= 5
		ced5 += 1
	elif troco >= 2:
		troco -= 2
		ced2 += 1
	elif troco >= 1:
		troco -= 1
		ced1 += 1

print ("O troco deverá ser dado com:")
if ced50 > 0:
	print ("%d cédulas de R$ 50,00" %ced50)
if ced20 > 0:
	print ("%d cédulas de R$ 20,00" %ced20)
if ced10 > 0:
	print ("%d cédulas de R$ 10,00" %ced10)
if ced5 > 0:
	print ("%d cédulas de R$ 5,00" %ced5)
if ced2 > 0:
	print ("%d cédulas de R$ 2,00" %ced2)
if ced1 > 0:
	print ("%d cédulas de R$ 1,00" %ced1)
