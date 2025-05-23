#descripcion: clase base abstracta Usuario y subclases Cliente y Administrador
#aplicacion de: encapsulamiento, herencia, polimorfismo

from abc import ABC, abstractmethod  #se usa para definir clases abstractas
from reserva import Reserva  #se importa la clase Reserva para su uso en realizar_reserva

#clase abstracta base que representa a un usuario del sistema
class Usuario(ABC):
    def __init__(self, id_usuario, nombre):
        #se almacena el ID como string, rellenando con ceros a la izquierda para que siempre tenga 10 digitos
        self._id = str(id_usuario).zfill(10)
        self._nombre = nombre  #nombre del usuario

    # Getter para el ID
    @property
    def id(self):
        return self._id  #retorna el ID ya formateado con 10 digitos

    @id.setter
    def id(self, nuevo_id):
        #convierte a string y rellena con ceros para mantener 10 digitos
        self._id = str(nuevo_id).zfill(10)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    #metodo abstracto: cada subclase debe implementar como se muestra la informacion del usuario
    @abstractmethod
    def mostrar_informacion(self):
        pass

    #metodo abstracto: cada subclase define como se realiza una reserva (polimorfismo)
    @abstractmethod
    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        pass

#subclase concreta que representa a un Cliente
class Cliente(Usuario):
    #implementacion del metodo para mostrar la información del cliente
    def mostrar_informacion(self):
        print(f"Cliente: {self.nombre} (ID: {self.id})")

    #implementación del metodo para realizar una reserva
    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        print(f"Reserva realizada por Cliente {self.nombre}.")
        return Reserva(1, self, sala, fecha, hora_inicio, hora_fin)  #se retorna una instancia de Reserva

#subclase concreta que representa a un Administrador
class Administrador(Usuario):
    #implementacion del metodo para mostrar la informacion del administrador
    def mostrar_informacion(self):
        print(f"Administrador: {self.nombre} (ID: {self.id})")
    #implementacion del metodo para realizar una reserva
    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        print(f"Reserva urgente por Administrador {self.nombre}.")
        return Reserva(2, self, sala, fecha, hora_inicio, hora_fin)
