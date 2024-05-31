import requests
import os
import sys
import shutil
from colorama import Fore, init

def main(*args):  # Acepta argumentos aunque no los use
    init()  # Inicializa colorama
    url_exe = 'https://github.com/OneMoreKyra/iniciador/raw/main/Sniper.exe'  # URL del nuevo archivo .exe
    exe_path = os.path.join(os.getcwd(), 'Sniper.exe')  # Ruta del archivo .exe a descargar
    current_exe = sys.argv[0]  # Ruta del archivo .exe actual en ejecución

    print(Fore.YELLOW + "Descargando el archivo...")
    r = requests.get(url_exe)
    with open(exe_path, 'wb') as f:
        f.write(r.content)
    print(Fore.GREEN + "El archivo ha sido descargado exitosamente.")

    new_exe = os.path.join(os.getcwd(), 'Sniper_0.11.exe')
    os.rename(exe_path, new_exe)

    print(Fore.CYAN + "Cerrando la versión actual y ejecutando la nueva versión...")

    # Ejecuta el nuevo archivo y cierra el actual
    os.startfile(new_exe)
    sys.exit()

if __name__ == "__main__":
    main()
