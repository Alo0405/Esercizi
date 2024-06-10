class Persona:
    def __init__(self, first_name: str, last_name: str) -> None:
        
        
        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            print('il nome inserito non è una stringa!')
            self.first_name = None


        if isinstance(last_name, str):
            self.last_name = last_name
        else:
            print('il cognome inserito non è una stringa!')
            self.last_name = None
        

        if isinstance (first_name, str) and isinstance(last_name, str):
            self.age = 0
        else:
            self.age = None

    def setName(self, first_name: str):
        if isinstance(first_name, str):
            self.first_name = first_name
        else: 
            print('il nome inserito non è una stringa!')
        
    def setLastName(self, last_name: str):
        if isinstance(last_name, str):
            self.last_name = last_name
        else: 
            print('il cognome inserito non è una stringa!')

    def setAge(self, age: str):
        if isinstance(age, str):
            self.age = age
        else: 
            print('L\'età deve essere un numero intero')

    def getName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name
    
    def getage(self):
        return self.age
    
    def greet(self):
        print(f'ciao, sono {self.first_name} {self.last_name} e ho {self.age}')






        
        