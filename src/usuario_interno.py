#descripcion: clase UsuarioInterno que hereda de Usuario

from usuario import Usuario  #Importamos la clase base Usuario
from reserva import Reserva  #Importamos la clase Reserva

#subclase UsuarioInterno con atributo adicional: departamento
class UsuarioInterno(Usuario):
    def __init__(self, id_usuario, nombre, departamento):
        super().__init__(id_usuario, nombre)
        self._departamento = departamento  #atributo adicional

    #Getter del departamento
    @property
    def departamento(self):
        return self._departamento

    #Setter del departamento
    @departamento.setter
    def departamento(self, nuevo_departamento):
        self._departamento = nuevo_departamento

    #implementación del metodo abstracto para mostrar informacion
    def mostrar_informacion(self):
        print(f"Usuario Interno: {self.nombre} (ID: {self.id}) - Departamento: {self.departamento}")

    #implementacion del metodo polimorfico de reserva
    def realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):
        print(f"{self.nombre} (Interno) ha reservado la sala {sala.nombre}.")  #confirmación
        return Reserva(3, self, sala, fecha, hora_inicio, hora_fin)  #retorna reserva
