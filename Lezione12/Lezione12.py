class Libro:
    def __init__(self, titolo: str, autore: str) -> None:
        self.titolo = titolo
        self.autore = autore
        self.stato_prestito = False
class Biblioteca:
    def __init__(self) -> None:
        self.books = []
    def add_books(self, book: Libro):
        self.book = book
        self.books.append(book)
        print('Il libro è stato aggiunto')
    def lend_books(self, titolo: str):
        for book in self.books:
            if book.titolo == titolo and book.stato_prestito == False:
                book.stato_prestito == True
        print('il libro è disponibile')
    def give_back_books(self, titolo: str):
        for book in self.books:
            if book.titolo == titolo:
                book.stato_prestito == False
        print('il libro è stato restituito')
    
    def show_books(self):
        flag: bool = False
        list1: list = []
        for read in self.books:
            list1.append(read.titolo)
            flag = True
        if flag == False:
            print('ERRORE!!!!!!')
        else:
            print(list1)





book1: Libro = Libro ('lalalal', 'Valerio')
book2: Libro = Libro ('ololo', 'Gabriel')
Biblioteca1: Biblioteca = Biblioteca()
Biblioteca1.add_books(book1)
Biblioteca1.lend_books(book2)
Biblioteca1.show_books()



