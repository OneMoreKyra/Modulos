import requests
import json
import os
from colorama import Fore, init

# Inicializar colorama
init()

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
    amigos_que_ya_estaban = [amigo for amigo in amigos_actuales if amigo not in amigos_nuevos]
    if amigos_nuevos:
        print(Fore.GREEN + "Amigos nuevos:")
        for amigo in amigos_nuevos:
            print(Fore.GREEN + f"{amigo}")
    if amigos_que_ya_estaban:
        print(Fore.YELLOW + "Amigos que ya estaban:")
        for amigo in amigos_que_ya_estaban:
            print(Fore.YELLOW + f"{amigo}")
    if amigos_antiguos:
        print(Fore.RED + "Amigos que ya no están:")
        for amigo in amigos_antiguos:
            print(Fore.RED + f"{amigo}")
    amigos_a_guardar = amigos_que_ya_estaban + amigos_nuevos
    guardar_amigos(usuario_id, amigos_a_guardar)

def main(usuario_id):
    amigos_actuales = obtener_amigos(usuario_id)
    comparar_amigos(usuario_id, amigos_actuales)

# Restablecer colorama
print(Fore.RESET)
