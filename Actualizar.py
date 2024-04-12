# main.py
import os
import subprocess
from colorama import Fore, init

def main(usuario_id):
    init()  # Inicializa colorama
    updater_exe = 'updater.exe'  # Nombre del archivo .exe del actualizador

    print(Fore.YELLOW + "Ejecutando el módulo de actualización...")
    subprocess.Popen([updater_exe, usuario_id])  # Ejecuta updater.exe y pasa el nombre del archivo .exe principal como argumento

if __name__ == "__main__":
    main('Sniper-final')  # Reemplaza 'Sniper-final' con el nombre de tu archivo .exe sin la extensión
