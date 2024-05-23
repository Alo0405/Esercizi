class Zoo:
      def __init__(self, fence: list, zoo_keepers: list ) -> None:
            self.fence = fence
            self.zoo_keeper = zoo_keepers
      def describe_zoo(self):
            
            print('\nGuardians:\n')
            for zoo_keeper in self.zoo_keeper:
                  
                  print(f'Zookeeper(name={zoo_keeper.name}, surname={zoo_keeper.surname}, id={zoo_keeper.id})\n') 
            
            print('Fences:\n')
            for fence in self.fence:
                  
                  print(f'Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})\n')
                  
                  print('with animals:\n')
                  for animal in fence.animal:
                        
                        print(f'Animal(name={animal.name}, species={animal.species}, age={animal.age})\n')
            print('#########################')
            



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
            self.animal = animal
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
      def remove_animal(self, animal: Animal, fence: Fence):
            if animal in fence.animal:
                  fence.animal.remove(animal)
                  fence.area += (animal.height * animal.width)
      def feed(self, animal: Animal):
            if (animal.fence.area - (((animal.height * 0.02) * (animal.width * 0.02))) >=0):
                  animal.health = animal.health *0.01
                  animal.height = animal.height * 0.02
                  animal.width = animal.width *0.02
                  print('gli animali si stanno nutrendo')
            else:
                  print('non c\'è spazio per nutrire gli animali')

      def clean(self, fence) -> float:
            time: float = 0
            area_occupied: float = 0
            if (fence.area == 0):
                  for i in fence.animal:
                        time += (i.height * i.width)
                  return time
            else:
                  for i in fence.animal:
                        area_occupied += (i.height * i.width)
                  time += (area_occupied / fence.area)
                  return time
                  

                  








