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
class Procesos():
    def __init__(self, procesos):
        self.procesos = procesos
    
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

    def crear_procesos(self):
        numero_procesos = 4
        ####
        mutex_casillero = Lock()
        casillero = Casillero(mutex_casillero,[])
        casillero.creacion_matriz(4,10000)
        casillero.anadir_numeros_aleatorios()
        print(casillero.getMatriz(),'matriz')
        ####
        #le tengo que pasar la matriz y todas las filas
        mutex = Lock()
        array_ocupado = Array('b', [False] * numero_procesos)
        filas = Filas(mutex, array_ocupado)
        ##
        for identificador in range(numero_procesos):
            proceso = Process(target = self.ordenar_matriz, args=(filas, identificador, casillero))
            self.procesos.append(proceso)
        tiempo_inicio = time.time()
        for proceso in self.procesos:
            proceso.start()
        for proceso in self.procesos:
            proceso.join()
        tiempo_final = time.time()
        tiempo_ejecucion = tiempo_final - tiempo_inicio
        print(tiempo_ejecucion, 'tiempo en ejecucion')
        print(casillero.getMatriz())