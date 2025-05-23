#descripcion: clase Reserva que representa una reserva de sala hecha por un usuario

class Reserva:
    def __init__(self, id_reserva, usuario, sala, fecha, hora_inicio, hora_fin):
        self._id = id_reserva            #ID de la reserva
        self._usuario = usuario          #objeto de tipo Usuario
        self._sala = sala                #objeto de tipo Sala
        self._fecha = fecha              #fecha de la reserva
        self._hora_inicio = hora_inicio  #hora de inicio
        self._hora_fin = hora_fin        #hora de finalizacion

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario

    @property
    def sala(self):
        return self._sala
    @sala.setter
    def sala(self, nueva_sala):
        self._sala = nueva_sala

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self, nueva_fecha):
        self._fecha = nueva_fecha

    @property
    def hora_inicio(self):
        return self._hora_inicio
    @hora_inicio.setter
    def hora_inicio(self, nueva_hora_inicio):
        self._hora_inicio = nueva_hora_inicio

    @property
    def hora_fin(self):
        return self._hora_fin
    @hora_fin.setter
    def hora_fin(self, nueva_hora_fin):
        self._hora_fin = nueva_hora_fin

    #muestra de los detalles de la reserva
    def mostrar_detalles(self):
        print(f"\nReserva ID: {self.id}")
        self.usuario.mostrar_informacion()  #llama al metodo polimorfico
        print(f"Sala: {self.sala.nombre} (Capacidad: {self.sala.capacidad})")
        print(f"Fecha: {self.fecha}, Hora: {self.hora_inicio} - {self.hora_fin}")
