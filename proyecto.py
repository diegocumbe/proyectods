# -*- coding: utf-8 -*-
"""
Editor de Spyder
Este es un archivo temporal
"""

import serial, time
arduino = serial.Serial('COM3', 9600)
i=0
#Se crea una lista para almacenar los valores recibidos
parametros = ["","","",""] 
#Ciclo While para tomar indefinidamente los datos que arroja el Arduino
while(True):
    i += 1
    print("-------------------------------")
    print("Datos", i,":\n")
    
    #Ciclo para imprimir los 4 datos recolectados
    for pos in range(4):
        time.sleep(1)
        rawString = arduino.readline().strip() #Lee los datos que arroja Arduino
        valores = rawString.decode('ascii') #Transforma el tipo Byte en String
        print(valores)
        parametros[pos] = valores
    print("\n",parametros)    
    print("-------------------------------") #Print para separar cada grupo

arduino.close()
