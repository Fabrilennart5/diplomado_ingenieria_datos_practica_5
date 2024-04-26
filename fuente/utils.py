"""" Aquí vamos a crear las funciones necesarias para el proyecto."""

from bs4 import BeautifulSoup
import requests


def get_html_content(url):
    """
    Obtiene el contenido HTML de una URL.

    Parámetros:
        url (str): La URL del sitio web del que se desea obtener el contenido HTML.

    Devuelve:
        str: El contenido HTML de la página si la solicitud es exitosa, None en caso de error.
    """
    # Espera 10 seg antes de considerar la solicitud como fallida
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.text
    else:
        print("Error al recuperar el contenido HTML de la página:", url)
    return None


def extract_table_data(html_content):
    """
    Extrae los datos de una tabla HTML.

    Parámetros:
        html_content (str): El contenido HTML que contiene la tabla.

    Devuelve:
        tuple: Una tupla que contiene una lista de encabezados de columna y una lista de listas
        que representan las filas de la tabla.
    """
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table", class_="table table-hover table-striped main-table")
        if table:
            # Encabezados de columna
            headers = [header.text.strip() for header in table.find_all("th")]

            # Contenido de las filas
            rows = []
            for row in table.find_all("tr"):
                row_data = [data.text.strip() for data in row.find_all("td")]
                if row_data:
                    rows.append(row_data)

            return headers, rows
        else:
            print("Tabla no encontrada en el contenido HTML.")
    else:
        print("Contenido HTML vacío.")


def create_countries_table(conn):
    """
    Crea una tabla en una base de datos SQLite para almacenar datos de países.

    Parámetros:
        conn: La conexión a la base de datos SQLite.

    Devuelve:
        None
    """
    # Crear un cursor
    cursor = conn.cursor()

    # Ejecutar la consulta para crear la tabla
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS countries(
                        country TEXT, 
                        country_code INTEGER, 
                        iso_codes TEXT, 
                        population REAL,
                        area_km2 REAL,
                        gdp_$usd TEXT
                    )"""
    )
    # Imprimir que la tabla fue creada
    print("La tabla se creo exitosamente")
    # Guardar los cambios
    conn.commit()
