import requests
import json
import tkinter as tk
from colorama import Fore, init

# Inicializar colorama
init()

def obtener_outfit_details(outfit_id):
    url = f"https://avatar.roblox.com/v1/outfits/{outfit_id}/details"
    response = requests.get(url)
    data = json.loads(response.text)
    if 'errors' in data and data['errors'][0]['message'] == 'Too many requests':
        print(Fore.RED + "Roblox es puto y pone un limite todo ridiculo para utilizar esta api, espera 1 minuto e intentalo de nuevo c:")
        return None
    return data

def imprimir_outfit_details(data):
    if data is None:
        return
    if 'assets' in data:
        print(Fore.GREEN + "Accesorios:")
        for item in data['assets']:
            print(Fore.GREEN + f"{item['name']} (ID: {item['id']})")
    else:
        print(Fore.RED + "No se encontraron accesorios.")
    print(Fore.YELLOW + "Color del cuerpo:")
    for key, value in data['bodyColors'].items():
        print(Fore.YELLOW + f"{key.capitalize()}: {value}")
    print(Fore.BLUE + "Escala:")
    for key, value in data['scale'].items():
        print(Fore.BLUE + f"{key.capitalize()}: {value}")
    print(Fore.CYAN + f"Tipo de avatar: {data['playerAvatarType']}")

def main(usuario_id):
    # Crear una ventana de Tkinter
    window = tk.Tk()
    window.title("Ingrese el ID del outfit")
    tk.Label(window, text="ID del outfit:").pack()
    outfit_id_entry = tk.Entry(window)
    outfit_id_entry.pack()
    tk.Button(window, text="Enviar", command=lambda: window.quit()).pack()
    # Ejecutar la ventana de Tkinter
    window.mainloop()
    # Obtener el ID del outfit del campo de entrada
    outfit_id = outfit_id_entry.get()
    # Cerrar la ventana de Tkinter
    window.destroy()
    # Obtener los detalles del outfit
    outfit_details = obtener_outfit_details(outfit_id)
    # Imprimir los detalles del outfit
    imprimir_outfit_details(outfit_details)

# Restablecer colorama
print(Fore.RESET)

if __name__ == "__main__":
    main()
