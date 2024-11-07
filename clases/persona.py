class Persona:
  def __init__(self, nombre, anacimiento, rut ):
    self.__nombre = nombre
    self.__anacimiento = anacimiento
    self.__rut = rut

  def getNombre(self):
    return self.__nombre
  
  def setNombre(self, nombre):
    self.__nombre = nombre

  def __str__(self):
    return f'Nombre: {self.__nombre}\nAño de nacimiento: {self.__anacimiento}\nRun: {self.__rut}'