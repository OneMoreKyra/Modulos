import requests
import json
import os
from colorama import Fore, init

init(autoreset=True)

def obtener_informacion_perfil(usuario_id):
    url = f"https://users.roblox.com/v1/users/{usuario_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def guardar_informacion_perfil(usuario_id, info_perfil):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Perfiles')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.json'), 'w') as f:
        json.dump(info_perfil, f)

def comparar_informacion_perfil(usuario_id, info_perfil_actual):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Perfiles')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.json')
    try:
        with open(ruta_archivo, 'r') as f:
            info_perfil_anterior = json.load(f)
    except FileNotFoundError:
        info_perfil_anterior = {}
    cambios = []
    for clave in info_perfil_actual:
        if clave in info_perfil_anterior and info_perfil_actual[clave] != info_perfil_anterior[clave]:
            cambios.append(f"-{clave}, pasó de {info_perfil_anterior[clave]} a {info_perfil_actual[clave]}")
    return cambios

def main(usuario_id):
    info_perfil_actual = obtener_informacion_perfil(usuario_id)
    print(f"El usuario con id {usuario_id} se llama {info_perfil_actual['name']} y su displayName es {info_perfil_actual['displayName']}. Su descripción es {info_perfil_actual['description']}. {'Tiene' if info_perfil_actual['hasVerifiedBadge'] else 'No tiene'} emblema de verificado y {'está baneado' if info_perfil_actual['isBanned'] else 'no está baneado'}.")
    cambios = comparar_informacion_perfil(usuario_id, info_perfil_actual)
    if cambios:
        print(Fore.GREEN + "Los cambios detectados son")
        print(Fore.WHITE + '\n'.join(cambios))
    else:
        print(Fore.RED + "No hay ningún cambio detectado")
    guardar_informacion_perfil(usuario_id, info_perfil_actual)

if __name__ == "__main__":
    main(579559941)  # Reemplaza esto con el ID del usuario que deseas buscar
