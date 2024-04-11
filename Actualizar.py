import requests
import os
import sys
from colorama import Fore, init

def main(exe_name):
    init()  # Inicializa colorama
    url_exe = 'https://github.com/OneMoreKyra/iniciador/raw/main/' + exe_name  # URL del nuevo archivo .exe
    r = requests.get(url_exe)
    temp_exe_path = os.path.join(os.getcwd(), 'temp.exe')
    final_exe_path = os.path.join(os.getcwd(), exe_name)  # Nombre del archivo .exe a reemplazar

    print(Fore.YELLOW + "Descargando el archivo...")
    with open(temp_exe_path, 'wb') as f:
        f.write(r.content)
    print(Fore.GREEN + "El archivo ha sido descargado exitosamente.")

    print(Fore.YELLOW + "Reemplazando el archivo existente...")
    if os.path.exists(final_exe_path):  # Verifica si el archivo existe
        os.remove(final_exe_path)  # Elimina el archivo .exe existente
    os.rename(temp_exe_path, final_exe_path)  # Renombra el nuevo archivo .exe
    print(Fore.GREEN + "El archivo '" + exe_name + "' ha sido actualizado exitosamente.")

if __name__ == "__main__":
    if len(sys.argv) > 1:  # Verifica si se proporcionó un argumento
        main(sys.argv[1])  # Usa el primer argumento como el nombre del archivo .exe
    else:
        print(Fore.RED + "Por favor, proporciona el nombre del archivo .exe como un argumento.")
