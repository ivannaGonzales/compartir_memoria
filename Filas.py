from Casilla import Casilla
from multiprocessing import Process, Manager
import numpy as np
import ctypes as c
import random
class Filas():
    def __init__(self,mutex, filas_ocupado):
        self.mutex = mutex
        self.filas_ocupado = filas_ocupado

    def ordenar_fila(self,fila):
        n = len(fila)
        for i in range(n-1):
            for j in range(n-i-1):
                if(fila[j] > fila[j+1]):
                        fila[j], fila[j+1] = fila[j+1], fila[j]
        return fila

    def get_filas_ocupado(self):
        return self.filas_ocupado

    def get_mutex(self):
        return self.mutex

    def get_filas_identificador(self):
        return self.filas_identificadores
    
    def get_filas_ocupado(self):
        return self.filas_ocupado
        
    def get_identificador_filas(self):
        fila_ocupado = False
        posicion_aleatoria = random.randint(0, 3)
        numero_procesos = 4
        intentos = 0
        
        with self.get_mutex():
            while not fila_ocupado and intentos < numero_procesos:
                fila_ocupado = not self.get_filas_ocupado()[posicion_aleatoria]
                intentos = intentos + 1
                if(not fila_ocupado):
                    if(posicion_aleatoria == 3):#osea que empece por el final
                        posicion_aleatoria = 0
                    else:
                        posicion_aleatoria = posicion_aleatoria + 1  
                else:
                    fila = self.set_ocupado_posicion(posicion_aleatoria)
            return posicion_aleatoria
                
    def set_ocupado_posicion(self, posicion):
        self.get_filas_ocupado()[posicion] = True



                    

