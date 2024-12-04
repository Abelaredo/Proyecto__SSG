import itertools #proporciona una serie de herramientas y funciones para trabajar con iteradores
import string #proporciona constantes con el alfabeto en mayúsculas y minúsculas, dígitos numéricos y caracteres especiales
import time  # Importar módulo para medir el tiempo

def fuerza_bruta(password_objetivo, longitud_maxima):
    caracteres = string.ascii_letters + string.digits  # Letras y números
    intentos = 0
    inicio = time.time()  # Registrar el tiempo de inicio

    for longitud in range(1, longitud_maxima + 1):
        # Generar todas las combinaciones posibles de la longitud actual
        for combinacion in itertools.product(caracteres, repeat=longitud):
            intentos += 1
            intento = ''.join(combinacion)
            print(f"Probando: {intento}")  # Para observar los intentos
            if intento == password_objetivo:
                fin = time.time()  # Registrar el tiempo de finalización
                tiempo_total = fin - inicio
                print(f"\n¡Contraseña encontrada!: {intento}")
                print(f"Número de intentos: {intentos}")
                print(f"Tiempo total: {tiempo_total:.2f} segundos")
                return intento

    fin = time.time()
    tiempo_total = fin - inicio
    print("\nNo se encontró la contraseña dentro de los parámetros dados.")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    return None

# Ejemplo de uso
password_objetivo = "abc"  # Contraseña que quieres encontrar
longitud_maxima = 3           # Longitud máxima de las contraseñas a probar

fuerza_bruta(password_objetivo, longitud_maxima)

# Nota: Este enfoque es extremadamente lento y no es práctico para contraseñas reales.
# Se recomienda utilizar métodos más avanzados y seguros para la gestión de contraseñas.
# Este script es solo un ejemplo didáctico para comprender el concepto de fuerza bruta.