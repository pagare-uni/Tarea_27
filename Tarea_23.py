import pyautogui
import datetime
import subprocess

try:
    # Toma la captura de pantalla
    image = pyautogui.screenshot()
    date = datetime.datetime.now()

    # Genera el nombre de la imagen
    name_image = r'SS_'
    name_image += str(date.strftime('%Y%m%d_%H%M%S'))
    name_image+= '.png'

    # Guarda la captura de pantalla
    try:
        image.save(name_image)
        print(f"Captura guardada como: {name_image}")
    except Exception as e:
        print(f"Error al guardar la captura de pantalla: {e}")

    # Ejecuta el comando 'tasklist' para listar los procesos
    try:
        result = subprocess.run('tasklist', capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando 'tasklist': {e}")
    else:
        # Genera el nombre del archivo de texto
        name_text = r'Procesos_'
        name_text += str(date.strftime('%Y%m%d_%H%M%S'))
        name_text += '.txt'

        # Guarda la salida del comando en un archivo de texto
        try:
            with open(name_text, 'w') as file:
                file.write(result.stdout)
            print(f"Listado de procesos guardado como: {name_text}")
        except Exception as e:
            print(f"Error al guardar el listado de procesos: {e}")

except pyautogui.FailSafeException as e:
    print(f"Error con pyautogui: {e}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
