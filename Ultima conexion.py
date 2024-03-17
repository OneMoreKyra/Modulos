import os
import requests
from datetime import datetime
from pytz import timezone

def obtener_estado_en_linea(usuario_id, roblox_cookie):
    url = "https://presence.roblox.com/v1/presence/users"
    data = {"userIds": [usuario_id]}
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Cookie': f'.ROBLOSECURITY={roblox_cookie}'
    }
    response = requests.post(url, headers=headers, json=data)
    user_presence_info = response.json()['userPresences'][0]
    return user_presence_info

def calcular_tiempo_desde(ultimo_en_linea):
    ahora = datetime.now(timezone('UTC'))
    ultimo_en_linea = datetime.strptime(ultimo_en_linea, "%Y-%m-%dT%H:%M:%S.%fZ")
    ultimo_en_linea = ultimo_en_linea.replace(tzinfo=timezone('UTC'))
    diferencia = ahora - ultimo_en_linea
    minutos = int(diferencia.total_seconds() / 60)
    if minutos < 1:
        return "menos de un minuto"
    elif minutos < 60:
        return f"hace {minutos} minutos"
    horas = minutos // 60
    if horas < 24:
        return f"hace {horas} horas"
    dias = horas // 24
    return f"hace {dias} días"

def main(usuario_id):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cookie_file = os.path.join(dir_path, 'cookie.txt')
    with open(cookie_file, 'r') as f:
        roblox_cookie = f.read().strip()
    user_presence_info = obtener_estado_en_linea(usuario_id, roblox_cookie)
    ultimo_lugar = user_presence_info['lastLocation']
    ultimo_en_linea = user_presence_info['lastOnline']
    tiempo_desde = calcular_tiempo_desde(ultimo_en_linea)
    ultimo_en_linea = datetime.strptime(ultimo_en_linea, "%Y-%m-%dT%H:%M:%S.%fZ")
    ultimo_en_linea = ultimo_en_linea.astimezone(timezone('America/Mexico_City')).strftime("%Y-%m-%d %H:%M:%S")
    print(f"Tipo de presencia: {user_presence_info['userPresenceType']}")
    print(f"Ultima ubicacion: {ultimo_lugar}")
    print(f"ID del juego: {user_presence_info['placeId']}")
    print(f"ID base del juego: {user_presence_info['rootPlaceId']}")
    print(f"ID del servidor: {user_presence_info['gameId']}")
    print(f"ID del universo: {user_presence_info['universeId']}")
    print(f"ID del usuario: {user_presence_info['userId']}")
    print(f"Ultima conexion: {ultimo_en_linea} ({tiempo_desde})")
    if user_presence_info['userPresenceType'] == 2:  # El usuario está en un juego
        print("Para acceder al servidor especifico accede a este juego (https://www.roblox.com/games/16719762525/TP) y coloca las credenciales especificadas")
