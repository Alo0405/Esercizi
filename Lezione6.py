class Person:  
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
    print(person.get_ssn())
