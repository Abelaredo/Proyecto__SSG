import itertools
import string
import time
import hashlib
from multiprocessing import Pool, cpu_count

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def comprobar_combinacion(args):
    """Función auxiliar para comprobar combinaciones en paralelo"""
    combinacion, password_objetivo_hash = args
    intento = ''.join(combinacion)
    if hash_password(intento) == password_objetivo_hash:
        return intento
    return None

def fuerza_bruta_mejorada(password_objetivo, longitud_maxima, tiempo_limite):
    password_objetivo_hash = hash_password(password_objetivo)
    caracteres = string.ascii_letters + string.digits
    inicio = time.time()
    intentos = 0
    encontrado = None

    with Pool(processes=cpu_count()) as pool:
        for longitud in range(1, longitud_maxima + 1):
            if encontrado:
                break

            # Generar todas las combinaciones para una longitud dada
            combinaciones = itertools.product(caracteres, repeat=longitud)
            
            # Comprobar las combinaciones en paralelo
            for resultado in pool.imap_unordered(
                comprobar_combinacion, 
                ((combinacion, password_objetivo_hash) for combinacion in combinaciones)
            ):
                intentos += 1

                # Si se encuentra la contraseña
                if resultado:
                    encontrado = resultado
                    break
                
                # Detener si el tiempo límite se supera
                if time.time() - inicio > tiempo_limite:
                    print("\nTiempo límite alcanzado. Deteniendo búsqueda.")
                    break
            
            # Si se supera el tiempo límite, salir del bucle
            if time.time() - inicio > tiempo_limite:
                break

    # Mostrar resultados
    fin = time.time()
    tiempo_total = fin - inicio

    if encontrado:
        print(f"\n¡Contraseña encontrada!: {encontrado}")
        print(f"Número de intentos: {intentos}")
        print(f"Tiempo total: {tiempo_total:.2f} segundos")
    else:
        print("\nNo se encontró la contraseña dentro de los parámetros dados.")
        print(f"Número de intentos: {intentos}")
        print(f"Tiempo total: {tiempo_total:.2f} segundos")

    return encontrado
