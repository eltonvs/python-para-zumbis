#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
'''

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (9 * celsius / 5) + 32

print ("A temperatura em Fahrenheit é %.2f °F" %fahrenheit)
