#descripción: archivo principal de pruebas para el sistema de reservas de salas.
# Miembros del Grupo:
# - Estrella Quiroz Jose
# - Granda Cabrera Suly
# - Jama Lema Gina
# - Loor Toscano Lucia
# - Olaya Villafuerte Ammy

# Funcion para validar horario
# Propósito: Verifica si un rango de horario dado es válido para una reserva,específicamente para usuarios externos, que tienen un horario restringido.
# Solo permite reservas entre 08:00 y 17:00.
# Métodos Principales: horario_valido(hora_inicio_str, hora_fin_str):
# - Transforma las cadenas de texto de las horas a objetos datetime para poder compararlas.
# - Define los límites del horario permitido (08:00 y 17:00).
# - Compara las horas de inicio y fin de la reserva con los límites definidos.

# Clase: Sala
# Propósito: Representa una sala disponible para ser reservada en el sistema.
# Miembros del Grupo: Estrella Quiroz Jose, Granda Cabrera Suly, Jama Lema Gina, Loor Toscano Lucia, Olaya Villafuerte Ammy
# Métodos Principales: __init__(self, numero, nombre, capacidad): Constructor que inicializa los atributos de la sala (número, nombre, capacidad).

# Clase: Usuario
# Propósito: Clase base que representa a un usuario del sistema de reservas.
# Define atributos comunes como ID y nombre.
# Miembros del Grupo: Estrella Quiroz Jose, Granda Cabrera Suly, Jama Lema Gina, Loor Toscano Lucia, Olaya Villafuerte Ammy
# Métodos Principales: __init__(self, id, nombre): Constructor que inicializa el ID y nombre del usuario.
# Métodos Abstractos: mostrar_informacion, realizar_reserva

# Subclase: Cliente (Hereda de Usuario)
# Propósito: Representa a un tipo específico de usuario, un cliente, que puede realizar reservas.
# Miembros del Grupo: Estrella Quiroz Jose, Granda Cabrera Suly, Jama Lema Gina, Loor Toscano Lucia, Olaya Villafuerte Ammy
# Métodos: # Métodos: mostrar_informacion(self):, realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):

# Subclase: Administrador (Hereda de Usuario)
# Propósito: Representa a un usuario con privilegios administrativos, que puede realizar reservas y quizás otras acciones de gestión.
# Miembros del Grupo: Estrella Quiroz Jose, Granda Cabrera Suly, Jama Lema Gina, Loor Toscano Lucia, Olaya Villafuerte Ammy
# Métodos: mostrar_informacion(self):, realizar_reserva(self, sala, fecha, hora_inicio, hora_fin):

# Clase: Usuario_Interno (Hereda de Usuario)
# Propósito: Representa a un usuario que es parte de la organización interna.
# Miembros del Grupo: Estrella Quiroz Jose, Granda Cabrera Suly, Jama Lema Gina, Loor Toscano Lucia, Olaya Villafuerte Ammy
# Métodos Principales: __init__(self, id_usuario, nombre, departamento):
# Métodos Abstractos: mostrar_informacion, realizar_reserva

# Clase: Usuario_Externo (Hereda de Usuario)
# Propósito: Representa a un usuario que no es parte de la organización interna.
# Miembros del Grupo: Estrella Quiroz Jose, Granda Cabrera Suly, Jama Lema Gina, Loor Toscano Lucia, Olaya Villafuerte Ammy
# Métodos Principales: __init__(self, id_usuario, nombre, institucion):
# Métodos Abstractos: mostrar_informacion, realizar_reserva

# Clase: Reserva
# Propósito: Representa una reserva concreta de una sala en una fecha y hora específicas por un usuario.
# Contiene los detalles de la reserva.
# Miembros del Grupo: Estrella Quiroz Jose, Granda Cabrera Suly, Jama Lema Gina, Loor Toscano Lucia, Olaya Villafuerte Ammy
# Métodos Principales: __init__(self, id_reserva, usuario, sala, fecha, hora_inicio, hora_fin):
# Métodos Abstractos: mostrar_detalles.


from sala import Sala
from usuario import Cliente, Administrador
from usuario_interno import UsuarioInterno
from usuario_externo import UsuarioExterno
from datetime import datetime

#Funcion para validar horario
#Solo permite reservas entre 08:00 y 17:00 para usuarios externos
def horario_valido(hora_inicio_str, hora_fin_str):
    formato = "%H:%M"
    hora_inicio = datetime.strptime(hora_inicio_str, formato)
    hora_fin = datetime.strptime(hora_fin_str, formato)
    hora_min = datetime.strptime("08:00", formato)
    hora_max = datetime.strptime("17:00", formato)
    return hora_min <= hora_inicio < hora_max and hora_min < hora_fin <= hora_max

# Crear Sala
sala1 = Sala(101, "Sala Ejecutiva", 12)
sala2= Sala(102, "Sala de conferencias", 80)

# Crear usuarios
cliente = Cliente(148569473, "Carla Rodriguez")
admin = Administrador(895741236, "Javier Solorzano")
interno = UsuarioInterno(878098718, "Sofía Calle", "Recursos Humanos")
externo = UsuarioExterno(248099747, "Pedro Gimenez", "Universidad de Galapagos")

#Prueba 1: Reserva válida del Cliente
print("\n--- Prueba 1: Reserva válida de Cliente ---")
reserva1 = cliente.realizar_reserva(sala1, "23-05-2025", "09:00", "10:00")
reserva1.mostrar_detalles()

#Prueba 2: Reserva válida del Administrador
print("\n--- Prueba 2: Reserva válida de Administrador ---")
reserva2 = admin.realizar_reserva(sala1, "23-05-2025", "11:00", "12:00")
reserva2.mostrar_detalles()

#Prueba 3: Reserva nocturna válida de UsuarioInterno
print("\n--- Prueba 3: Reserva nocturna válida de UsuarioInterno ---")
reserva3 = interno.realizar_reserva(sala2, "23-05-2025", "18:00", "22:00")
reserva3.mostrar_detalles()

#Prueba 4: Reserva inválida del UsuarioExterno (fuera de horario)
print("\n--- Prueba 4: Reserva inválida de UsuarioExterno fuera del horario ---")
hora_inicio_externo = "18:30"
hora_fin_externo = "19:30"

if horario_valido(hora_inicio_externo, hora_fin_externo):
    reserva4 = externo.realizar_reserva(sala1, "23-05-2025", hora_inicio_externo, hora_fin_externo)
    reserva4.mostrar_detalles()
else:
    print(f"No se pudo realizar la reserva para {externo.nombre} (ID: {externo.id}): "
          f"los usuarios externos solo pueden reservar entre 08:00 y 17:00.")
