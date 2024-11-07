from clases.persona import Persona

print('Hola Mundo')

p1 = Persona('Lukas', '1997', '19191919-9')
p2 = Persona('Matías', '1999', '20202020-0')

print(p2)

p2.setNombre('Bryan')

print(p2)

print(p1.getNombre())
