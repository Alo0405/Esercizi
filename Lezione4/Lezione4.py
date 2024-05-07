import time
#8-1


'''def display_message():
    print('in this chapter I learn the function')
display_message()'''


#8-2


'''def favorite_book(Title:str):
    print(f'One of my favorite books is {Title}')
favorite_book('Alice in wonderland')'''


#8-3, 8-4


'''def make_shirt(size, message):
    print(f'the size of the t-shirt is {size}, with the message: {message}')
make_shirt('medium', 'I love this shirt')
make_shirt(size = 'large', message = 'this shirt is perfect')

def make_shirt(size = 'large', message = 'I love python'):
     print(f"Making a {size} shirt with the message: '{message}'")
make_shirt()
make_shirt("medium")
make_shirt("small", "My shirt")'''


#8-5


'''def describe_city(city, country='default'):
    print(f'{city} is in {country}')
describe_city('rome', 'italy')
describe_city('paris', 'france')
describe_city('berlin' )'''


#8-6


'''def city_country(city, country):
     return (f'{city.title()}, {country.title()}')
print(city_country('santiago', 'chile'))
print(city_country('Paris', 'France'))
print(city_country('San Paolo', 'Brasile'))'''


#8-7,8-8


'''def make_album(artist_name, album_title, num_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_songs:
        album['num_songs'] = num_songs
    return album
album1 = make_album('gemitaiz', 'qvc4')
album2 = make_album('sfera ebbasta', 'famoso', 17) 
album3 = make_album('Noyz Narcos', 'Cvlt')
print(album1)
print(album2)
print(album3)

while True:
    artist = input("Enter the artist's name (or 'q' to quit): ")
    if artist == 'q':
        break'''


#8-9, 8-10, 8-11


'''message_list: list = ['ciao', 'hello', 'hola']
def show_message(messages):
    for read in messages:
        print(read)
show_message(message_list)'''


#8-12


'''def make_sandwich(*items):
    print("Make your sandwich with this items:")
    for item in items:
        print("- " + item)
make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Swiss Cheese")
make_sandwich("Tuna Salad")'''


#8-13


'''def build_profile(first_name, last_name, age, hair_color, weight):
    profile = f"{first_name} {last_name}, age {age}, hair {hair_color}, weight {weight}"
    return profile
my_profile = build_profile("Valerio", "Rondoni", 19, "brown", "85")
print(my_profile)'''


#8-14


'''def make_car(manufacturer, model, **kwargs):
    car_info = {'manufacturer': manufacturer, 'model': model}
    car_info.update(kwargs)
    return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)'''


#8-15


'''def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:", current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)'''


#8-16







#implementazione bubble sort
'''numbers: list = [i for i in range(0, 10000)]

def bubblesort(numbers: list):
    for i in range(len(numbers)):
        swap_flag: bool = False
        for j in range (len(numbers) - i - 1):
            if(numbers[j] > numbers[j + 1]):
                swap_flag = True
                temp: int = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j+1] = temp
            continue
        if (swap_flag == False):
            return numbers
        continue
    return numbers
start: int = time.time()
numbers1 = bubblesort(numbers)
print(numbers1)
print(time.time() - start)'''

def to_hexadecimal(num):
    if num == 0:
        return "0"

    hex_chars = "0123456789abcdef"
    result = ""

    if num < 0:
        num = (1 << 32) + num

    while num > 0:
        result = hex_chars[num % 16] + result
        num //= 16

    return result












