import requests
import json
import os

def obtener_grupos(usuario_id):
    url = f"https://groups.roblox.com/v1/users/{usuario_id}/groups/roles"
    response = requests.get(url)
    data = json.loads(response.text)
    grupos = data['data']
    lista_grupos = []
    for grupo in grupos:
        lista_grupos.append(f"{grupo['group']['name']} [ID: {grupo['group']['id']}]")
    return lista_grupos

def guardar_grupos(usuario_id, grupos):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Grupos')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w', encoding='utf-8') as f:
        for grupo in grupos:
            f.write(f"{grupo}\n")

def comparar_grupos(usuario_id, grupos_actuales):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Grupos')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            grupos_anteriores = f.read().splitlines()
    except FileNotFoundError:
        grupos_anteriores = []
    grupos_nuevos = [grupo for grupo in grupos_actuales if grupo not in grupos_anteriores]
    grupos_antiguos = [grupo for grupo in grupos_anteriores if grupo not in grupos_actuales]
    if grupos_nuevos:
        print(f"Grupos nuevos:\n{'\n'.join(grupos_nuevos)}")
    if grupos_antiguos:
        print(f"Grupos que ya no están:\n{'\n'.join(grupos_antiguos)}")

def main(usuario_id):
    grupos_actuales = obtener_grupos(usuario_id)
    comparar_grupos(usuario_id, grupos_actuales)
    guardar_grupos(usuario_id, grupos_actuales)
