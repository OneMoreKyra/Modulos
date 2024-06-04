import requests
import json
import os
from colorama import Fore, init

# Inicializar colorama
init()

def obtener_siguiendo(usuario_id):
    url = f"https://friends.roblox.com/v1/users/{usuario_id}/followings?sortOrder=Desc&limit=100"
    siguiendo = []
    while url:
        response = requests.get(url)
        data = json.loads(response.text)
        siguiendo.extend(data['data'])
        url = data.get('nextPageCursor')  # Obtener la siguiente página de resultados
        if url:
            url = f"https://friends.roblox.com/v1/users/{usuario_id}/followings?cursor={url}&sortOrder=Desc&limit=100"
    lista_siguiendo = [f"{usuario['name']} ({usuario['displayName']}) [ID: {usuario['id']}]" for usuario in siguiendo]
    return lista_siguiendo

def guardar_siguiendo(usuario_id, siguiendo):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Siguiendo')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w') as f:
        for usuario in siguiendo:
            f.write(f"{usuario}\n")

def comparar_siguiendo(usuario_id, siguiendo_actuales):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Siguiendo')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r') as f:
            siguiendo_anteriores = f.read().splitlines()
    except FileNotFoundError:
        siguiendo_anteriores = []

    ids_siguiendo_actuales = {usuario.split('[ID: ')[-1].rstrip(']') for usuario in siguiendo_actuales}
    ids_siguiendo_anteriores = {usuario.split('[ID: ')[-1].rstrip(']') for usuario in siguiendo_anteriores}

    siguiendo_nuevos = [usuario for usuario in siguiendo_actuales if usuario.split('[ID: ')[-1].rstrip(']') not in ids_siguiendo_anteriores]
    siguiendo_antiguos = [usuario for usuario in siguiendo_anteriores if usuario.split('[ID: ')[-1].rstrip(']') not in ids_siguiendo_actuales]
    siguiendo_que_ya_estaban = [usuario for usuario in siguiendo_actuales if usuario.split('[ID: ')[-1].rstrip(']') in ids_siguiendo_anteriores]

    if siguiendo_nuevos:
        print(Fore.GREEN + "Usuarios nuevos seguidos:")
        for usuario in siguiendo_nuevos:
            print(Fore.GREEN + f"{usuario}")
    if siguiendo_que_ya_estaban:
        print(Fore.YELLOW + "Usuarios que ya seguía:")
        for usuario in siguiendo_que_ya_estaban:
            print(Fore.YELLOW + f"{usuario}")
    if siguiendo_antiguos:
        print(Fore.RED + "Usuarios que ya no sigue:")
        for usuario in siguiendo_antiguos:
            print(Fore.RED + f"{usuario}")

    siguiendo_a_guardar = siguiendo_que_ya_estaban + siguiendo_nuevos
    guardar_siguiendo(usuario_id, siguiendo_a_guardar)

def main(usuario_id):
    siguiendo_actuales = obtener_siguiendo(usuario_id)
    comparar_siguiendo(usuario_id, siguiendo_actuales)

# Restablecer colorama
print(Fore.RESET)

# Ejemplo de ejecución del script
# main('ID_DEL_USUARIO_AQUI')
