# main.py
import os
import subprocess
import requests
from colorama import Fore, init

def main(usuario_id):
    init()  # Inicializa colorama
    updater_exe = 'updater.exe'  # Nombre del archivo .exe del actualizador
    url_updater = 'https://github.com/OneMoreKyra/iniciador/raw/main/Actualizador.exe' + updater_exe  # URL del archivo .exe del actualizador

    print(Fore.YELLOW + "Descargando el módulo de actualización...")
    r = requests.get(url_updater)
    with open(updater_exe, 'wb') as f:
        f.write(r.content)
    print(Fore.GREEN + "El módulo de actualización ha sido descargado exitosamente.")

    print(Fore.YELLOW + "Ejecutando el módulo de actualización...")
    subprocess.Popen([updater_exe, usuario_id])  # Ejecuta updater.exe y pasa el nombre del archivo .exe principal como argumento

if __name__ == "__main__":
    main('Sniper-final')  # Reemplaza 'Sniper-final' con el nombre de tu archivo .exe sin la extensión
