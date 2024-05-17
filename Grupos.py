import requests
import json
import os
from colorama import Fore, init

# Inicializar colorama
init()

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

    ids_grupos_actuales = {grupo.split('[ID: ')[-1].rstrip(']') for grupo in grupos_actuales}
    ids_grupos_anteriores = {grupo.split('[ID: ')[-1].rstrip(']') for grupo in grupos_anteriores}

    grupos_nuevos = [grupo for grupo in grupos_actuales if grupo.split('[ID: ')[-1].rstrip(']') not in ids_grupos_anteriores]
    grupos_antiguos = [grupo for grupo in grupos_anteriores if grupo.split('[ID: ')[-1].rstrip(']') not in ids_grupos_actuales]
    grupos_que_ya_estaban = [grupo for grupo in grupos_actuales if grupo.split('[ID: ')[-1].rstrip(']') in ids_grupos_anteriores]

    if grupos_nuevos:
        print(Fore.GREEN + "Grupos nuevos:")
        for grupo in grupos_nuevos:
            print(Fore.GREEN + f"{grupo}")
    if grupos_que_ya_estaban:
        print(Fore.YELLOW + "Grupos que ya estaban:")
        for grupo in grupos_que_ya_estaban:
            print(Fore.YELLOW + f"{grupo}")
    if grupos_antiguos:
        print(Fore.RED + "Grupos que ya no están:")
        for grupo in grupos_antiguos:
            print(Fore.RED + f"{grupo}")

    grupos_a_guardar = grupos_que_ya_estaban + grupos_nuevos
    guardar_grupos(usuario_id, grupos_a_guardar)

def main(usuario_id):
    grupos_actuales = obtener_grupos(usuario_id)
    comparar_grupos(usuario_id, grupos_actuales)

# Restablecer colorama
print(Fore.RESET)

# Ejemplo de ejecución del script
# main('ID_DEL_USUARIO_AQUI')
