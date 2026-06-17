
import os
import random

def generar_caso(n, id_caso, ruta_salida):
   
    MAX_Q_TOTAL = 700  # Suma total de capítulos 
    MAX_M = 3000       # Minutos max
    MAX_E = 500        # Energia max
    
    MAX_T = 300        # Duración capítulo 
    MAX_C = 100        # Costo de energía 
    MAX_V = 10**9      # Satisfacción 
    MAX_B = 10**9      # Bono de completación 

   
    # Inicializamos los n animes con al menos un cap
    q = [1] * n
    
    # Calculamos cuantos capítulos extra podemos repartir como maximo
    max_extra_posible = min(MAX_Q_TOTAL - n, n * 29)
    
    if n <= 8:
        # casos pequeños
        q_objetivo_extra = random.randint(0, min(max_extra_posible, n * 5))
    else:
        # casos medianos y grandes
        q_objetivo_extra = random.randint(0, max_extra_posible)
        
    indices = list(range(n))
    while q_objetivo_extra > 0:
        idx = random.choice(indices)
        if q[idx] < 30:
            q[idx] += 1
            q_objetivo_extra -= 1

    # Definición random de las capacidades máximas (M y E)
    M = random.randint(150, MAX_M)
    E = random.randint(40, MAX_E)

    # simular nombre animes
    prefijos = ["shonen", "seinen", "romcom", "mecha", "slice", "isekai", "fantasy", "sports", "drama", "musical",]
    sufijos = ["quest", "days", "nova", "cafe", "world", "life", "chronicles", "academy", "clash", "drive"]

    lineas = []
    # Primera línea del archivo: n M E
    lineas.append(f"{n} {M} {E}")

    nombres_usados = set()

    for i in range(n):
        # Asegurar un nombre único sin espacios usando letras minúsculas y guiones bajos
        while True:
            nom = f"{random.choice(prefijos)}_{random.choice(sufijos)}_{i+1}"
            if nom not in nombres_usados:
                nombres_usados.add(nom)
                break
        
        q_i = q[i]
        b_i = random.randint(0, MAX_B) 
        lineas.append(f"{nom} {q_i} {b_i}")

        # Generar las especificaciones de cada capítulo
        for j in range(q_i):
            t_ij = random.randint(1, MAX_T)
            c_ij = random.randint(1, MAX_C)
            v_ij = random.randint(1, MAX_V)
            lineas.append(f"{t_ij} {c_ij} {v_ij}")

    # Escribir el archivo final respetando el formato requerido
    nombre_archivo = f"testcases_{n}_{id_caso}.txt"
    ruta_archivo = os.path.join(ruta_salida, nombre_archivo)
    
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas) + "\n")
    
    print(f"  [+] Archivo creado: {nombre_archivo} | Q_total = {sum(q)} capítulos | M = {M} | E = {E}")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_salida = os.path.join(base_dir, "data", "inputs")
    
    os.makedirs(ruta_salida, exist_ok=True)

    print(f"Generando conjunto de casos de prueba en: {ruta_salida}\n")

    # Tamaños 
    casos_pequeños = [3, 5, 8]
    casos_medianos = [20, 40, 80]
    casos_grandes = [100, 150, 200]

  
    instancias_por_n = 5

    print("--- 1. Casos Pequeños (Validación Fuerza Bruta y DP) ---")
    for n in casos_pequeños:
        for i in range(1, instancias_por_n + 1):
            generar_caso(n, i, ruta_salida)

    print("\n--- 2. Casos Medianos (Comparación Greedy vs DP) ---")
    for n in casos_medianos:
        for i in range(1, instancias_por_n + 1):
            generar_caso(n, i, ruta_salida)

    print("\n--- 3. Casos Grandes (Medición de Rendimiento Eficiente) ---")
    for n in casos_grandes:
        for i in range(1, instancias_por_n + 1):
            generar_caso(n, i, ruta_salida)

    print("\n[Éxito] Todos los archivos de prueba válidos han sido generados.")

if __name__ == "__main__":
    main()