import requests
import os
from colorama import Fore, init

def main(usuario_id):
    init()  # Inicializa colorama
    url_exe = 'https://github.com/OneMoreKyra/iniciador/raw/main/Sniper.exe'  # URL del nuevo archivo .exe
    r = requests.get(url_exe)
    temp_exe_path = os.path.join(os.getcwd(), 'temp.exe')
    final_exe_path = os.path.join(os.getcwd(), usuario_id + '.exe')  # Nombre del archivo .exe a reemplazar

    print(Fore.YELLOW + "Descargando el archivo...")
    with open(temp_exe_path, 'wb') as f:
        f.write(r.content)
    print(Fore.GREEN + "El archivo ha sido descargado exitosamente.")

    print(Fore.YELLOW + "Reemplazando el archivo existente...")
    os.remove(final_exe_path)  # Elimina el archivo .exe existente
    os.rename(temp_exe_path, final_exe_path)  # Renombra el nuevo archivo .exe
    print(Fore.GREEN + "El archivo '" + usuario_id + ".exe' ha sido actualizado exitosamente.")

if __name__ == "__main__":
    main('Sniper')  # Reemplaza 'Sniper-final' con el nombre de tu archivo .exe sin la extensión
