import requests
import os
from colorama import Fore, init

def main():
    init()  # Inicializa colorama
    url_exe = 'https://github.com/OneMoreKyra/iniciador/raw/main/Sniper.exe'
    r = requests.get(url_exe)
    exe_path = os.path.join(os.getcwd(), 'Sniper.exe')

    print(Fore.YELLOW + "Descargando el archivo 'Sniper.exe'...")
    with open(exe_path, 'wb') as f:
        f.write(r.content)
    print(Fore.GREEN + "El archivo 'Sniper.exe' ha sido actualizado exitosamente.")

if __name__ == "__main__":
    main()
