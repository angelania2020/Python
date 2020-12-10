

class Animals:



    def __init__(self, name, size):



         self.name = name



         self.size = size



    def print_info_animals(self):

        print(f'Названия: {​​self.name}​​, Размер: {​​self.size}​​')




Bear = Animals('Медведь', 400)

Bear.print_info_animals()




class Birds(Animals):

    def __init__(self, name, size, wings):

        super().__init__ (name, size)

        self.wings = wings



    def print_info_bird(self):

        print(f"Названия: {​​self.name}​​, Размер: {​​self.size}​​, крылья: {​​self.wings}​​")




Pinguin = Birds ("Пингвин", 250, "sfdwserf")

Pinguin.print_info_bird()
