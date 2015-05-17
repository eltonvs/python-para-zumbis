#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
'''

preco = float(input("Digite o valor da mercadoria: "))
porcentagem = int(input("Digite o percentual de desconto: [Digite 50 para 50%] "))
desconto = preco * porcentagem / 100

print ("O valor do desconto: R$ %.2f\nValor da mercadoria com desconto: R$ %.2f" %(desconto, preco - desconto))
