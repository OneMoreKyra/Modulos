import requests
import json
import os

def obtener_nombre_para_mostrar(usuario_id):
    url = f"https://users.roblox.com/v1/users/{usuario_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['displayName']

def obtener_seguidores(usuario_id):
    url = f"https://friends.roblox.com/v1/users/{usuario_id}/followers"
    response = requests.get(url)
    data = json.loads(response.text)
    seguidores = data['data']
    lista_seguidores = []
    for seguidor in seguidores:
        nombre_para_mostrar = obtener_nombre_para_mostrar(seguidor['id'])
        lista_seguidores.append(f"{seguidor['name']} ({nombre_para_mostrar}) [ID: {seguidor['id']}]")
    return lista_seguidores

def guardar_seguidores(usuario_id, seguidores):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Seguidores')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w') as f:
        for seguidor in seguidores:
            f.write(f"{seguidor}\n")

def comparar_seguidores(usuario_id, seguidores_actuales):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Seguidores')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r') as f:
            seguidores_anteriores = f.read().splitlines()
    except FileNotFoundError:
        seguidores_anteriores = []
    seguidores_nuevos = [seguidor for seguidor in seguidores_actuales if seguidor not in seguidores_anteriores]
    if seguidores_nuevos:
        print(f"Seguidores nuevos:\n{'\n'.join(seguidores_nuevos)}")
    return seguidores_nuevos

def main(usuario_id):
    seguidores_actuales = obtener_seguidores(usuario_id)
    seguidores_nuevos = comparar_seguidores(usuario_id, seguidores_actuales)
    guardar_seguidores(usuario_id, seguidores_nuevos)
