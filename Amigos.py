import requests
import json
import os

def obtener_nombre_para_mostrar(usuario_id):
    url = f"https://users.roblox.com/v1/users/{usuario_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['displayName']

def obtener_amigos(usuario_id):
    url = f"https://friends.roblox.com/v1/users/{usuario_id}/friends"
    response = requests.get(url)
    data = json.loads(response.text)
    amigos = data['data']
    lista_amigos = []
    for amigo in amigos:
        nombre_para_mostrar = obtener_nombre_para_mostrar(amigo['id'])
        lista_amigos.append(f"{amigo['name']} ({nombre_para_mostrar}) [ID: {amigo['id']}]")
    return lista_amigos

def guardar_amigos(usuario_id, amigos):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Amigos')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w') as f:
        for amigo in amigos:
            f.write(f"{amigo}\n")

def comparar_amigos(usuario_id, amigos_actuales):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Amigos')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r') as f:
            amigos_anteriores = f.read().splitlines()
    except FileNotFoundError:
        amigos_anteriores = []
    amigos_nuevos = [amigo for amigo in amigos_actuales if amigo not in amigos_anteriores]
    amigos_antiguos = [amigo for amigo in amigos_anteriores if amigo not in amigos_actuales]
    if amigos_nuevos:
        print(f"Amigos nuevos:\n{'\n'.join(amigos_nuevos)}")
    if amigos_antiguos:
        print(f"Amigos que ya no están:\n{'\n'.join(amigos_antiguos)}")
    return [amigo for amigo in amigos_actuales if amigo not in amigos_antiguos]

def main(usuario_id):
    amigos_actuales = obtener_amigos(usuario_id)
    amigos_actuales = comparar_amigos(usuario_id, amigos_actuales)
    guardar_amigos(usuario_id, amigos_actuales)
