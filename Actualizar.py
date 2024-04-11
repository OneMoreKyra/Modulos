# main.py
import os
import subprocess
import sys
from colorama import Fore, init

def create_updater(exe_name):
    init()  # Inicializa colorama
    print(Fore.YELLOW + "Creando el módulo externo...")
    with open('updater.py', 'w') as f:
        f.write(f"""
import os
import time
import requests
from colorama import Fore, init

def main():
    init()  # Inicializa colorama
    url_exe = 'https://github.com/OneMoreKyra/iniciador/raw/main/' + '{exe_name}'  # URL del nuevo archivo .exe
    temp_exe_path = os.path.join(os.getcwd(), 'temp.exe')
    final_exe_path = os.path.join(os.getcwd(), '{exe_name}')  # Nombre del archivo .exe a reemplazar

    print(Fore.YELLOW + "Cerrando el proceso existente...")
    os.system('taskkill /f /im ' + '{exe_name}')  # Cierra el proceso existente

    print(Fore.YELLOW + "Descargando el archivo...")
    r = requests.get(url_exe)
    with open(temp_exe_path, 'wb') as f:
        f.write(r.content)
    print(Fore.GREEN + "El archivo ha sido descargado exitosamente.")

    print(Fore.YELLOW + "Reemplazando el archivo existente...")
    os.rename(temp_exe_path, final_exe_path)  # Renombra el nuevo archivo .exe
    print(Fore.GREEN + "El archivo '" + '{exe_name}' + "' ha sido actualizado exitosamente.")

if __name__ == "__main__":
    main()
""")
    print(Fore.GREEN + "El módulo externo ha sido creado exitosamente.")

def main(usuario_id):
    exe_name = usuario_id + '.exe'
    create_updater(exe_name)
    print(Fore.YELLOW + "Ejecutando el módulo externo...")
    subprocess.Popen(['python', 'updater.py'])  # Ejecuta updater.py
    sys.exit()  # Cierra el script principal

if __name__ == "__main__":
    main('Sniper-final')  # Reemplaza 'Sniper-final' con el nombre de tu archivo .exe sin la extensión
