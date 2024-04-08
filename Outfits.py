import requests
import json
import os
from colorama import Fore, init

# Inicializar colorama
init()

def obtener_outfits(usuario_id):
    url = f"https://avatar.roblox.com/v1/users/{usuario_id}/outfits?page=1&itemsPerPage=50&isEditable=true"
    response = requests.get(url)
    data = json.loads(response.text)
    outfits = data['data']
    lista_outfits = []
    for outfit in outfits:
        lista_outfits.append(f"{outfit['name']} (ID: {outfit['id']})")
    return lista_outfits

def guardar_outfits(usuario_id, outfits):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Outfits')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w') as f:
        for outfit in outfits:
            f.write(f"{outfit}\n")

def comparar_outfits(usuario_id, outfits_actuales):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Outfits')
    ruta_archivo = os.path.join(ruta_datos, f'{usuario_id}.txt')
    try:
        with open(ruta_archivo, 'r') as f:
            outfits_anteriores = f.read().splitlines()
    except FileNotFoundError:
        outfits_anteriores = []
    outfits_nuevos = [outfit for outfit in outfits_actuales if outfit not in outfits_anteriores]
    outfits_antiguos = [outfit for outfit in outfits_anteriores if outfit not in outfits_actuales]
    outfits_que_ya_estaban = [outfit for outfit in outfits_actuales if outfit not in outfits_nuevos]
    if outfits_nuevos:
        print(Fore.GREEN + "Outfits nuevos:")
        for outfit in outfits_nuevos:
            print(Fore.GREEN + f"{outfit}")
    if outfits_que_ya_estaban:
        print(Fore.YELLOW + "Outfits que ya estaban:")
        for outfit in outfits_que_ya_estaban:
            print(Fore.YELLOW + f"{outfit}")
    if outfits_antiguos:
        print(Fore.RED + "Outfits que ya no están:")
        for outfit in outfits_antiguos:
            print(Fore.RED + f"{outfit}")
    outfits_a_guardar = outfits_que_ya_estaban + outfits_nuevos
    guardar_outfits(usuario_id, outfits_a_guardar)

def main(usuario_id):
    outfits_actuales = obtener_outfits(usuario_id)
    comparar_outfits(usuario_id, outfits_actuales)

# Restablecer colorama
print(Fore.RESET)
