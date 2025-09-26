import random

ganados = 0
perdidos = 0

entrenador_1 = None
pokemon_1 = None


class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.maximo_ataque = random.randint(20, 100)
        self.vida_maxima = random.randint(150, 400)
        self.vida_actual = self.vida_maxima


def crearEntrenadorPokemon(tipo):
    global entrenador_1, pokemon_1
    
    print("\n" + ("***** Creación de elEntrenador Principal *****" if tipo == 1 else "***** Creación de Entrenador Rival *****"))
        
    nombre_entrenador = input(f"Ingrese el nombre del Entrenador {tipo}: ")
    nombre_pokemon = input(f"Ingrese el nombre del Pokemon {tipo}: ")
    
   
    entrenador_obj = Entrenador(nombre_entrenador)
    pokemon_obj = Pokemon(nombre_pokemon)
    
    if tipo == 1:
        entrenador_1 = entrenador_obj
        pokemon_1 = pokemon_obj
        print(f"\n{pokemon_1.nombre} creado!")
        print(f"Estadísticas: Ataque Máx: {pokemon_1.maximo_ataque}, Vida Máx: {pokemon_1.vida_maxima}")
        
        return entrenador_1, pokemon_1 
    
   
    return entrenador_obj, pokemon_obj 

def valorDeAtaque(pokemon_atacante):
    valor = random.randint(0, pokemon_atacante.maximo_ataque)
    return valor

def defender(pokemon_defensor, valor_ataque_recibido):
   
    defensa = random.randint(1, 6)
    ataque_final = valor_ataque_recibido

    if defensa == 6:
        ataque_final = 0
        print(f"{pokemon_defensor.nombre} defiende con exito, el daño se cancelo")
    else:
        print(f"(Tirada de defensa: {defensa})")
        
    pokemon_defensor.vida_actual = pokemon_defensor.vida_actual - ataque_final
    
    print(f"{pokemon_defensor.nombre} recibe {ataque_final} puntos de daño")
    
    return pokemon_defensor.vida_actual

def recuperar(pokemon_obj):
    
    pokemon_obj.vida_actual = pokemon_obj.vida_maxima
    print(f"\n{pokemon_obj.nombre} ha recuperado su vida al máximo: {pokemon_obj.vida_actual} HP!")



def iniciar_juego():
    global entrenador_1, pokemon_1, ganados, perdidos
    
    crearEntrenadorPokemon(1) 
    
    menu_opcion = ''
    while menu_opcion != 'F':
        print("***** MENÚ PRINCIPAL *****")
        print("Desea Pelear marque(P) o Finalizar el juego marque(F)?")
        menu_opcion = input("Opción: ").upper()
        
        if menu_opcion == 'P':
            recuperar(pokemon_1)
            
            entrenador_2, pokemon_2 = crearEntrenadorPokemon(2)
            
            print(f"\n***** INICIO DE BATALLA *****")
            print(f"¡{entrenador_1.nombre} reta a {entrenador_2.nombre}!")
            print(f"Enfrentamiento: {pokemon_1.nombre} vs {pokemon_2.nombre}")
            print("********************")
            
            turno = 1 
            
           
            while pokemon_1.vida_actual > 0 and pokemon_2.vida_actual > 0:
                print(f"\n***** TURNO {turno} *****")
                
                
                if turno % 2 != 0: 
                    
                    atacante = pokemon_1
                    defensor = pokemon_2
                    entrenador_defensor = entrenador_2
                    
                    print(f"Turno de ataque de: {atacante.nombre} (Entrenador {entrenador_1.nombre})")
                  
                    valor_ataque = valorDeAtaque(atacante)
                    
                   
                    vida_restante = defender(defensor, valor_ataque)
                    
                    print(f"Resumen de {defensor.nombre}: {max(0, vida_restante)} / {defensor.vida_maxima} HP")
                    
                    if vida_restante <= 0:
                        
                        print(f"\nGanaste! El Pokemon {defensor.nombre} de {entrenador_defensor.nombre} ha sido vencido")
                        print(f"el que gano es {entrenador_1.nombre} con su Pokemon {pokemon_1.nombre}!")
                        ganados += 1
                        break

                else: 
                    
                    atacante = pokemon_2
                    defensor = pokemon_1
                    entrenador_defensor = entrenador_1
                    
                    print(f"el turno de ataque de: {atacante.nombre} (Entrenador {entrenador_2.nombre})")

                    
                    valor_ataque = valorDeAtaque(atacante)
                    
                    
                    vida_restante = defender(defensor, valor_ataque)
                    
                    
                    print(f"Resumen de {defensor.nombre}: {max(0, vida_restante)} / {defensor.vida_maxima} HP")
                    
                    if vida_restante <= 0:
                        
                        print(f"\n Perdiste pipipi el Pokemon {defensor.nombre} de {entrenador_defensor.nombre} ha sido vencido")
                        print(f"el que gano es {entrenador_2.nombre} con su Pokemon {pokemon_2.nombre}!")
                        perdidos += 1
                        break
                        
                turno += 1 
            
        elif menu_opcion == 'F':
            
            print("\n" + "="*40)
            print("***** JUEGO TERMINADO *****")
            print(f"Las estadisticas de {pokemon_1.nombre} (Entrenador: {entrenador_1.nombre}):")
            print(f"  Ataque Maximo: {pokemon_1.maximo_ataque}")
            print(f"  Vida Máxima: {pokemon_1.vida_maxima}")
            print(f"  Vida Actual: {pokemon_1.vida_actual} (La vida con la que termino)")
            print("-" * 40)
            print(f"Resumen de los encuentros:")
            print(f"  Encuentros que se gano: {ganados}")
            print(f"  Encuentros que se perdio: {perdidos}")
            print("="*40)
            
        else:
            print("ingrese 'P' para Pelear o 'F' si quieres Finalizar")


if __name__ == "__main__":
    iniciar_juego()