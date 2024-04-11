import requests

def main(usuario_id):
    url_script = 'https://raw.githubusercontent.com/OneMoreKyra/iniciador/main/iniciador.py'
    r = requests.get(url_script)
    with open('Iniciador.py', 'w', encoding='utf-8') as f:
        f.write(r.text)
    print("Actualizado exitosamente.")

if __name__ == "__main__":
    main()
