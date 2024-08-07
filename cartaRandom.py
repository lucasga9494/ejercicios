import random



cartas = [
    "1 de Oros", "2 de Oros", "3 de Oros", "4 de Oros", "5 de Oros", "6 de Oros", "7 de Oros",
    "Sota de Oros", "Caballo de Oros", "Rey de Oros",
    "1 de Copas", "2 de Copas", "3 de Copas", "4 de Copas", "5 de Copas", "6 de Copas", "7 de Copas",
    "Sota de Copas", "Caballo de Copas", "Rey de Copas",
    "1 de Espadas", "2 de Espadas", "3 de Espadas", "4 de Espadas", "5 de Espadas", "6 de Espadas", "7 de Espadas",
    "Sota de Espadas", "Caballo de Espadas", "Rey de Espadas",
    "1 de Bastos", "2 de Bastos", "3 de Bastos", "4 de Bastos", "5 de Bastos", "6 de Bastos", "7 de Bastos",
    "Sota de Bastos", "Caballo de Bastos", "Rey de Bastos"
]

print('*********')
print('Culo Sucio: ')
print('*********')

while True:
    cartaRandom=random.choice(cartas)
    cartaRandom2=random.choice(cartas)
    jugador1= int(input('Jugador 1: Toca 1 para agarrar la carta: '))
    if jugador1==1: 
        jugador1=cartaRandom
        print(cartaRandom)
    else: 
        print('Opcion invalida,Perdiste.')
        break
        
    jugador2= int(input('Jugador 2: Toca 1 para agarrar la carta: '))
    if jugador2==1: 
        jugador2=cartaRandom2
        print(cartaRandom2)
    else: 
        print('Opcion invalida,Perdiste.')
        break
        


    if jugador1==cartas[0]:
        print('Perdio el jugador uno')
        break
    if jugador2==cartas[0]:
        print('Perdio el jugador dos')
        break
    
