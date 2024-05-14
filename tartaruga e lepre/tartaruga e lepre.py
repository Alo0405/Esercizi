import random
import time

def ability_tortuga(ability: int, position_tortuga: int, weather: str):
    if (1<= ability <= 5):
        position_tortuga += 3
    elif (6 <= ability <= 7):
        position_tortuga - 6
    elif (8 <= ability <=10):
        position_tortuga += 1
    else:
        position_tortuga += 1
    if(weather == 'pioggia'):
        position_tortuga -= 0
        if(position_tortuga < 0):
            position_tortuga = 0
    return position_tortuga

        
def ability_hare(ability: int, position_hare: int, weather: str):
    if (1 <= ability <= 2):
        position_hare == 0
    elif (3 <= ability <= 4):
        position_hare += 9
    elif (ability == 5):
        position_hare - 12
    elif (6 <= ability <= 8):
        position_hare += 1
    elif (9 <= ability <= 10):
        position_hare - 2
    
    else:
        position_hare += 1
    if(weather == 'pioggia'):
        position_hare -= 0
        if(position_hare < 0):
            position_hare = 0
    return position_hare

lenght_route = 70
route: list[int] =  ['_'] * lenght_route
position_tortuga: int = 0
position_hare: int = 0
tic = 0
change_w: list = range(0, 1000000, 10)
print('BANG !!!!!')
print('AND THEY\'RE OFF !!!!!')

def positions(route: list):

    print(route)



while (tic != 1000000):
    for i in change_w:
        if(tic == i):
            weather: str = random.choice(['soleggiato', 'pioggia'])
    time.sleep(0.5)
    route[position_tortuga] = '_'
    route[position_hare] = '_'
    ability_t: int = random.randint(1, 10)
    ability_h: int = random.randint(1, 10)
    position_tortuga = ability_tortuga(ability_t, position_tortuga, weather)
    position_hare = ability_hare(ability_h, position_hare, weather)

    if (position_tortuga >= 69):
        print('TORTOISE WINS! || VAY!!!')
        break

    if (position_hare >= 69):
        print('HARE WINS || YUCH!!!')
        break

    if (position_hare >= 69) and (position_tortuga >= 69):
        print('ITS A TIE.')
        break


    if (route[position_tortuga] == '_'):
        route[position_tortuga] = 'T'
    elif(route[position_tortuga] == 'H'):
        print('OUCH!!!')
        route[position_tortuga] = 'TH'

    if (route[position_hare] == '_'):
        route[position_hare] = 'H'
    elif(route[position_hare] == 'T'):
        print('OUCH!!!')
        route[position_hare] = 'TH'
    positions(route)
    tic += 1
    
    


        

    




     
