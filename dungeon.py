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
        # self.doors = {"north": 0,
        #               "south": 0,
        #               "east": 0,
        #               "west": 0}

        self.info = None
        self.unique = {"Abstraction": False,
                      "Encapsulation": False,
                      "Inheritance": False,
                      "Polymorphism": False,
                      "Entrance": False,
                      "Exit": False}

    def __str__(self):
        return f'{self.position}, {self.doors}'

class Dungeon:
    def __init__(self):
        pass

    def generate(self, rows, columns):
        if rows * columns < 6:
            raise ValueError("Dungeon size is too small.")
        elif rows * columns > 225:
            raise ValueError("Dungeon size is too large.")
        self.rows = rows
        self.cols = columns
        self.grid = [[RoomNode(i,j) for j in range(columns)] for i in range(rows)]
        self.set_borders()
        self.set_walls()
        self.set_unique_rooms()

    def set_borders(self):
        for RoomNode in self.grid[0]:
            RoomNode.doors["north"] = 0
        for RoomNode in self.grid[self.rows-1]:
            RoomNode.doors["south"] = 0
        for row in self.grid:
            row[0].doors["west"] = 0
            row[self.cols-1].doors["east"] = 0

    def set_walls(self):
        pass

    def set_unique_rooms(self):
        unique = {"Abstraction": None,
                  "Encapsulation": None,
                  "Inheritance": None,
                  "Polymorphism": None,
                  "Entrance": None,
                  "Exit": None}

        for key in unique:
            while unique[key] is None:
                randrow = random.randint(0, self.rows - 1)
                randcol = random.randint(0, self.cols-1)
                if self.grid[randrow][randcol] not in unique.values():
                    unique[key] = self.grid[randrow][randcol]
                    self.grid[randrow][randcol].unique[key] = True
        #test lines
        # for key, value in unique.items():
        #     print(f'{key} at {value}')

    def traverse(self):
        for list in self.grid:
            for RoomNode in list:
                yield RoomNode

    def draw(self):
        display = MapDisplay(self.cols, self.rows)
        display.draw_border()
        for list in self.grid:
            for room in list:
                display.draw_room(room.position[0], room.position[1], room.doors)
        display.root.mainloop()


if __name__ == '__main__':

    test = Dungeon()
    test.generate(6,9)
    test.draw()
    print(test.grid[1][4])
    test.grid[1][4].doors["north"] = 3
    test.grid[1][4].doors["south"] = 3
    test.grid[1][4].doors["east"] = 3
    test.grid[1][4].doors["west"] = 3
    print(test.grid[1][4])
    test.draw()



