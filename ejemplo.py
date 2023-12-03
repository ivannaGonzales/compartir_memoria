import multiprocessing as mp
import numpy as np
import ctypes as c
import random
import os

def creacion_matriz(n,m):
    shared_array = mp.Array('i',n*m)
    shared_array = np.frombuffer(shared_array.get_obj(),c.c_int) 
    print('np array len=',len(shared_array))
    shared_array = shared_array.reshape((n,m))
    return shared_array

def ordenar_matriz(matrix):
    info('Proceso ordenar matriz')
    print()
    flattened = matrix.reshape(-1)
    flattened.sort()
    matrix[:] = np.array(flattened).reshape(matrix.shape)

def anadir_numeros_aleatorios(mp_arr):
    info('Proceso anadir numeros aleatorios')
    print()
    n = len(mp_arr)
    m = len(mp_arr)
    i=0
    for nn in range(n):
        for mm in range(m):
            numero_aleatorio = random.randint(0,100)
            mp_arr[nn][mm] = numero_aleatorio
            i=i+1
def transponer_matriz(matriz):
    info('Proceso anadir transponer matriz')
    print()
    matriz = matriz.transpose()

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

if __name__=='__main__':
    with mp.Manager() as manager:
        matriz = creacion_matriz(10,10)
        print(matriz)
        #
        p_matriz_aleatorios = mp.Process(target = anadir_numeros_aleatorios,args=(matriz,))
        p_matriz_aleatorios.start()
        p_matriz_aleatorios.join()
        #
        #p_matriz_ordenada = mp.Process(target=ordenar_matriz, args=(matriz,))
        #p_matriz_ordenada.start()
        #p_matriz_ordenada.join()
        #
        #p_matriz_traspuesta = mp.Process(target=transponer_matriz, args=(matriz,))
        #p_matriz_traspuesta.start()
        #p_matriz_traspuesta.join()
        print(matriz[:])




