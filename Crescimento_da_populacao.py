# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:29:09 2020

@author: Rávilla
"""

import matplotlib.pyplot as plt
import pandas as pd

dados = open("populacao_brasileira.csv").readlines()
ano = []
pop = []


for i in range (1, len(dados)):
    linha = dados[i].split(";")
    
    ano.append(int(linha[0]))
    pop.append(int(linha[1]))
    if (pop[i-1] >= 150000000) and (pop[i-2] < 150000000):
        print (ano[i-1])


plt.plot(ano, pop, color = 'red', linestyle = "--")
#plt.bar(ano, pop, color = "pink")
plt.title("Crescimento da População Brasileira")
plt.xlabel ("Ano")
plt.ylabel ("População x 10^8")
#plt.show()
plt.savefig("Grafico_Populacao_Brasileira.png", dpi = 300)
