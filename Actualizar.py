import tkinter as tk
from colorama import Fore, init
import requests
import os
import sys
import shutil

def ejecutar_modulo(modulo, ID, boton):
    print(Fore.GREEN + "Cargando datos")
    modulo.main(ID)

def main(*args):  # Acepta argumentos aunque no los use
    init()  # Inicializa colorama
    url_exe = 'https://github.com/OneMoreKyra/iniciador/raw/main/Sniper.exe'  # URL del nuevo archivo .exe
    exe_path = os.path.join(os.getcwd(), 'Sniper.exe')  # Ruta del archivo .exe a descargar
    new_exe = os.path.join(os.getcwd(), 'Sniper_Launcher(0.2).exe')  # Nueva ruta del archivo descargado
    temp_exe_path = os.path.join(os.getcwd(), 'temp_Sniper.exe')  # Ruta temporal del archivo descargado
    current_exe = sys.argv[0]  # Ruta del archivo .exe actual en ejecución

    # Verifica si el nuevo archivo ya existe antes de descargar
    if os.path.exists(new_exe):
        print(Fore.RED + "Ya tienes la última versión instalada. No es necesario actualizar.")
        return

    print(Fore.YELLOW + "Descargando el archivo...")
    r = requests.get(url_exe)
    with open(temp_exe_path, 'wb') as f:
        f.write(r.content)
    print(Fore.GREEN + "El archivo ha sido descargado exitosamente.")

    # Mover el archivo temporal a la ubicación final
    shutil.move(temp_exe_path, new_exe)

    print(Fore.CYAN + "Cerrando la versión actual y ejecutando la nueva versión...")

    # Ejecuta el nuevo archivo y cierra el actual
    os.startfile(new_exe)
    sys.exit()

if __name__ == "__main__":
    main()
