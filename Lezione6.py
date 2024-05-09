'''class Person:  
    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:


        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = '04/05/2004'
        self._birth_place: str = 'Rome'
        self._gender: str = 'male'
        self._ssn: str =  None

        self.compute_ssn()


    def __str__(self) -> str:
        return f'Name: {self._name}     cognome: {self._surname}     ssn:{self._ssn}'
    
    
    def get_ssn(self) -> str:
        """
        This function returns the ssn value
        input: none
        return:self._name : str, the function returns the ssn value
        """
        return self._ssn
    
    
    def set_ssn(self, ssn: str):
        """
        This function returns the ssn value
        input: none
        return:self._name : str, the function returns the ssn value
        """
        raise Exception ('you connot change the ssn')
    
    
    def get_name(self):
        """
        This function returns a person's name
        input: none
        return:self._name : str, the function returns the person's name
        """
        return self._name
    
    
    def set_name(self, name: str):
        """
        This function set the attribute name
        input: name : str, the parameter contains the user's name 
        return: None
        """
        self._name = name
        self._ssn = self.compute_ssn
    
    
    def compute_ssn(self) -> bool:
        """
        check the ssn's correctness
        """
        first_three_name_char = self._name [:3]
        last_three_surname_char = self._surname[-3:]
        self._ssn = first_three_name_char + last_three_surname_char

Person_1: Person = Person(name='Valerio', 
                          surname='Rondoni', 
                          birth_date='04/05/2004', 
                          birth_place='Rome', 
                          gender='male')

print(str(Person_1))

queue: list[Person] = [Person_1]
for person in queue:
    print(person.get_ssn())'''

'''class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
alice: Person = Person('Alice W.', 45)
bob: Person = Person('Bob M.', 36)
print(bob.age)
persons= [alice, bob]
for p in persons:
    print(p.age)


if alice.age > bob.age:
    print(alice.age)
else:
    print(bob.age)'''
'''class Student:
    def __init__(self, name: str, studyProgram: str, age: int, gender: str ) -> None:
        self.name: str = name
        self.studyProgram: str = studyProgram
        self.age: int = age
        self.gender: str = gender
    def printInfo(self) -> None:
        print(f'Name : {self.name} / SP : {self.studyProgram} / Age : {self.age} / Gender : {self.gender}') 
Student1: Student = Student('Valerio', 'Python', 19, 'male')
Student2: Student = Student('Gabriel', 'Python', 56, 'female')
Student3: Student = Student('Daniele', 'Python', 78, 'male')
Student1.printInfo()
Student2.printInfo()
Student3.printInfo()'''




'''class Animal:
    def __init__(self, name, gender, legs) -> None:
        self.name: str = name
        self.gender: str = gender
        self.legs: str = legs
    def setlegs(self, legs: int):
        self.legs = legs
    def getlegs(self):
        return self.legs
    def printInfo(self):
        print(f'Name: {self.name} / Gender: {self.gender} / legs: {self.legs}')    





animal1: Animal = Animal('tiger', 'male', 4)
animal2: Animal = Animal('lion', 'female', 4)
animal1.legs = 9
animal1.setlegs(4)
print(animal1.getlegs())
animal1.printInfo()'''

class Food:
    def __init__(self, name, price, description) -> None:
        self.name: str = name
        self.price: float = price
        self.description: str =description
class Menu:
    def __init__(self, food_list: list[int] = []) -> None:

        self.food_list: list [int] = food_list

    def addfood(self, food: Food) -> None:

        self.food_list.append(food)

    def removefood(self, food: Food) -> None:

        self.food_list.remove(food)
    def printprices(self) -> None:
        for read in self.food_list:
            print(f"price: {read.price} / name: {read.name}")
    def get_average_price(self) -> float:
        prezzo = 0
        for i in self.food_list:
            prezzo += i.price
        media = prezzo / len(self.food_list)
        return media
    


        


food1: Food = Food('Bread', 0.70, 'Grano duro')
food2: Food = Food('Apple', 0.50, 'Fruit')
food3: Food = Food('Pizza', 7.0, 'Margherita')
food4: Food = Food('Pasta', 1.0, 'Spaghetti')
menu: Menu = Menu([food1, food2, food3])
menu.addfood(food4)
menu.removefood(food2)
menu.printprices()
print(menu.get_average_price())

        





