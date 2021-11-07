main=360
def check_full(value, main=360):
    ...
    
from time import sleep 
import math 
def calcular_porcentos(maxim,comming):
    try:
        porcento=(100 *(maxim-comming))/maxim
        print(f'processing : {round(porcento)} % \t from {maxim} in {comming}')
        os.system('clear')
        if porcento>=99:
            import os
            os.system('clear')
            print('Upload full uploaded')
    except:
        print(0)

max=360

for i in range(max+1,1,-1):
    sleep(0.1)
    calcular_porcentos(max,i)
    
