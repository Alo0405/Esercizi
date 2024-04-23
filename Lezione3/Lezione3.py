#4-1, 4-11


'''best_pizza: list = ['Salame Piccante', 'Fiori di zucca', 'Focaccia']
for output in best_pizza:
    print("I really love", output)
print(f'My favorite pizza are:{best_pizza[0]}, {best_pizza[1]} and {best_pizza[2]}')
friend_pizzas: list = best_pizza
best_pizza.append('Boscaiola')
print(best_pizza)
friend_pizzas.append('Marinara')
print(friend_pizzas)
for pizza1 in best_pizza:
    print(f'My favorite pizzas are: {pizza1}')
for pizza2 in friend_pizzas:
    print(f"My friend favorite pizza are: {pizza2}")'''

#4-2


'''feline: list =['Lion', 'Tiger', 'cheetah']
for output in feline:
    print(output, "Is very aggressive")
print(f'{feline[0]}, {feline[1]} and {feline[2]} are felin.')'''


#4-3


'''for numbers in range(1, 21):
    print(numbers)'''


#4-4


'''numbers_million: list = (range(1, 1000001))
for read in numbers_million:
    print(read)'''


#4-5


'''numbers_one_to_million: list = [range(1, 1000001)]
print(min(numbers_one_to_million))
print(max(numbers_one_to_million))
print(sum(numbers_one_to_million))'''


#4-6


'''odd_numbers: list = range(1, 21, 2)
for read in odd_numbers:
    print(read)'''


#4-7


'''threes: list = range(3, 31, 3)
for read in threes:
    print(read)'''


#4-8


'''cubes: list = range(1, 11)
for i in cubes:
    print(i ** 3)'''


#4-9, 4-10


'''cube_comprehension: list = [numbers **3 for numbers in range(1, 11)]
for i in cube_comprehension:
    print(i)
print(f'The first three items are {cube_comprehension[0]}, {cube_comprehension[1]}, {cube_comprehension[2]}')
print(cube_comprehension[0:3])
print(f'The middle three items are {cube_comprehension[4]}, {cube_comprehension[5]}, {cube_comprehension[6]}')
print(cube_comprehension[4:7])
print(f'The last three items are {cube_comprehension[7]}, {cube_comprehension[8]}, {cube_comprehension[9]}')
print(cube_comprehension[7:])'''


#5-1

'''x: int = 0
while (x < 10):
    x += 1
    car: str = input('Scrivi una macchina : ')
    if car == 'subaru':
        print("I predict the car is a subaru")
        print(car == 'subaru')
    elif (car == 'maserati'):
        print("I predict the car is a maserati")
        print(car == 'maserati')
    elif (car == 'bmw'):
        print("I predict the car is a bmw")
        print(car == 'bmw')'''

#5-2


'''x: int = 0
while (x < 2):
    x += 1
    var1: str = input('scrivi qualcosa: ')
    var2: str = input('scrivi qualcosa: ')
    var1 = var1.lower()
    print('le variabili sono uguali')
    print((var1 == var2) and (var1 == var2))
    print('le variabil sono diverse')
    print((var1 != var2) and (var1 != var2))

num1: str = input('scrivi un numero: ')
num2: str = input('scrivi un numero: ')
if num1 == num2:
    print('I numeri sono uguali')
elif num1 != num2:
    print('I numeri sono diversi')
if num1 < num2:
    print('num2 è maggiore di num1')
elif num1 > num2:
    print('num1 è maggiore di num2')
a: list = [1, 2]
if ((list[0] != 3) and (list[1] != 3)):
    print('Il 3 non è nella lista.')
    print((list[0] != 3) and (list[1] != 3))
    print('Il 3 è nella lista.')
    print((list[0] == 3) and (list[1] == 3))'''




#5-3, 5-4, 5-5


x: int = 0
while (x < 2):
    x += 1
    alien_color: str = input('scrivi un colore: ')
    if (alien_color == 'green'):
        print('the player just earned 5 points.')
    elif (alien_color == 'red'):
        print('the player do not earned 5 points')
x: int = 0
while (x < 2):
    x +=  1
    alien_color: str = input('scrivi un colore: ')
    if (alien_color == 'green'):
        print('the player just earned 5 points')
    else:
        print('the player just earned 10 points')
x: int = 0
while (x < 3):
    x += 1
    alien_color: str = input('scrivi un colore: ')
    if (alien_color == 'green'):
        print('the player just earned 5 points')
    elif (alien_color == 'yellow'):
        print('the player just earned 10 points')
    elif (alien_color == 'red'):
        print('the player just earned 15 points')


    










