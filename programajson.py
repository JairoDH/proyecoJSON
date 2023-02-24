from funciones import *


opcion = menu()
print (opcion)
while opcion != 6 : 
    if opcion == 1 :
        listar_personajes(personajes)
    elif opcion == 2:
        habilidades_personajes(personajes)
    opcion = menu()
