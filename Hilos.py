from Proceso import Proceso
from Casillero import Casillero
from Filas import Filas
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Lock, Array
import multiprocessing as mp
import numpy as np
import ctypes as c
import time
import subprocess
import os
import threading
class Hilos():
    def __init__(self, hilos):
        self.hilos = hilos
    
    def ordenar_matriz(self,filas, identificador, casillero):
        print(f"PID: {os.getpid()}")
        comando = f"ps -p {os.getpid()} -o pid,ppid,cmd,psr,%mem,%cpu"
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate(timeout=1)
        if error:
            print(f"Error al obtener información del proceso: {error}")
        elif salida:
            print(salida.decode())
            posicion_valida = filas.get_identificador_filas()
            fila = casillero.get_fila(posicion_valida)
            fila_ordenada = filas.ordenar_fila(fila)

        print('El proceso con identificador', identificador, 'ha modificado el array con posicion', posicion_valida,
        'del casillero')

        casillero.cambiar_fila(fila_ordenada, posicion_valida)

    def crear_hilos(self):
        numero_hilos = 4
        ####
        mutex_casillero = threading.Lock()
        casillero = Casillero(mutex_casillero,[])
        casillero.creacion_matriz(4,10000)
        casillero.anadir_numeros_aleatorios()
        print(casillero.getMatriz(),'matriz')
        ####
        #le tengo que pasar la matriz y todas las filas
        mutex_filas = threading.Lock()
        array_ocupado =[False] * numero_hilos
        print(array_ocupado)
        filas = Filas(mutex_filas, array_ocupado)
        ##
        for identificador in range(numero_hilos):
            proceso = Process(target = self.ordenar_matriz, args=(filas, identificador, casillero))
            self.hilos.append(proceso)
        tiempo_inicio = time.time()
        for proceso in self.hilos:
            proceso.start()
        for proceso in self.hilos:
            proceso.join()
        tiempo_final = time.time()
        tiempo_ejecucion = tiempo_final - tiempo_inicio
        print(tiempo_ejecucion, 'tiempo en ejecucion')
        print(casillero.getMatriz())