# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:39:52 2020

@author: Bill
"""

def function_weigth():
    
     H = input("Inserisci il tuo peso: ")
     
     type = input("è in kg(1) o lbs(2): ")
     
     if(type == '1'):
         peso =  int(H)/0.45
         print (f'Questo è il peso in lbs {peso}')
     
     elif(type == '2'):
         peso = int(H) * 0.45
         print (f'Questo è il peso in kg {peso}')

function_weigth()