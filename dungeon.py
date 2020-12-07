import random
from dungeondraw import MapDisplay

class RoomNode:
    def __init__(self, row, column):
        self.position = (row, column)
        self.doors = {"north": random.randint(0, 4),
                      "south": random.randint(0, 4),
                      "east": random.randint(0, 4),
                      "west": random.randint(0, 4)
                      }

        self.info = None
        self.pillar = None
        self.isexit = False
        self.isentrance = False

    def __str__(self):
        return f'{self.position}, {self.doors}'

class Dungeon:
    def __init__(self, rows, columns):
        if rows * columns < 6:
            raise ValueError("Dungeon size is too small.")
        elif rows * columns > 225:
            raise ValueError("Dungeon size is too large.")
        self.rows = rows
        self.cols = columns
        self.unique_rooms = []

    def generate(self):
        self.grid = [[RoomNode(r,c) for c in range(self.cols)] for r in range(self.rows)]
        self.set_borders()
        self.set_pillars()
        self.set_entrance_and_exit()
        completable = self.check_traversal()
        while completable == False:
            self.generate()
            completable = self.check_traversal()

    def set_borders(self):
        for RoomNode in self.grid[0]:
            RoomNode.doors["north"] = 0
        for RoomNode in self.grid[self.rows-1]:
            RoomNode.doors["south"] = 0
        for row in self.grid:
            row[0].doors["west"] = 0
            row[self.cols-1].doors["east"] = 0

    def set_pillars(self):
        pillars = ("Abstraction", "Encapslation", "Inheritance", "Polymorphism")

        for key in pillars:
            unique_room = self.find_rand_room()
            self.unique_rooms.append(unique_room)
            unique_room.pillar = key
        #test lines
        # for key, value in pillars.items():
        #     print(f'{key} at {value}')

    def find_rand_room(self):
        randrow = random.randint(0, self.rows - 1)
        randcol = random.randint(0, self.cols - 1)
        if self.grid[randrow][randcol] not in self.unique_rooms:
            return self.grid[randrow][randcol]
        else:
            return self.find_rand_room()


    def set_entrance_and_exit(self):
        entrance = self.find_rand_room()
        entrance.isentrance = True
        self.unique_rooms.append(entrance)
        exit = self.find_rand_room()
        exit.isexit = True
        self.unique_rooms.append(exit)
        print(f'Entrance at {entrance} \nExit at {exit}')


    def check_traversal(self):
        pass


    def draw(self):
        display = MapDisplay(self.rows, self.cols)
        display.draw_border()
        for list in self.grid:
            for room in list:
                display.draw_room(room)
        display.root.mainloop()



if __name__ == '__main__':

    test = Dungeon(3,3)
    test.generate()
    test.draw()


