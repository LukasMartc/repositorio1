from clases.persona import Persona
from controlador.controlador_persona import add_persona, buscar_persona, obtener_personas

def leerNumero():
  while True:
    try:
      op = int(input())
      return op
    except:
      print('Debe ingresar un número')

def menu():
  print('Menu')
  print('1.- Agregar')
  print('2.- Editar')
  print('3.- Eliminar')
  print('4.- Mostrar uno')
  print('5.- Mostrar Todos')
  print('0.- Salir')
  print('Ingrese una opción:')
  op=leerNumero()
  return op

def agregar_persona():
  nombre = input('Ingrese el nombre: ')
  print('Ingrese el año de nacimiento:')
  anacimiento = leerNumero()
  rut = input('Ingrese el rut: ')
  persona = Persona(nombre, anacimiento, rut)
  add_persona(persona)

def editar_persona():
  rut = input('Ingrese el Rut: ')
  persona = buscar_persona(rut)
  if persona is None:
    print('Persona no encontrada')
    return
  print('Menu editar')
  print('1.- Nombre')
  print('2.- Año nacimiento')
  print('0.- Salir')
  print('Ingrese una opción:')
  op = leerNumero()
  if op == 1:
    print(f'El nombre actual es: {persona.getNombre()}')
    nombre = input('Ingrese el nuevo nombre: ')
    persona.setNombre(nombre)
    print('El nombre fue modificado')
  elif op == 2:
    print(f'El año de nacimiento actual es: {persona.getAnacimiento()}')
    print('Ingrese el nuevo año de nacimiento:')
    anacimiento = leerNumero()
    persona.setAnacimiento(anacimiento)
    print('El año de nacimiento fue modificado')
  else:
    print('No se realizaron cambios.')

def imprimir_todos():
  personas = obtener_personas()
  for persona in personas:
    print(persona)

def main():
  op = 1
  while op != 0:
    op = menu()
    if op == 1:
      agregar_persona()
    elif op == 2:
      editar_persona()
    elif op == 5:
      imprimir_todos()
