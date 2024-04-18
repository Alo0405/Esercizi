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







