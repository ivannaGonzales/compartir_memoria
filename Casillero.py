import multiprocessing as mp
import numpy as np
import ctypes as c
import random

class Casillero():
    def __init__(self,mutex, matriz):
        self.mutex = mutex
        self.matriz = matriz
    
    def anadir_numeros_aleatorios(self):
        print('Numeros aleatorios')
        n = len(self.matriz)
        m = len(self.matriz)
        i=0
        for nn in range(n):
            for mm in range(m):
                numero_aleatorio = random.randint(0,10000)
                self.matriz[nn][mm] = numero_aleatorio
                i=i+1

    def creacion_matriz(self,n,m):
        shared_array = mp.Array('i',n*m)
        shared_array = np.frombuffer(shared_array.get_obj(),c.c_int) 
        print('np array len=',len(shared_array))
        shared_array = shared_array.reshape((n,m))
        self.matriz = shared_array
        return shared_array
        
    def getMatriz(self):
        return self.matriz

    def get_mutex(self):
        return self.mutex
    
    def get_fila(self,identificador_fila):
        with self.get_mutex():
            return self.matriz[identificador_fila]
            
    def cambiar_fila(self,fila, identificador_fila):
        with self.get_mutex():
            self.matriz[identificador_fila] = fila

    