import tkinter as tk
from tkinter import messagebox
import requests

def obtener_universeid(id_juego):
    url = f"https://apis.roblox.com/universes/v1/places/{id_juego}/universe"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['universeId']
    else:
        return None

def main(ID):
    def submit():
        id_juego = entry.get()
        universeid = obtener_universeid(id_juego)
        if universeid is not None:
            print(f"El UniverseID para el juego con ID {id_juego} es {universeid}")
        else:
            print("No se pudo obtener el UniverseID. Por favor, verifica el ID del juego.")
        root.destroy()

    root = tk.Tk()
    tk.Label(root, text="Introduce el ID del juego de Roblox:").pack()
    entry = tk.Entry(root)
    entry.pack()
    tk.Button(root, text="Enviar", command=submit).pack()
    root.mainloop()

if __name__ == "__main__":
    main()
