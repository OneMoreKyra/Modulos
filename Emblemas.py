import requests
import json
import os

def obtener_emblemas(usuario_id):
    url = f"https://badges.roblox.com/v1/users/{usuario_id}/badges?limit=25&sortOrder=Desc"
    response = requests.get(url)
    data = json.loads(response.text)
    emblemas = data['data']
    lista_emblemas = []
    for emblema in emblemas:
        lista_emblemas.append(f"{emblema['name']} [ID: {emblema['id']}]")
    return lista_emblemas

def guardar_emblemas(usuario_id, emblemas):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Emblemas')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w', encoding='utf-8') as f:
        for emblema in emblemas:
            f.write(f"{emblema}\n")

def comparar_emblemas(usuario_id, emblemas_actuales):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Emblemas')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r') as f:
            emblemas_anteriores = f.read().splitlines()
    except FileNotFoundError:
        emblemas_anteriores = []
    emblemas_nuevos = [emblema for emblema in emblemas_actuales if emblema not in emblemas_anteriores]
    emblemas_antiguos = [emblema for emblema in emblemas_anteriores if emblema not in emblemas_actuales]
    if emblemas_nuevos:
        print(f"Emblemas nuevos:\n{'\n'.join(emblemas_nuevos)}")
    if emblemas_antiguos:
        print(f"Emblemas que ya no están:\n{'\n'.join(emblemas_antiguos)}")

def main(usuario_id):
    emblemas_actuales = obtener_emblemas(usuario_id)
    comparar_emblemas(usuario_id, emblemas_actuales)
    guardar_emblemas(usuario_id, emblemas_actuales)
