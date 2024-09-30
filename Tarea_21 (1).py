# Importar librerías
import requests
import json
import logging
import getpass

# Parámetros
key = 'ec1e2ebed1754f1b8c00f2b90aa15906'
headers = {
    'content-type': 'application/json',
    'api-version': '3',
    'User-Agent': 'python',
    'hibp-api-key': key
}

# API
def main():
    try:
        email = input("Ingrese el correo a investigar: ")
        url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'
        response = requests.get(url, headers=headers)
        response.raise_for_status()

    # Manejo de errores de la solicitud HTTP
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return

    else:
        try:
            data = response.json()
            encontrados = len(data)

            if encontrados > 0:
                print(f"Los sitios en los que se ha filtrado el correo {email} son:")
                for filtracion in data:
                    print(filtracion["Name"])
            else:
                print(f"El correo {email} no ha sido filtrado.")

            # Log del resultado
            msg = f"{email} Filtraciones encontradas: {encontrados}"
            logging.basicConfig(filename='hibpINFO.log',
                                format="%(asctime)s %(message)s",
                                datefmt="%m/%d/%Y %I:%M:%S %p",
                                level=logging.INFO)
            logging.info(msg)

        # Manejo de errores al decodificar JSON
        except json.JSONDecodeError as e:
            print(f"Error al decodificar la respuesta JSON: {e}")
        
        # Manejo de errores por claves no encontradas
        except KeyError as e:
            print(f"Error: no se encontró la clave {e} en la respuesta.")
        
    finally:
        print("Proceso terminado.")

if __name__ == "__main__":
    main()
