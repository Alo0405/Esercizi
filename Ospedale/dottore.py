from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            print('la specializzazione inserita non è una stringa!')
            self.specialization = None

        if isinstance(parcel, str):
            self.parcel = parcel
        else:
            print('la parcella inserita non è di tipo float!')
            self.parcel = None

    def setSpecialization(self, specialization):
        if isinstance(specialization, str):
            self.specialization = specialization
        else: 
            print('la specializzazione inserita non è una stringa!')
    
    def setParcel(self, parcel):
        if isinstance(parcel, str):
            self.parcel = parcel
        else: 
            print('la parcella inserita non è un float!')

    def getSpecialization(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def isAValidDoctor(self, age: int):
        if age > 30:
            print('Doctor nome e cognome is valid!')
            return True
        else:
            print('Doctor nome e cognome is not valid!')
            return False
        
    def doctorGreet(self):
        Persona.greet()
        print(f'Sono un medico {self.specialization}')
