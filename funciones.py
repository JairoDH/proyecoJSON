import json 
import os

with open('proyectojson.json') as p:
    personajes = json.load(p)
    


def menu():
    print("Menu: ")
    print("1. Información de personajes: ")
    print("2. Habilidades del personaje: ")
    print("3. Dime una habilidad: ")
    print("4. Poder Ki: ")
    print("5. Combates.")
    print("6. Salir")
    opcion = int(input("Selecciona una opcion: "))
    return opcion


def listar_personajes(personajes):

    for personaje in personajes['characters']:
        print("El personaje, ",personaje['id'],": ",personaje['bio'])
        print()

def habilidades_personajes(personajes):
    nombre = input("Dime el nombre del pesonaje: ")
    for personaje in personajes['characters']:
        if personaje['id'] == nombre:
            print("Las habilidades de: ",personaje['id'], "son, ",personaje['abilities'])

def pedir_habilidad(personajes):
    habilidad = input("Dime el nombre de la habilidad: ")
    poder = []
    for personaje in personajes['characters']:
        if habilidad in personaje['abilities']:
            poder.append({
                'nombre': personaje['id'],
                'genero': personaje['gender'],
                'raza'  : personaje['race'],
                'habilidades': personaje['abilities']})
    print(f"personaje con dicha habilidad '{habilidad}':")
    for p in poder:
        print(f"Nombre: {p['nombre']}")
        print(f"Género: {p['genero']}")
        print(f"Raza: {p['raza']}")
        print(f"Habilidades: {','.join(p['habilidades'])}")
        print()

def pedir_nivelKi(personajes):
    ki = input("Cuánto poder KI quieres ver (nn):  ")
    poderki = []
    for personaje in personajes['characters']:
        if personaje['kiRestoreSpeed'] >= ki:
            poderki.append(personaje)
    if not poderki:
        print("No hay personaje con ese nivel de ki")
    else:
        print("Personajes con nivel superior o igual al ki: ")
        for personaje in poderki:
            print(f" - {personaje['name']} ({personaje['kiRestoreSpeed']})")

def combate_personajes(personajes):
    personaje1 = input("Dime el primer oponente: ")
    personaje2 = input("Dime el segundo oponente: ")

    oponentes = []
    personaje1_encontrado = False
    personaje2_encontrado = False
    for personaje in personajes['characters']:
        if personaje1 == personaje['id']:
            oponentes.append(personaje)
            personaje1_encontrado = True
        if personaje2 == personaje['id']:    
            oponentes.append(personaje)
            personaje2_encontrado = True
    if not personaje1_encontrado:
        print("Primer personaje no encontrado")
    if not personaje2_encontrado:
        print("Segundo personaje no encontrado")

    ganador = None
    
    for estadistica in ['health','attack','defense']:
        if oponentes[0][estadistica] > oponentes[1][estadistica]:
            ganador = oponentes[0]
            
        elif oponentes[0][estadistica] < oponentes[1][estadistica]:
            ganador = oponentes[1]
    
        else: 
            print(f"Es un empate en{estadistica}!")
    if ganador is not None:
        print(f"El ganador es {ganador['name']} con {ganador['health']} de salud, {ganador['attack']} puntos de ataque y {ganador['defense']} de defensa!!")   
    

    
        
