from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, id: str) -> None:
        super().__init__(first_name, last_name) 

        if isinstance(id, str):
            self.id = id
        else:
            print('l\'id inserita non è una stringa!')
            self.id = None
        
    def setidCode(self, idCode):
        self.idCode = idCode

    def getidCode(self):
        return self.idCode
    
    def patientInfo(self):
        print(f'Paziente: {self.first_name} {self.last_name}\nID: {self.idCode}')

