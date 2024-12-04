
import itertools #proporciona una serie de herramientas y funciones para trabajar con iteradores
import string #proporciona constantes con el alfabeto en mayúsculas y minúsculas, dígitos numéricos y caracteres especiales
import time  # Importar módulo para medir el tiempo
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#hashlib es un módulo de Python que permite cifrar contraseñas y otros datos sensibles.

def fuerza_bruta(password_objetivo, longitud_maxima):
    password_objetivo_hash = hash_password(password_objetivo)
    caracteres = string.ascii_letters + string.digits
    intentos = 0
    inicio = time.time()

    for longitud in range(1, longitud_maxima + 1):
        for combinacion in itertools.product(caracteres, repeat=longitud):
            intentos += 1
            intento = ''.join(combinacion)
            intento_hash = hash_password(intento)
            print(f"Probando: {intento}")
            if intento_hash == password_objetivo_hash:
                fin = time.time()
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