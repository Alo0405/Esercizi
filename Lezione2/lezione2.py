#Valerio Rondoni
#17/04/2024

#print ("hello world")

#2-3. Personal Message: Use a variable to represent a person’s name, and print
#a message to that person. Your message should be simple, such 
#as, “Hello Eric, would you like to learn some Python today?”'''


'''name = 'Mario'
message: str = f'ciao {name}, ti va imparare un pò di python insieme'
print(message)'''


#2-4. Name Cases: Use a variable to represent
#a person’s name, and then print
#that person’s name in lowercase, uppercase, and title case.'


'''name: str = 'Valerio'
name_lower: str = name.lower()
print(name_lower)
name_upper: str = name.upper()
print(name_upper)
name_title: str = name.title()
print(name_title)'''


#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote
#and the name of its author. Your output
#should look something like the following, including the quotation marks: Albert Einstein
#once said, “A person who never
#made a mistake never tried anything new.”


'print(Albert Einstein once said: “A person who never made a mistake never tried anything new.”)'


#2-6

'''famous_person: str = 'Albert Einstein'
print(f'{famous_person} once said: “A person who never made a mistake never tried anything new.”')'''


#2-8


'''filename: str = 'python_notes.txt'
print('python_notes.txt'.removesuffix('.txt'))'''


#3-1


'''amici_list: list = ['Federico', 'Leonardo', 'Giulio', 'Bruno']
print(amici_list[0])
print(amici_list[1])
print(amici_list[2])
print(amici_list[3])'''


#3-2


'''amici_list: list = ['Federico', 'Leonardo', 'Giulio', 'Bruno']
message: str ='ciao valerio'
print(f'{amici_list[0]} ha detto {message}')
print(f'{amici_list[1]} ha detto {message}')
print(f'{amici_list[2]} ha detto {message}')
print(f'{amici_list[3]} ha detto {message}')'''


#3-3


'''transport_list: list = ['Lamborghini', 'Ferrari', 'Maserati']
print(f'I would like to own a {transport_list[0]}')
print(f'I would like to own a {transport_list[1]}')
print(f'I would like to own a {transport_list[2]}')'''


#3-4, 3-5, 3-6, 3-9


'''invite_list: list = ['Federico', 'Leonardo', 'Giulio']
#print(f'{invite_list[0]} vuoi venire a cena?')
#print(f'{invite_list[1]} vuoi venire a cena?')
#print(f'{invite_list[2]} vuoi venire a cena?')

#print(f'{invite_list[0]} non puo venire')
invite_list.pop(0)

#print(f'{invite_list[0]} vuoi venire a cena?')
#print(f'{invite_list[1]} vuoi venire a cena?')

#print(f'{invite_list[0]} i found a big table')
#print(f'{invite_list[1]} i found a big table')
invite_list.insert(0, 'Francesco')
invite_list.insert(2, 'Lorenzo')
invite_list.append('Giovanni')
#print(invite_list)

#print(f'{invite_list[0]} vuoi venire a cena?')
#print(f'{invite_list[1]} vuoi venire a cena?')
#print(f'{invite_list[2]} vuoi venire a cena?')
#print(f'{invite_list[3]} vuoi venire a cena?')
#print(f'{invite_list[4]} vuoi venire a cena?')

print(f'{invite_list[0]} posso invitare solo 2 persone')
print(f'{invite_list[1]} posso invitare solo 2 persone')
print(f'{invite_list[2]} posso invitare solo 2 persone')
print(f'{invite_list[3]} posso invitare solo 2 persone')
print(f'{invite_list[4]} posso invitare solo 2 persone')

invite_list.pop(0)
print(f'{invite_list[0]} sorry but i can not invite you at dinner')
invite_list.pop(0)
print(f'{invite_list[0]} sorry but i can not invite you at dinner')
invite_list.pop(0)
print(f'{invite_list[0]} sorry but i can not invite you at dinner')

print(f'{invite_list[0]} you are still invited')
print(f'{invite_list[1]} you are still invited')

invite_list.__delitem__(0)
invite_list.__delitem__(0)

print(invite_list)

print(len(invite_list))


#3-8


travel_list: list = ['Giappone', 'Cina', 'America', 'Canada', 'Spagna']
print(travel_list)
travel_list_sa: list = sorted(travel_list)
print(travel_list_sa)
travel_list_rev: list = sorted(travel_list, reverse = True)
print(travel_list_rev)
travel_list.reverse()
print(travel_list)
travel_list_rev.reverse()
print(travel_list_rev)
travel_list.sort()
print(travel_list)
travel_list.sort(reverse = True)
print(travel_list)'''


#3.10


random_list: list = ['mountains', 'rivers', 'countries', 'cities', 'languages']
print(random_list)
random_list.insert(0, 'mouse')
print(random_list)
random_list.append('lion')
print(random_list)
random_list.pop(0)
print(random_list)
random_list.__delitem__(0)
print(random_list)
random_list = sorted(random_list)
print(random_list)
random_list = sorted(random_list, reverse = True)
print(random_list)
random_list.sort()
print(random_list)


#6-1


person: dict = {'first_name': 'Valerio', 'last_name': 'Rondoni', 'age': '19', 'city': 'Rome' }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])



#6-2, 6-10
fav_numbers: dict = {'Valerio': 16, 'Filippo': 2, 'Giulio': 7, 'Simone': 15, 'Marco': 99}
print('Valerio:', fav_numbers['Valerio'])
print('Filippo:', fav_numbers['Filippo'])
print('Giulio:', fav_numbers['Giulio'])
print('Simone:', fav_numbers['Simone'])
print('Marco:', fav_numbers['Marco'])

fav_numbers['Valerio'] = [16, 67]
fav_numbers['Filippo'] = [2, 11]
fav_numbers['Giulio'] = [7, 19]
fav_numbers['Simone'] = [15, 5]
fav_numbers['Marco'] = [99, 90]
print('VAlerio:', fav_numbers['Valerio'][0], ',', fav_numbers['Valerio'][1])
print('Filippo:', fav_numbers['Filippo'][0], ',', fav_numbers['Filippo'][1])
print('Giulio:', fav_numbers['Giulio'][0], ',', fav_numbers['Giulio'][1])
print('Simone:', fav_numbers['Simone'][0], ',', fav_numbers['Simone'][1])
print('Marco:', fav_numbers['Marco'][0], ',', fav_numbers['Marco'][1])
print()



#6-3


glossary: list = {'pop': 'scoppiare', 'insert': 'inserire', 'print': 'stampare', 'list': 'lista', 'dictionary': 'dizionario'}
print(' pop',  glossary['pop'])
print(' insert',  glossary['insert'])
print(' print',  glossary['print'])
print(' list', glossary['list'])
print(' dictionary', glossary['dictionary'])
print()



#6-8


pet1: dict = {'owner': 'Valerio', 'kind': 'dog'}
pet2: dict = {'owner': 'Leonardo', 'kind': 'cat'}
pet3: dict = {'owner': 'Marco', 'kind': 'rabbit'}
pet4: dict = {'owner': 'Edoardo', 'kind': 'hourse'}
pets: list = [pet1, pet2, pet3, pet4]
print(pets[0]['owner'])
print(pets[0]['kind'])
print(pets[1]['owner'])
print(pets[1]['kind'])
print(pets[2]['owner'])
print(pets[2]['kind'])
print(pets[3]['owner'])
print(pets[3]['kind'])
print()



#6-9


favorite_places: dict = {'Marco': 'Napoli', 'Valerio': 'Roma', 'Leonardo': 'Milano'}
print('Francesco: ', favorite_places['Marco'])
print('Gianmarco: ', favorite_places['Valerio'])
print('Gabriel: ', favorite_places['Leonardo'])
print()



#6-11, 6-12


cities: dict = {'Rome': {'country': 'Italy', 'population': '3 million', 'fact': 'has more fountains than any other city on the planet.'}, 'Paris': {'country': 'France', 'population': '2 milion', 'fact': 'not it\'s original name.'}, 'Berlin': {'country': 'Germany', 'population': '3.6 milion', 'fact': 'is the greenest city in Europe.'}}
print('Rome', 'is the capital city of', cities['Rome']['country'], 'and has almost', cities['Rome']['population'], 'residents, it also', cities['Rome']['fact'])
print('Paris', 'is the capital city of', cities['Paris']['country'], ', has almost', cities['Paris']['population'], 'residents, it\'s also', cities['Paris']['fact'])
print('Berlin', 'is the capital city of', cities['Berlin']['country'], ', has almost', cities['Berlin']['population'], 'residents and', cities['Berlin']['fact'])