#descripcion: clase UsuarioExterno que hereda de Usuario

from usuario import Usuario  #Clase base Usuario
from reserva import Reserva  #Clase Reserva

#Subclase UsuarioExterno con atributo adicional: institucion
class UsuarioExterno(Usuario):
    def __init__(self, id_usuario, nombre, institucion):
        super().__init__(id_usuario, nombre)
        self._institucion = institucion  #nueva propiedad

    #Getter de la institucion
    @property
    def institucion(self):
        return self._institucion

    #Setter de la institucion
    @institucion.setter
    def institucion(self, nueva_institucion):
        self._institucion = nueva_institucion

    #muestra informacion del usuario externo
    def mostrar_informacion(self):
        print(f"Usuario Externo: {self.nombre} (ID: {self.id}) - Institución: {self.institucion}")

    #metodo de reserva con mensaje especial
    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        print(f"{self.nombre} (Externo) requiere validación para reservar.")  #mensaje extra
        return Reserva(4, self, sala, fecha, hora_inicio, hora_fin)
