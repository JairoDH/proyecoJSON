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
    print("5. ")
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
                'habilidades': personaje['abilities']})
    print(f"personaje con dicha habilidad '{habilidad}':")
    for p in poder:
        print(f"Nombre: {p['nombre']}")
        print(f"Género: {p['genero']}") 
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