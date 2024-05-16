'''#dichiaro variabile
nome_variabile: int = 10
nome_variabile: float = 10.0
'diffrenza tra Float e Double: Double può rappresentare numeri più grandi (64bit)'
nome_variabile: bool = False

#chiamo una variabile dentro un altra
nome_variabile: int = 10

"se scrivo questo o quello sotto è uguale"
nome_variabile = nome_variabile + 5.5 
nome_variabile += 5.5

print(nome_variabile)

#divisioni

'prende l\'intero più piccolo'
lunghezza_lista: int = 7
punto_di_mezzo: int = 7 // 2 # = 3

'prende l\'intero più grande'
import math
math.ceil(punto_di_mezzo)
print(math.ceil(punto_di_mezzo))

var_1: bool = True
var_2: bool = False

print( var_1 and var_2)#False
print(var_1 or var_2)#True
print(not var_1)#False

#condizione if


'entra nell\'if solo se x è maggiore di 0 e minore di 20'
x: int = 10
if x > 0 or x < 20:
    print(f'{var_1 and var_2}')


'condizione di scambio posizione'
"""x: int = -1000
i: int = 10
lista: list = [1, 2, 5, 3]
if lista[i] > lista[i+1]:
    temp: int = lista[i]
    lista[i] = lista[i+1]
    lista[i+1] = temp"""



a: bool = False
b: bool = False




if a and b:

    print(f'sono nel primo if')

elif a or b: 
    print(f'sono nel primo elif ')

else: 
    print(f'sono nell\' else ')


#condizione for

lista: list = [1, 2, 3, 5, 6] 

for numero in lista:
    print(f'x^2: {numero**2}')

for numero in range(len(lista)):
    print(f'x^2: {lista[numero]**2}')

#ciclo while
contatore : int = 0
while contatore <= len(lista) - 1:

    print(f'x^2: {lista[numero]**2}')
    contatore += 1

class Persona:

    def __init__(self) -> None:
        pass

anagrafe: dict = {
    'persona1': 'Flavio',
    'persona2': 'Marco', 
    'persona3': 'Leonardo'
}

print(anagrafe['persona1'])

anagrafe['persona2'] = 'Bardh'

anagrafe: dict = {
    'persona1': 'Flavio',
    'persona2': 'Marco', 
    'persona3': 'Leonardo'
}

key: str = 'persona100'

if key in anagrafe:
    anagrafe[key].append(voto)

    else:'''
#1
def numbers()-> list:
    num = []
    for i in range(2000, 3001):
        if i % 7 == 0 and i % 5 != 0:
            num.append(i)
    return num
result = numbers()
print(result)

#2
def fact_num()










