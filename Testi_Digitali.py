class Documento:
    def __init__(self) -> None:
        self.testo = ''

    def getText(self):
        return self.testo
    
    def setText(self, testo: str):
        self.testo = testo
    
    def islnText(self, chiave: bool):
        if chiave in self.testo:
            return True
        else:
            return False


class Email(Documento):
    def __init__(self) -> None:
        super().__init__()
        self.mittente = ''
        self.destinatario = ''
        self.titolo_messaggio = ''

    def getMittente(self):
        return self.mittente
    
    def setMittente(self, mittente: str):
        self.mittente = mittente

    def getDestinatario(self):
        return self.destinatario
    
    def setDestinatario(self, destinatario: str):
        self.destinatario = destinatario

    def getTitolo(self):
        return self.titolo_messaggio
    
    def setTitolo(self, titolo_messaggio: str):
        self.titolo_messaggio = titolo_messaggio
    
    def setText(self, corpo_messaggio: str):
        return super().setText(corpo_messaggio)
    
    def getText(self):
        return f'{self.mittente}{self.destinatario}{self.titolo_messaggio}{super().getText()}'

