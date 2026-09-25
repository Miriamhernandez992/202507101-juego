import random
import time
# ==========================================
# VARIABLES GLOBALES (Ámbito de variables)
# ==========================================
vidas_globales = 2  
nivel_actual = 1
heroe_stats = {
    "nombre": "JERDAV",
    "tipo": "Héroe guerrero",
    "vida": 100,
    "ataque": 20,
    "defensa": 10,
    "experiencia": 0
}
inventario = ["Espada de hierro", "Poción pequeña"]
misiones_completadas = []
enemigos_derrotados = []
DATOS_ORIGINALES = ("JERDAV", "Guerrero", "Humano")
ENEMIGO_GOBLIN = ("Goblin", 30, 8)  
ENEMIGO_ORCO = ("Orco", 50, 15)
# ==========================================
# NUEVA FUNCIÓN: BIENVENIDA AL JUEGO
# ==========================================
def mostrar_bienvenida():
    """Muestra una pantalla de bienvenida y la introducción de la historia."""
    print("\n" + "="*60)
    print("""
      ¡BIENVENIDO A EL HÉROE DEL REINO! 
    """)
    print("="*60)
    print(f"\n[HISTORIA] El Reino está bajo ataque por fuerzas oscuras.")
    print(f"Un valiente {DATOS_ORIGINALES[1]} {DATOS_ORIGINALES[2]} llamado **{DATOS_ORIGINALES[0]}**")
    print("ha sido elegido para superar 5 niveles plagados de peligros.")
    print("\n[INSTRUCCIONES] Usa los números del teclado para elegir tus acciones.")
    print("Si te quedas sin vidas, el destino del reino colapsará y volverás al inicio.")
    print("="*60)
    time.sleep(2)  # Pausa de 2 segundos para que el usuario pueda leer la bienvenida
# ==========================================
# FUNCIONES SOLICITADAS EN EL DOCUMENTO
# ==========================================
def mostrar_estadisticas():
    """Muestra el estado actual del héroe en la consola."""
    print("\n" + "="*30)
    print(f" STATS DE {heroe_stats['nombre'].upper()} (Nivel {nivel_actual})")
    print(f" Tipo: {DATOS_ORIGINALES[1]} | Raza: {DATOS_ORIGINALES[2]}")
    print(f" Vida: {heroe_stats['vida']} HP")
    print(f" Ataque: {heroe_stats['ataque']} | Defensa: {heroe_stats['defensa']}")
    print(f" Experiencia: {heroe_stats['experiencia']} XP")
    print(f" Inventario: {inventario}")
    print(f" Vidas restantes en la partida: {vidas_globales}")
    print("="*30)
def atacar_enemigo(nombre_enemigo, vida_enemigo, ataque_enemigo):
    """Simula una batalla usando variables locales (daño_temporal)."""
    print(f"\n ¡Un {nombre_enemigo} salvaje ha aparecido!")
    vida_rival = vida_enemigo
    while vida_rival > 0 and heroe_stats["vida"] > 0:
        dano_temporal_heroe = max(5, heroe_stats["ataque"] - random.randint(0, 5))
        vida_rival -= dano_temporal_heroe
        print(f" -> Atacas al {nombre_enemigo} y le haces {dano_temporal_heroe} de daño.")
        if vida_rival <= 0:
            break
        dano_temporal_enemigo = max(2, ataque_enemigo - heroe_stats["defensa"])
        heroe_stats["vida"] -= dano_temporal_enemigo
        print(f" -> El {nombre_enemigo} te contraataca y te quita {dano_temporal_enemigo} de vida.")
        time.sleep(0.5)  # Hace el combate más dinámico y legible
    if heroe_stats["vida"] > 0:
        print(f" ¡Has derrotado al {nombre_enemigo}!")
        enemigos_derrotados.append(nombre_enemigo)
        return True
    else:
        print(f" Has sido derrotado por el {nombre_enemigo}.")
        return False
def curarse():
    """Permite al jugador usar una poción de su lista de inventario."""
    if "Poción pequeña" in inventario:
        inventario.remove("Poción pequeña")
        heroe_stats["vida"] += 20
        print("\n Usaste una Poción pequeña. ¡Recuperas 20 puntos de vida!")
    elif "Poción mediana" in inventario:
        inventario.remove("Poción mediana")
        heroe_stats["vida"] += 50
        print("\n Usaste una Poción mediana. ¡Recuperas 50 puntos de vida!")
    else:
        print("\n No tienes pociones en tu inventario para curarte.")
def ganar_experiencia(cantidad_xp):
    """Suma experiencia al héroe y gestiona las recompensas."""
    print(f" ¡Has ganado {cantidad_xp} XP!")
    heroe_stats["experiencia"] += cantidad_xp
    if cantidad_xp == 150 and nivel_actual == 2:
        print(" Recompensa extra: ¡Encontraste una 'Poción mediana' y 'Espada de plata'!")
        inventario.append("Poción mediana")
        inventario.append("Espada de plata")
        heroe_stats["ataque"] += 20  
def subir_de_nivel(nivel_objetivo):
    """Actualiza las estadísticas globales fijas de cada nivel."""
    global nivel_actual
    nivel_actual = nivel_objetivo 
    if nivel_actual == 1:
        heroe_stats["vida"], heroe_stats["ataque"], heroe_stats["defensa"] = 100, 20, 10
    elif nivel_actual == 2:
        heroe_stats["vida"], heroe_stats["ataque"], heroe_stats["defensa"] = 120, 25, 15
    elif nivel_actual == 3:
        heroe_stats["vida"], heroe_stats["ataque"], heroe_stats["defensa"] = 150, 30, 20
    elif nivel_actual == 4:
        heroe_stats["vida"], heroe_stats["ataque"], heroe_stats["defensa"] = 180, 40, 25
    elif nivel_actual == 5:
        heroe_stats["vida"], heroe_stats["ataque"], heroe_stats["defensa"] = 250, 50, 35
    print(f" ¡Estadísticas actualizadas para el Nivel {nivel_actual}!")
def resetear_juego_completo():
    """Reinicia todo al Nivel 1 si se pierden todas las vidas (Acción del diagrama)."""
    global vidas_globales, nivel_actual
    print("\n" + "!"*50)
    print(" REGRESAR AL NIVEL 1: PERDISTE TODAS LAS VIDAS ")
    print("!"*50)
    vidas_globales = 2
    subir_de_nivel(1)
    heroe_stats["experiencia"] = 0
# ==========================================
# CONTROL DE FLUJO PRINCIPAL (Diagrama)
# ==========================================
def menu_principal():
    """Despliega el menú de inicio con manejo de errores."""
    # LLAMADA A LA BIENVENIDA ANTES DEL MENÚ
    mostrar_bienvenida()
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Jugar")
        print("2. Salir")
        try:
            opcion = int(input("Selecciona una opción (1-2): "))
            if opcion == 1:
                jugar_partida()
            elif opcion == 2:
                print("¡Gracias por jugar! Adiós.")
                break
            else:
                print(" Opción inválida. Elige 1 o 2.")
        except ValueError:
            print(" Error: Por favor, introduce un número válido (no letras).")
def jugar_partida():
    """Ciclo principal que recorre los niveles según el diagrama de flujo."""
    global vidas_globales, nivel_actual
    vidas_globales = 2
    subir_de_nivel(1)
    while nivel_actual <= 5:
        print(f"\n--- INICIANDO NIVEL {nivel_actual} ---")
        if vidas_globales < 1:
            print(" GAME OVER")
            resetear_juego_completo()
            continue    
        mostrar_estadisticas()
        print(f"¿Qué deseas hacer en el Nivel {nivel_actual}?")
        print("1. Avanzar y luchar")
        print("2. Tomar poción de vida")
        try:
            accion = int(input("Opción: "))
        except ValueError:
            print(" Acción inválida, pierdes el turno.")
            accion = 1   
        if accion == 2:
            curarse()
            continue
        if nivel_actual < 3:
            nombre, hp, atk = ENEMIGO_GOBLIN
        else:
            nombre, hp, atk = ENEMIGO_ORCO
        exito = atacar_enemigo(nombre, hp, atk)
        if exito:
            print(f" ¡Completa Nivel {nivel_actual}!")
            misiones_completadas.append(f"Superar Nivel {nivel_actual}")
            ganar_experiencia(150)
            if nivel_actual == 5:
                print("\n ¡FELICIDADES! HAS COMPLETADO EL NIVEL 5 Y SALVADO EL REINO ")
                print("=== FIN DEL JUEGO ===")
                break
            else:
                subir_de_nivel(nivel_actual + 1)
        else:
            vidas_globales -= 1
            print(f" No pasaste el nivel. Perdiste 1 vida. Vidas restantes: {vidas_globales}")
            
            if vidas_globales >= 1:
                print(" Volviendo a intentar el nivel actual...")
                heroe_stats["vida"] = 50 
            else:
                print(" GAME OVER")
                resetear_juego_completo()
if __name__ == "__main__":
    menu_principal()