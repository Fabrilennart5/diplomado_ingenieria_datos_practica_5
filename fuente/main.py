"""
Este script realiza scraping de datos de un sitio web para obtener información sobre países
y los almacena en una base de datos SQLite.

Requiere la instalación de las bibliotecas 'sqlite3', 'pandas' y 'utils'.

Autor: Fabricio Lennart Flores Ledezma
Fecha: 25 de Abril de 2024
"""

# Importando las bibliotecas necesarias
import sqlite3
import pandas as pd
import utils as ut  # pylint: disable=unused-import

# Esta es la página que vamos a analizar
url = "https://countrycode.org/"

# Ahora llamemos a nuestra función para leer la URL
html_content = ut.get_html_content(url)

# Extraemos la clase de la tabla del contenido HTML
data = ut.extract_table_data(html_content)

# Verificamos si hay contenido en los datos
if data:
    # Extraemos los encabezados y las filas
    headers, rows = data

    # Imprimimos los encabezados y las filas para verlos
    print("Estos son los encabezados:", headers)
    print("\nEste es el contenido:")
    for row in rows:
        print(row)
else:
    print("No se encontraron datos.")

# Creamos un objeto DataFrame

# Transformamos los encabezados en un estilo camel case
headers_lower = [header.replace(" ", "_").lower() for header in headers]

# Creamos el DataFrame
df = pd.DataFrame(rows, columns=headers_lower)

# Conexión a SQLite
conn = sqlite3.connect("D:/Repos/Data/Diplomado/TP5/base_de_datos/prueba.db")

# Creamos la tabla en nuestra base de datos
ut.create_countries_table(conn)

# Insertamos los datos en la tabla y cerramos la conexión
df.to_sql("countries", conn, if_exists="append", index=False)

# Finalizando el proyecto
conn.close()
