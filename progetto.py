'''class Room:
    def __init__(self, ID: float, floor: int, seats: int, area: float)->None:
        self.ID = ID
        self.floor = floor
        self.seats = seats
        self.area = seats*2
    def get_ID(self):
        return self.ID
    def get_floor(self):
        return self.floor
    def get_seats(self):
        return self.seats
    def get_area(self):
        return self.area
class building:
    def __init__(self, name: str, address: float, floors: int)->None:
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []
    def get_floors(self):
        return self.floors
    def get_rooms(self):
        return self.rooms
    def add_room(self, room: Room):
        if room.floor >= min(self.floors) and room.floor <= min(self.floors):
            self.rooms.append(room)
    def area(self):
        area_totale = 0
        for i in self.rooms:
            area_totale = area_totale + i.self.area_totale
    '''

class Person:
    def __init___(self, cf, name, surname, age):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
class Student(Person):
    def __init__(self, cf, name, surname, age) -> None:
        super().__init__(cf, name, surname, age)
class lecturer(Person):
    def __init__(self, cf, name, surname, age) -> None:
        super().__init__(cf, name, surname, age)    
class Group:
    def __init__(self, name, limit) -> None:
           self.name = name
           self.limit = limit
           self.students = ()
           self.lectures = ()
    def get_name(self):
        return self.name
    def get_limit(self):
        return self.limit
    def get_students(self):
        return self.students
    #def get_limit_lectures(self):
        #limit_lectures = 1

    def add_students(self, student):
        self.students.append(student)
    def add_lectures(self, lecture):
        self.lectures.append(lecture)
    
    
    
    
    
    
    
    
    
    
    
        