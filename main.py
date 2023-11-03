import os
import requests
import json

url = "https://www.catastro.gov.py/expediente-electronico/api/public/consultas-publicas/movimiento-expediente"

# Los filtros deben estar en formato JSON
# Define las variables que necesitas
botId = os.environ["BOT_ID"]
chatId = os.environ["CHAT_ID"]
anio = os.environ["ANIO"]
expediente = os.environ["EXPEDIENTE_ID"]

filters = {"anho": anio, "numeroExpediente": expediente}
params = {"filters": json.dumps(filters)}

def enviar_mensaje(telegramMsg):
    # Construye la URL con las variables
    url = f"https://api.telegram.org/bot{botId}/sendMessage?chat_id={chatId}&text={telegramMsg}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        
        # Aquí puedes manejar la respuesta según tus necesidades
        print("Mensaje enviado con éxito.")

    except requests.exceptions.RequestException as e:
        print(f"Error al enviar el mensaje: {e}")

def hacer_solicitud():
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa

        # Si la respuesta es exitosa, puedes acceder a los datos JSON
        data = response.json()
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

def guardar_en_json(data, archivo):
    with open(archivo, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def cargar_desde_json(archivo):
    try:
        with open(archivo, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return None

# Nombre del archivo JSON para guardar los datos
archivo_json = "resultado.json"

# Cargar los datos más recientes desde el archivo JSON
datos_previos = cargar_desde_json(archivo_json)

# Realizar la solicitud y guardar los datos en un archivo JSON
nuevos_datos = hacer_solicitud()
guardar_en_json(nuevos_datos, archivo_json)

if datos_previos:
    # Comparar los datos actuales con los datos anteriores
    if nuevos_datos == datos_previos:
        print("No hay diferencias con la última solicitud.")
    else:
        print("Se encontraron diferencias con la última solicitud.")
        enviar_mensaje("Se encontraron diferencias con la última solicitud. Revisar Catastro.")
else:
    print("No se pudieron cargar datos anteriores. Esta es la primera solicitud.")
