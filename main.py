# from clases.persona import Persona

# # print('Hola Mundo')

# p1 = Persona('Lukas', 1997, '19191919-9')
# p2 = Persona('Matías', 1999, '20202020-0')

# # print(p2)

# p2.setNombre('Bryan')

# # print(p2)

# print(p1)

# p1.setAnacimiento(2000)

# print(p1)

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
menu()