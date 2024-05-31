'''class Contatore:
    def __init__(self, conteggio: float = 0):
        self.conteggio = conteggio
    def setZero(self):
        self.conteggio = 0
    def add1(self):
        self.conteggio += 1
    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -=1
        elif self.conteggio == 0:
            print("Non è possibile eseguire la sottrazione")
        else:
            print("il numero e troppo piccolo")
    def get(self):
        return self.conteggio
    def mostra(self):
        print(f'Conteggio attuale: {self.conteggio}')'''
#2
class RecipeManager:
    def __init__(self):
        self.recipe = {}
    def create_recipe(self, name: str, ingredients: list):
        if name in recipe:
            print('ERRORE!!!')
    def add_ingredient(self, recipe_name: str, ingredient: list):
        if recipe_name in self.recipe:
            self.recipe[recipe_name].append(ingredient)
            return self.recipe
        else:
            print('L\'ingrediente esiste già, o la ricetta non esiste')
    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name in self.recipe:
            self.recipe[recipe_name].remove(ingredient)
            return self.recipe
        else:
            print('L\'ingrediente non esiste, o la ricetta non esiste')
