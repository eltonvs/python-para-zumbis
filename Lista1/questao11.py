#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Sabendo que str() converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
'''

num = str(pow(2, 1000000))
print ("2 elevado a um milhão (1000000) possui %d dígitos" %len(num))
