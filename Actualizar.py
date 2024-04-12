import requests
import os
from colorama import Fore, init

def main(usuario_id):
    init()  # Inicializa colorama
    url_exe = 'https://github.com/OneMoreKyra/iniciador/raw/main/Sniper.exe'  # URL del nuevo archivo .exe
    exe_path = os.path.join(os.getcwd(), 'Sniper.exe')  # Ruta del archivo .exe a descargar

    print(Fore.YELLOW + "Descargando el archivo...")
    r = requests.get(url_exe)
    with open(exe_path, 'wb') as f:
        f.write(r.content)
    print(Fore.GREEN + "El archivo ha sido descargado exitosamente.")

    print(Fore.CYAN + "Cierra esta versión del sniper y ejecuta la nueva versión la cual se descargó en el mismo directorio que esta versión, puedes borrar esta versión si así lo deseas y quedarte con la nueva únicamente c:")

if __name__ == "__main__":
    main()
