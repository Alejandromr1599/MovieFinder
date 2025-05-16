# 🎬 MovieFinder– Explorador de Películas con JSON

> Aplicación interactiva en Python para consultar una base de datos de películas a partir de un archivo JSON. Ideal para prácticas de estructuras de datos, lectura de archivos y menús interactivos.

---

## 📌 Descripción

**MovieFinder** es una aplicación de consola que permite buscar, listar y contar películas almacenadas en un archivo `peliculas.json`. Este proyecto está diseñado con fines educativos para trabajar con datos estructurados en formato JSON, aplicando buenas prácticas de desarrollo en Python.

---
## 🧾 Estructura del JSON

Cada película está representada con los siguientes campos:

``json
{
  "titulo": "Nombre de la película",
  "poster": "Ruta al póster de la película (opcional)",
  "director": ["Nombre del director"],
  "precio": Número (precio estimado o ficticio),
  "categoria": ["Género1", "Género2", ...],
  "anno": Año de estreno,
  "desc": "Descripción breve de la película",
  "actores": [
    {
      "nombre": "Nombre del actor",
      "personaje": "Personaje interpretado"
    }
  ]
}

---

🔍 Funcionalidades del menú
🎞️ Listar todos los títulos de películas

🎬 Contar cuántas películas ha dirigido cada 

📅 Buscar películas entre un rango de 

🎭 Buscar películas por nombre de 

📂 Contar películas por cada género o categoría

🚪 Salir del programa

---

▶️ Ejecución del programa
Requisitos
Python 3.7 o superior

Archivo peliculas.json válido en la misma carpeta que el script

---

🛠 Tecnologías aplicadas

📄 Lectura y escritura con JSON en Python

🔁 Bucles y condicionales

🗂️ Estructuras de datos: listas y diccionarios

📚 Gestión de errores con try-except

🧠 Programación modular con funciones


👨‍💻 Autor
Desarrollado por Alejandro Medina Ramirez
Técnico en Sistemas Microinformáticos y Redes
Estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM)

📜 Licencia
Este proyecto se distribuye bajo la Licencia MIT.
Uso libre para fines educativos y personales.


