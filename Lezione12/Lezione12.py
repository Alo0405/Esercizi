#Libreria

'''class Libro:
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
Biblioteca1.show_books()'''

class MovieCatalog:

    def __init__(self) -> None:
        
        self.movies = {}

    def add_movie(self, director_name: str, movies: list):

        for movie in movies:
            if (director_name in self.movies):
                self.movies[director_name].append(movie)
            else:               
                self.movies.update({director_name: [movie]})

    def remove_movie(self, director_name: str, movie: str):

        self.movies[director_name].remove(movie)
        if (self.movies[director_name] == []):
            print('The director has no more movies in the catalog do you want to remove it too? Say y or n: ', end = '')
            choice: str = input()
            if (choice == 'y'):
                self.movies.pop(director_name)

    def list_directors(self):
        
        print('Directors: ')
        for director in self.movies:
            print(director)

    def get_movies(self, director_name: str):

        print('Movies:')
        for movie in self.movies[director_name]:
                print(movie)
    
    def search_movies_by_title(self):

        pass



catalog1: MovieCatalog = MovieCatalog()
catalog1.add_movie('Valerio', ['Harry Potter: La pietra filosofale'])
catalog1.add_movie('Valerio', ['Harry Potter: L\'ordine della fenice'])
catalog1.remove_movie('Valerio', 'Harry Potter: La pietra filosofale')
catalog1.list_directors()
catalog1.get_movies('Valerio')
catalog1.remove_movie('Valerio', 'Harry Potter: L\'ordine della fenice')
catalog1.list_directors()



