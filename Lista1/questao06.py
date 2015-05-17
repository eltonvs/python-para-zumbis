#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''

distancia = int(input("Distância a ser percorrida [Km]: "))
velocidade = int(input("Velocidade média esperada [Km/h]: "))

print ("O tempo de viagem será de %.2f horas" %(distancia/velocidade))
