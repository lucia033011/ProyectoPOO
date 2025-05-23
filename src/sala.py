#descripcion: clase Sala para representar una sala de reunion

class Sala:
    def __init__(self, id_sala, nombre, capacidad):
        self._id = id_sala  #ID de la sala
        self._nombre = nombre  #nombre de la sala
        self._capacidad = capacidad  #capacidad de la sala

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def capacidad(self):
        return self._capacidad
    @capacidad.setter
    def capacidad(self, nueva_capacidad):
        if isinstance(nueva_capacidad, int) and nueva_capacidad > 0:
            self._capacidad = nueva_capacidad  #solo permite usar numeros positivos
        else:
            print("La capacidad debe ser un número entero positivo.")  #validacion
