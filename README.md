---

# 💜 PROYECTO PRIMER PARCIAL - PROGRAMACIÓN ORIENTADA A OBJETOS 💜  

## 📖 *Índice*  
1. [Objetivo del Proyecto](#objetivo-del-proyecto)  
2. [Estructura del Proyecto](#estructura-del-proyecto)  
3. [Restricciones de Horario](#restricciones-de-horario)  
4. [Tabla de Permisos por Usuario](#tabla-de-permisos-por-usuario)  
5. [Explicación de Resultados de Pruebas](#explicación-de-resultados-de-pruebas)  
6. [Ejemplo de Uso](#ejemplo-de-uso)  
7. [Equipo de Desarrollo](#equipo-de-desarrollo)  

---

## 🌸 *Sistema de Reservas de Salas – Proyecto* 💜  
Este proyecto, desarrollado por un *equipo extraordinario, implementa un sistema de reservas de salas mediante **Programación Orientada a Objetos (POO)*. Buscamos ofrecer una solución estructurada, escalable y eficiente, resaltando la capacidad de las estudiantes en la tecnología. 👩‍💻🚀  

---

## 📌 *Objetivo del Proyecto*  
Este sistema permite a distintos tipos de usuarios reservar salas con ciertas restricciones dependiendo de su categoría. El código sigue *principios de modularidad y reutilización*, lo que facilita su mantenimiento y expansión.  

---

## 📂 *Estructura del Proyecto* 🏗  
El código sigue una *arquitectura modular*, con los archivos principales agrupados dentro de la carpeta /src/, asegurando un diseño claro y escalable.  

📂 *src/* (Carpeta principal con las clases y módulos)  
- 📄 *main.py* – Archivo principal con pruebas de reserva y validación de usuarios.  
- 🏠 *src/sala.py* – Define la clase Sala, representando los espacios disponibles.  
- 👤 *src/usuario.py* – Contiene la clase base Usuario y sus subclases (Cliente, Administrador).  
- 🏢 *src/usuario_interno.py* – Implementa UsuarioInterno, con permisos extendidos de reserva.  
- 🌍 *src/usuario_externo.py* – Implementa UsuarioExterno, con restricciones de horario.  
- 📅 *src/reserva.py* – Define la clase Reserva, que gestiona la asignación de salas.  
- 🛠 *src/utils.py* – Funciones auxiliares, como validación de horarios.  

---

## 📸 *Captura del Proyecto* 💝  
![Ejecución del programa](https://github.com/user-attachments/assets/37123a2a-1571-42f9-a42d-aa20f4350261)  

---

## 🛠 *Tecnologías Utilizadas*  
- 🐍 *Lenguaje*: Python  
- 📏 *Paradigma*: Programación Orientada a Objetos  
- ⏳ *Librerías*: datetime para manejo de horarios y reservas  

---

## 🚀 *Instalación y Uso*  
1. 🔗 Clona este repositorio con:  
   bash
   git clone <[URL_DEL_REPOSITORIO](https://github.com/lucia033011/Proyecto.git)>
     
2. 🛠 Asegúrate de tener Pycharm instalado.  
3. ▶ Ejecuta main.py para probar la funcionalidad.  
   bash
   python main.py
     

---

## ⏰ *Restricciones de Horario*  
Para garantizar la disponibilidad y orden en el sistema:  
✔ *Usuarios externos* solo pueden reservar entre *08:00 y 17:00*.  
✔ *Usuarios internos* pueden reservar fuera de ese horario.  

---

## 🔗 *Tabla de Permisos por Usuario*  

Para mayor claridad, aquí tienes un resumen de los permisos de cada tipo de usuario:  

| Usuario | Puede reservar | Horario permitido | Privilegios adicionales |
|---------|---------------|-------------------|-------------------------|
| Cliente | ✅ Sí | 08:00 - 17:00 | Ninguno |
| UsuarioInterno | ✅ Sí | Sin restricciones | Más flexibilidad de reserva |
| UsuarioExterno | ✅ Sí | 08:00 - 17:00 | Restricciones de horarios |
| Administrador | ✅ Sí | Sin restricciones | Gestión de usuarios y reservas |

---

## 🔍 *Explicación de Resultados de Pruebas*  

Cada prueba sigue las reglas de reserva establecidas en el sistema. A continuación, explicamos *por qué se generaron estos resultados*:  

1. *Prueba 1 - Reserva exitosa para un Cliente:*  
   - *Usuario:* Cliente estándar.  
   - *Solicitud:* Reservar una sala en horario permitido.  
   - *Validaciones:*  
     ✅ El usuario es de tipo Cliente.  
     ✅ La sala está disponible en el horario solicitado.  
     ✅ La reserva se registra correctamente en el sistema.  
   - *Resultado:* La reserva se confirma con éxito.  

2. *Prueba 2 - Reserva denegada por capacidad insuficiente:*  
   - *Usuario:* Cliente.  
   - *Solicitud:* Reservar una sala con una capacidad menor al número de asistentes.  
   - *Validaciones:*  
     ❌ La capacidad de la sala es insuficiente para la reserva.  
   - *Resultado:* El sistema rechaza la solicitud y muestra un mensaje indicando que la sala no tiene suficiente espacio.  

3. *Prueba 3 - Error por intento de reserva en una fecha inválida:*  
   - *Usuario:* Administrador.  
   - *Solicitud:* Reservar una sala en una fecha no válida (por ejemplo, un formato incorrecto o una fecha fuera del rango permitido).  
   - *Validaciones:*  
     ❌ El formato de la fecha es incorrecto.  
     ❌ La fecha solicitada no es válida para reservas.  
   - *Resultado:* Se muestra un error indicando que el formato de la fecha es incorrecto o que la reserva está fuera del rango permitido.  

4. *Prueba 4 - Reserva fallida para un Usuario Externo fuera del horario permitido:*  
   - *Usuario:* UsuarioExterno.  
   - *Solicitud:* Reservar una sala fuera del horario permitido (por ejemplo, 18:00).  
   - *Validaciones:*  
     ❌ Los usuarios externos solo pueden reservar entre 08:00 y 17:00.  
   - *Resultado:* El sistema rechaza la reserva y muestra un mensaje informando que el usuario externo solo puede reservar dentro del horario permitido.  

---

## ✨ *Ejemplo de Uso*  
python
sala1 = Sala(101, "Sala Ejecutiva", 12)
cliente = Cliente(148569473, "Carla Rodriguez")
reserva = cliente.realizar_reserva(sala1, "23-05-2025", "09:00", "10:00")
reserva.mostrar_detalles()
  

---

## 💜 *Equipo de Desarrollo* 👩‍💻  
Este proyecto ha sido creado por un grupo de jóvenes apasionadas por la tecnología:  

- 🌟 Estrella Quiroz Jose  
- 🚀 Granda Cabrera Suly  
- 💡 Jama Lema Gina  
- 🎯 Loor Toscano Lucia  
- 🔥 Olaya Villafuerte Ammy  

---