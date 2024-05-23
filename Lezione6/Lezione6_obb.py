#9-1, 9-2, 9-4
class Reasturant:
    def __init__(self, reasturant_name: str, cusine_type: str) -> None:
        self.number_served = 0
        self.reasturant_name = reasturant_name
        self.cusine_type = cusine_type
    def describe_reasturant(self):
        print(f'Reasturant name: {self.reasturant_name} | cusine type: {self.cusine_type}')
    def open_reasturant(self):
        print('The Reasturant is open')
    def set_number_served(self, number_served: str):
        self.number_served = number_served
    def increment_number_served(self):
        self.number_served += 1
resturant1: Reasturant= Reasturant ('L\'archetto', 'Pizza')
resturant2: Reasturant= Reasturant ('Burger king', 'Panini')
resturant3: Reasturant= Reasturant ('Da Nino', 'Romana')




#reasturant1.describe_reasturant()
#reasturant2.describe_reasturant()
#reasturant3.describe_resturant()
#reasturant1.open_reasturant()
reasturant1: Reasturant = Reasturant ('Pasta e vino', 'romana')
print(reasturant1.number_served)
reasturant1.number_served = 56
print(reasturant1.number_served)
reasturant1.set_number_served(78)
print(reasturant1.number_served)
reasturant1.increment_number_served()
print(reasturant1.number_served)
#9-3


class User:
    def __init__(self, first_name: str, last_name: str, age: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print(f'name: {self.first_name} | last name: {self.last_name} | age: {self.age}')
    def greet_user(self):
        print('Bella Brooo!!!')
User1: User = User ('Valerio', 'Rondoni', 20)
#User1.describe_user()
#User1.greet_user()
































