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

ced50 = int(troco/50)
ced20 = int(troco%50/20)
ced10 = int(troco%50%20/10)
ced5 = int(troco%50%20%10/5)
ced2 = int(troco%50%20%10%5/2)
ced1 = int(troco%50%20%10%5%2)

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
