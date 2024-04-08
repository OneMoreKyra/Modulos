import requests
import json
import os
from colorama import Fore, init

# Inicializar colorama
init()

def obtener_emotes(usuario_id):
    url = f"https://avatar.roblox.com/v1/users/{usuario_id}/avatar"
    response = requests.get(url)
    data = json.loads(response.text)
    emotes = data['emotes']
    lista_emotes = []
    for emote in emotes:
        lista_emotes.append(f"{emote['assetName']} (ID: {emote['assetId']}) [Posicion: {emote['position']}]")
    return lista_emotes

def guardar_emotes(usuario_id, emotes):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Emotes')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w') as f:
        for emote in emotes:
            f.write(f"{emote}\n")

def comparar_emotes(usuario_id, emotes_actuales):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Emotes')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r') as f:
            emotes_anteriores = f.read().splitlines()
    except FileNotFoundError:
        emotes_anteriores = []
    emotes_nuevos = [emote for emote in emotes_actuales if emote not in emotes_anteriores]
    emotes_antiguos = [emote for emote in emotes_anteriores if emote not in emotes_actuales]
    emotes_que_ya_estaban = [emote for emote in emotes_actuales if emote not in emotes_nuevos]
    if emotes_nuevos:
        print(Fore.GREEN + "Emotes nuevos:")
        for emote in emotes_nuevos:
            print(Fore.GREEN + f"{emote}")
    if emotes_que_ya_estaban:
        print(Fore.YELLOW + "Emotes que ya estaban:")
        for emote in emotes_que_ya_estaban:
            print(Fore.YELLOW + f"{emote}")
    if emotes_antiguos:
        print(Fore.RED + "Emotes que ya no están:")
        for emote in emotes_antiguos:
            print(Fore.RED + f"{emote}")
    emotes_a_guardar = emotes_que_ya_estaban + emotes_nuevos
    guardar_emotes(usuario_id, emotes_a_guardar)

def main(usuario_id):
    emotes_actuales = obtener_emotes(usuario_id)
    comparar_emotes(usuario_id, emotes_actuales)

# Restablecer colorama
print(Fore.RESET)
