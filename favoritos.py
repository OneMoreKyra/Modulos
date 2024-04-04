import requests
import json
import os
from colorama import Fore, init

# Inicializar colorama
init()

def obtener_favoritos(usuario_id, cookie):
    try:
        url = f"https://inventory.roblox.com/v1/users/{usuario_id}/assets/collectibles?sortOrder=Asc&limit=100"
        headers = {'Cookie': '.ROBLOSECURITY=' + cookie}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        favoritos = data['data']
    except Exception as e:
        print(Fore.RED + "El inventario de este usuario es privado, intenta utilizar una cookie con los permisos necesarios.")
        favoritos = []
    lista_favoritos = []
    for favorito in favoritos:
        lista_favoritos.append(f"{favorito['name']} [ID: {favorito['assetId']}]")
    return lista_favoritos

def guardar_favoritos(usuario_id, favoritos):
    directorio = os.path.dirname(__file__)
    ruta_datos = os.path.join(directorio, '..', 'Datos', 'Favoritos')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w', encoding='utf-8') as f:
        for favorito in favoritos:
            f.write(f"{favorito}\\n")

def comparar_favoritos(usuario_id, favoritos_actuales):
    directorio = os.path.dirname(__file__)
    ruta_datos = os.path.join(directorio, '..', 'Datos', 'Favoritos')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            favoritos_anteriores = f.read().splitlines()
    except FileNotFoundError:
        favoritos_anteriores = []
    favoritos_nuevos = [favorito for favorito in favoritos_actuales if favorito not in favoritos_anteriores]
    favoritos_antiguos = [favorito for favorito in favoritos_anteriores if favorito not in favoritos_actuales]
    favoritos_que_ya_estaban = [favorito for favorito in favoritos_actuales if favorito not in favoritos_nuevos]
    if favoritos_nuevos:
        print(Fore.GREEN + "Favoritos nuevos:")
        for favorito in favoritos_nuevos:
            print(Fore.GREEN + f"{favorito}")
    if favoritos_que_ya_estaban:
        print(Fore.YELLOW + "Favoritos que ya estaban:")
        for favorito in favoritos_que_ya_estaban:
            print(Fore.YELLOW + f"{favorito}")
    if favoritos_antiguos:
        print(Fore.RED + "Favoritos que ya no están:")
        for favorito in favoritos_antiguos:
            print(Fore.RED + f"{favorito}")
    favoritos_a_guardar = favoritos_que_ya_estaban + favoritos_nuevos
    guardar_favoritos(usuario_id, favoritos_a_guardar)

def main(usuario_id):
    directorio = os.path.dirname(__file__)
    ruta_datos = os.path.join(directorio, '..', 'Modulos')
    with open(os.path.join(ruta_datos, 'cookie.txt'), 'r') as f:
        cookie = f.read().strip()
    favoritos_actuales = obtener_favoritos(usuario_id, cookie)
    comparar_favoritos(usuario_id, favoritos_actuales)

# Restablecer colorama
print(Fore.RESET)
