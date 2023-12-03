from multiprocessing import Process, Array

def worker(array, posicion):
   # Cambiar el valor en la posición especificada a True
   array[posicion] = True

if __name__ == '__main__':
   # Crear un array de booleanos
   array = Array('b', [False] * 10)

   # Crear dos procesos que cambian el valor en las posiciones especificadas a True
   process1 = Process(target=worker, args=(array, 0))
   process2 = Process(target=worker, args=(array, 1))

   # Iniciar los procesos
   process1.start()
   process2.start()

   # Esperar a que los procesos terminen
   process1.join()
   process2.join()

   # Imprimir el array
   print(array[:])
