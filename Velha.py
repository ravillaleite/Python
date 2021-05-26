# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:47:56 2021

@author: Rávilla

Projeto 1 do Curso de Python - Jogo da Velha
"""

import pandas as pd
import math
    
tabuleiro = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]    
    
#def begin():
print('Olá, esse é o jogo da velha! \nO jogador 1 utilizará X\n' 
          'O jogador 2 utilizará O')
print('Para jogar, você deverá informar o número da linha e da coluna' 
          'onde fará a jogada. Prontos?\n')
    
    #tabuleiro = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

print('    1     2     3')
print(' 1', tabuleiro[0], '\n 2',tabuleiro[1], '\n 3',tabuleiro[2])

jogar = 's'  
cont1 = 0
cont2 = 0  

def exibe_tabuleiro(jogador, jogada, tabuleiro1):
    
    tabuleiro_jogadas = list(jogada)
    linha = int(tabuleiro_jogadas[0])
    coluna = int(tabuleiro_jogadas[1])
    
    if jogador == '1':
        tabuleiro1[linha-1][coluna-1]= 'X'
    else:
        tabuleiro1[linha-1][coluna-1]= 'O'
    
    print(' 1', tabuleiro1[0], '\n 2',tabuleiro1[1], '\n 3',tabuleiro1[2])
    return tabuleiro1
    #print('    1     2     3')
    #print(' 1', tabuleiro1[0], '\n 2',tabuleiro1[1], '\n 3',tabuleiro1[2])
    

def entrada_jogadas(tab_jogadas):
    cont_jogadas = 0    
    
    while cont_jogadas < 9:
        
        if cont_jogadas == 0:
           print ("Jogador 1: ")
           jogada1 = (input())
           tab_jogadas = exibe_tabuleiro('1', jogada1, tab_jogadas)
        
        elif cont_jogadas%2 == 0:
            print ("Jogador 1: ")
            jogada1 = (input())
            tab_jogadas = exibe_tabuleiro('1', jogada1, tab_jogadas)
        
        else:
            print("Jogador 2: ")
            jogada2 = (input())
            tab_jogadas = exibe_tabuleiro('2', jogada2, tab_jogadas)   
            
        if cont_jogadas >= 4: #começar a conferir se há vencedor
            check = conferir_jogadas(tab_jogadas, cont_jogadas)
            
            
            if check == '1':
                print ("Jogador 1 é o vencedor!")
                break
            elif check == '2':
                print ("Jogador 2 é o vencedor!")
                break
            else:
                if cont_jogadas == 8:
                    print ("Houve um empate.")
                    break
            
        cont_jogadas+=1
        
def resultado(contador):
    
     if contador%2 == 0:
         return '1'
     else:
         return '2'
     
def conferir_jogadas(tab_jogadas, cont_jogadas):
    winner = 0
    for i in range (0, 1): # ----------------------------------------------------------------
        for j in range (0, 2): # ------------------------------------------------------------
            
            if i==0 and j ==0: # verificando o primeiro item
                if tab_jogadas[i][j] == tab_jogadas[i+1][j+1] == tab_jogadas[i+2][j+2]:
                    winner = resultado(cont_jogadas)
                    
                elif tab_jogadas[i][j] == tab_jogadas[i][j+1] == tab_jogadas[i][j+2]:
                    winner = resultado(cont_jogadas)
                    
                elif tab_jogadas[i][j] == tab_jogadas[i+1][j] == tab_jogadas[i+2][j]:
                    winner = resultado(cont_jogadas)
                j += 1
                
            elif i==0 and j!=0: #verificar as demais colunas
                if tab_jogadas[i][j] == tab_jogadas[i+1][j] == tab_jogadas[i+2][j]:
                    winner = resultado(cont_jogadas)
                j += 1
                
            else: #verificar as outras linhas
                
                if j == 2:
                    j = 0
                else:
                    if tab_jogadas[i+1][j] == tab_jogadas[i+1][j+1] == tab_jogadas[i+1][j+2]:
                        winner = resultado(cont_jogadas)
                
          # --------------------------------------------------------------------------------      
        i += 1
        # ----------------------------------------------------------------------------------
    return winner    
        
while jogar=='s':
    vencedor = entrada_jogadas(tabuleiro) 
    jogar = input("Deseja nogar novamente?\n    s/n")
    
"""   if vencedor == '1':
        cont1 +=1
    else:
        cont2 +=1
    jogar = input("s/n")
    
print ("Jogador 1: ", cont1, "vitórias\n"
       "Jogador 2: ", cont2, "vitórias")"""
        
        
        
        
        
        
        
        
        