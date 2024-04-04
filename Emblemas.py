import requests
import json
import os
from colorama import Fore, init

# Inicializar colorama
init()

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
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            emblemas_anteriores = f.read().splitlines()
    except FileNotFoundError:
        emblemas_anteriores = []
    emblemas_nuevos = [emblema for emblema in emblemas_actuales if emblema not in emblemas_anteriores]
    emblemas_antiguos = [emblema for emblema in emblemas_anteriores if emblema not in emblemas_actuales]
    emblemas_que_ya_estaban = [emblema for emblema in emblemas_actuales if emblema not in emblemas_nuevos]
    if emblemas_nuevos:
        print(Fore.GREEN + "Emblemas nuevos:")
        for emblema in emblemas_nuevos:
            print(Fore.GREEN + f"{emblema}")
    if emblemas_que_ya_estaban:
        print(Fore.YELLOW + "Emblemas que ya estaban:")
        for emblema in emblemas_que_ya_estaban:
            print(Fore.YELLOW + f"{emblema}")
    if emblemas_antiguos:
        print(Fore.RED + "Emblemas que ya no están:")
        for emblema in emblemas_antiguos:
            print(Fore.RED + f"{emblema}")
    emblemas_a_guardar = emblemas_que_ya_estaban + emblemas_nuevos
    guardar_emblemas(usuario_id, emblemas_a_guardar)

def main(usuario_id):
    emblemas_actuales = obtener_emblemas(usuario_id)
    comparar_emblemas(usuario_id, emblemas_actuales)

# Restablecer colorama
print(Fore.RESET)
