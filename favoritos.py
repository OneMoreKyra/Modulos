import requests
import json
import os

def obtener_favoritos(usuario_id):
    try:
        url = f"https://inventory.roblox.com/v1/users/{usuario_id}/assets/collectibles?sortOrder=Asc&limit=100"
        response = requests.get(url)
        data = json.loads(response.text)
        favoritos = data['data']
    except Exception as e:
        print("El inventario de este usuario es privado, quizá con una cookie correcta se solucione, pero esto es tema de una próxima actualización.")
        favoritos = []
    lista_favoritos = []
    for favorito in favoritos:
        lista_favoritos.append(f"{favorito['name']} [ID: {favorito['assetId']}]")
    return lista_favoritos

def guardar_favoritos(usuario_id, favoritos):
    directorio = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ruta_datos = os.path.join(directorio, 'Datos', 'Favoritos')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    with open(os.path.join(ruta_datos, f'{usuario_id}.txt'), 'w') as f:
        for favorito in favoritos:
            f.write(f"{favorito}\n")

def main(usuario_id):
    favoritos_actuales = obtener_favoritos(usuario_id)
    guardar_favoritos(usuario_id, favoritos_actuales)
