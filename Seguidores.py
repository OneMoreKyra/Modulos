import requests
import json
import os
from colorama import Fore, init

# Inicializar colorama
init()

def obtener_seguidores(usuario_id):
    url = f"https://friends.roblox.com/v1/users/{usuario_id}/followers?sortOrder=Desc&limit=100"
    seguidores = []
    while url:
        response = requests.get(url)
        data = json.loads(response.text)
        seguidores.extend(data['data'])
        url = data['nextPageCursor']  # Obtener la siguiente página de resultados
        if url:
            url = f"https://friends.roblox.com/v1/users/{usuario_id}/followers?cursor={url}&sortOrder=Desc&limit=100"
    lista_seguidores = [f"{seguidor['name']} ({seguidor['displayName']}) [ID: {seguidor['id']}]" for seguidor in seguidores]
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

    ids_seguidores_actuales = {seguidor.split('[ID: ')[-1].rstrip(']') for seguidor in seguidores_actuales}
    ids_seguidores_anteriores = {seguidor.split('[ID: ')[-1].rstrip(']') for seguidor in seguidores_anteriores}

    seguidores_nuevos = [seguidor for seguidor in seguidores_actuales if seguidor.split('[ID: ')[-1].rstrip(']') not in ids_seguidores_anteriores]
    seguidores_antiguos = [seguidor for seguidor in seguidores_anteriores if seguidor.split('[ID: ')[-1].rstrip(']') not in ids_seguidores_actuales]
    seguidores_que_ya_estaban = [seguidor for seguidor in seguidores_actuales if seguidor.split('[ID: ')[-1].rstrip(']') in ids_seguidores_anteriores]

    if seguidores_nuevos:
        print(Fore.GREEN + "Seguidores nuevos:")
        for seguidor in seguidores_nuevos:
            print(Fore.GREEN + f"{seguidor}")
    if seguidores_que_ya_estaban:
        print(Fore.YELLOW + "Seguidores que ya estaban:")
        for seguidor in seguidores_que_ya_estaban:
            print(Fore.YELLOW + f"{seguidor}")
    if seguidores_antiguos:
        print(Fore.RED + "Seguidores que ya no están:")
        for seguidor in seguidores_antiguos:
            print(Fore.RED + f"{seguidor}")

    seguidores_a_guardar = seguidores_que_ya_estaban + seguidores_nuevos
    guardar_seguidores(usuario_id, seguidores_a_guardar)

def main(usuario_id):
    seguidores_actuales = obtener_seguidores(usuario_id)
    comparar_seguidores(usuario_id, seguidores_actuales)

# Restablecer colorama
print(Fore.RESET)

# Ejemplo de ejecución del script
# main('ID_DEL_USUARIO_AQUI')
