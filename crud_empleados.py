import os
import json
os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)
    
def menu_general():
    os.system("cls")
    print("1. Crear empleado")
    print("2. Actualizar empleado")
    print("3. Eliminar empleado")
    print("4. Listar empleados")
    print("5. Salir")

def seleccionar_opcion(max_option):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese la opcion que deseas: >> "))
        except:
            pass
        
        if opcion < 1 or opcion > max_option:
            input("Error, presiona para continuar >> ")
        else:
            return opcion

def iniciar_programa():
    while True:
        opcion = seleccionar_opcion(5)

        if opcion == 1:
            print("1. Crear empleado")
        elif opcion == 2:
            print("2. Actualizar empleado")
        elif opcion == 3:
            print("3. Eliminar empleado")
        elif opcion == 4:
            print("4. Listar empleados")
        elif opcion == 5:
            
            return
        
        input




        empleados = cargar_json('./crud/empleados.json')
        print(empleados)

iniciar_programa()