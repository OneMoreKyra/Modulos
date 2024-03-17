import requests
import json
import os

def obtener_nombre_para_mostrar(usuario_id):
    url = f"https://users.roblox.com/v1/users/{usuario_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['displayName']

def obtener_seguidos(usuario_id):
    url = f"https://friends.roblox.com/v1/users/{usuario_id}/followings"
    response = requests.get(url)
    data = json.loads(response.text)
    seguidos = data['data']
    lista_seguidos = []
    for seguido in seguidos:
        nombre_para_mostrar = obtener_nombre_para_mostrar(seguido['id'])
        lista_seguidos.append(f"{seguido['name']} ({nombre_para_mostrar}) [ID: {seguido['id']}]")
    return lista_seguidos

def guardar_seguidos(usuario_id, seguidos):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Seguidos')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w') as f:
        for seguido in seguidos:
            f.write(f"{seguido}\n")

def comparar_seguidos(usuario_id, seguidos_actuales):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Seguidos')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r') as f:
            seguidos_anteriores = f.read().splitlines()
    except FileNotFoundError:
        seguidos_anteriores = []
    seguidos_nuevos = [seguido for seguido in seguidos_actuales if seguido not in seguidos_anteriores]
    seguidos_antiguos = [seguido for seguido in seguidos_anteriores if seguido not in seguidos_actuales]
    if seguidos_nuevos:
        print(f"Seguidos nuevos:\n{'\n'.join(seguidos_nuevos)}")
    if seguidos_antiguos:
        print(f"Seguidos que ya no están:\n{'\n'.join(seguidos_antiguos)}")
    return [seguido for seguido in seguidos_actuales if seguido not in seguidos_antiguos]

def main(usuario_id):
    seguidos_actuales = obtener_seguidos(usuario_id)
    seguidos_actuales = comparar_seguidos(usuario_id, seguidos_actuales)
    guardar_seguidos(usuario_id, seguidos_actuales)
