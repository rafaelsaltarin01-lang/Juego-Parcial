from abc import ABC, abstractmethod
import random

# Clase abstracta para personaje
class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa

    def get_nombre(self): return self.__nombre
    def get_vida(self): return self.__vida
    def set_vida(self, valor): self.__vida = max(0, valor)
    def get_ataque(self): return self.__ataque
    def get_defensa(self): return self.__defensa

    def esta_vivo(self):
        return self.__vida > 0

    @abstractmethod
    def atacar(self, objetivo):
        pass

# Subclases con polimorfismo

class Guerrero(Personaje):
    def atacar(self, objetivo):
        dano = (self.get_ataque() + 5) - objetivo.get_defensa()
        dano = max(0, dano)
        objetivo.set_vida(objetivo.get_vida() - dano)
        print(f"🗡️  {self.get_nombre()} lanza un TAJO MORTAL: -{dano} HP")

class Mago(Personaje):
    def atacar(self, objetivo):
        dano = self.get_ataque() - (objetivo.get_defensa() // 2)
        dano = max(0, dano)
        objetivo.set_vida(objetivo.get_vida() - dano)
        print(f"✨ {self.get_nombre()} lanza una RÁFAGA ARCANA: -{dano} HP")

class Arquero(Personaje):
    def atacar(self, objetivo):
        critico = 2 if random.random() < 0.3 else 1
        dano = (self.get_ataque() * critico) - objetivo.get_defensa()
        dano = max(0, dano)
        objetivo.set_vida(objetivo.get_vida() - dano)
        msg = "¡GOLPE CRÍTICO! 🎯" if critico > 1 else "Flecha certera"
        print(f"🏹 {self.get_nombre()} lanza {msg}: -{dano} HP")

# Clase controladora para la battalla

class Batalla:
    def __init__(self, heroe, enemigo):
        self.heroe = heroe
        self.enemigo = enemigo
        self.turno = 1

    def iniciar(self):
        print(f"\n" + "X" * 45)
        print(f"⚔️  DUELO DE DESTINOS: {self.heroe.get_nombre()} vs {self.enemigo.get_nombre()} ⚔️")
        print("X" * 45)
        
        while self.heroe.esta_vivo() and self.enemigo.esta_vivo():
            input(f"\n>>> [TURNO {self.turno}] Presiona Enter para continuar...")
            
            # El héroe siempre ataca primero
            self.heroe.atacar(self.enemigo)
            
            # El enemigo solo ataca si sigue vivo
            if self.enemigo.esta_vivo():
                self.enemigo.atacar(self.heroe)
            
            print(f"\nESTADO ACTUAL:")
            print(f"   {self.heroe.get_nombre()}: {self.heroe.get_vida()} HP")
            print(f"   {self.enemigo.get_nombre()}: {self.enemigo.get_vida()} HP")
            self.turno += 1
            
        print("\n" + "="*45)
        # Depende que personaje gane , sale un mensaje diferente
        if self.heroe.esta_vivo():
            print(f"✨ ¡LA LUZ HA PREVALECIDO! ✨")
            print(f"Felicidades, {self.heroe.get_nombre().upper()}. Has derrotado a la sombra.")
        else:
            print(f"🌑 ¡LA OSCURIDAD HA PREVALECIDO... 🌑")
            print(f"{self.enemigo.get_nombre()} ha consumido tu luz.")
        print("="*45)

# interfaz y creacion aleatoria

def generar_alter_ego():
    # Elige aleatoriamente una clase para el enemigo
    opciones = [
        ("Guerrero Sombrío", Guerrero, 120, 18, 14),
        ("Mago Tenebroso", Mago, 80, 24, 7),
        ("Arquero Oscuro", Arquero, 95, 21, 9)
    ]
    nombre, clase, vida, atk, df = random.choice(opciones)
    return clase(nombre, vida, atk, df)

def main():
    print("\n" + "🏰 GUARDIANS OF THE ANCIENT KINGDOM 🏰")
    user_name = input("Introduce tu nombre de héroe: ")
    
    print("\n--- SELECCIÓN DE CLASE ---")
    print(f"{'#':<2} | {'CLASE':<10} | {'HP':<4} | {'ATK':<4} | {'DEF':<4} | {'HABILIDAD'}")
    print("-" * 65)
    print(f"1  | Guerrero   | 120  | 20   | 15   | +5 Daño Fijo")
    print(f"2  | Mago       | 80   | 25   | 8    | Ignora 50% Defensa")
    print(f"3  | Arquero    | 95   | 22   | 10   | 30% Prob. Crítico (x2)")
    
    opcion = input("\nElige tu clase (1-3): ")

    if opcion == "1":
        heroe = Guerrero(user_name, 120, 20, 15)
    elif opcion == "2":
        heroe = Mago(user_name, 80, 25, 8)
    else:
        heroe = Arquero(user_name, 95, 22, 10)

    # Creamos el alter ego de forma aleatoria
    enemigo = generar_alter_ego()

    # Iniciamos la batalla
    partida = Batalla(heroe, enemigo)
    partida.iniciar()

if __name__ == "__main__":
    main()