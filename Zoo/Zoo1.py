class Zoo:
    def __init__(self, fence: list, zoo_keepers: list ) -> None:
            self.fence = fence
            self.zoo_keeper = zoo_keepers



class Animal:
      def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: int, health: float) -> None:
            self.name = name
            self.species = species
            self.age = age
            self.height = height
            self.width = width
            self.preferred_habitat = preferred_habitat
            self.health =  round(100 * (1 / age), 3)



class Fence:
      def __init__(self, animal: list, area: float, temperature: float, habitat: str) -> None:
            self.animal: animal
            self.area = area
            self.temperature = temperature
            self.habitat = habitat



class ZooKeeper:
      def __init__(self, name: str, surname: str, id: int) -> None:
            self.name = name
            self.surname = surname
            self.id = id
      def add_animal(self, animal: Animal, fence: Fence):
            
            if (animal.preferred_habitat == fence.habitat) and (fence.area - (animal.height * animal.width)>=0):
                  fence.animal.append(animal)
                  fence.area -= (animal.height * animal.width)
                  print('l\'animale è nel recinto')
            else:
                  print('non c\'è spazio per l\'animale nel recinto')
            







animal1: Animal = Animal('lion', 'feline', 7, 2.0, 1.0, 'savannah', 70)
fence1: Fence = Fence([] , 100.0, 25.0, 'savannah')
ZooKeeper1: ZooKeeper = ZooKeeper('')