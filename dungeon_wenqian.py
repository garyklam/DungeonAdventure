import random
from dungeondraw_wenqian import MapDisplay
from room_wenqian import Room


class Dungeon:
    def __init__(self, rows, columns):
        if rows * columns < 6:
            raise ValueError("Dungeon size is too small.")
        elif rows * columns > 225:
            raise ValueError("Dungeon size is too large.")
        self.rows = rows
        self.cols = columns
        self.unique_rooms = []
        self.visited_rooms = []

    def generate(self):
        self.visited_rooms.clear()
        self.grid = [[Room(r, c) for c in range(self.cols)] for r in range(self.rows)]
        self.set_borders()
        self.set_entrance_and_exit()
        entrance = self.unique_rooms[0]
        self.set_pillars()
        completable = self.check_traversal(entrance.position()[0], entrance.position()[1])
        if not completable:
            # test lines
            # print("Invalid dungeon, regenerating")
            # path = ""
            # for item in self.visited_rooms:
            #     path += f'{item}, '
            # print(path)
            # self.draw()
            self.generate()
            completable = self.check_traversal(entrance.position()[0], entrance.position()[1])

    def set_borders(self):
        for room in self.grid[0]:
            room.set_north_door(0)
        for room in self.grid[self.rows - 1]:
            room.set_south_door(0)
        for row in self.grid:
            row[0].set_west_door(0)
            row[self.cols - 1].set_east_door(0)

    def set_pillars(self):
        pillars = ("Abstraction", "Encapslation", "Inheritance", "Polymorphism")

        for key in pillars:
            unique_room = self.find_rand_room()
            self.unique_rooms.append(unique_room)
            unique_room.set_pillar(key)
            # test line
            # print(f'{key} at {unique_room}')

    def find_rand_room(self):
        randrow = random.randint(0, self.rows - 1)
        randcol = random.randint(0, self.cols - 1)
        if self.grid[randrow][randcol] not in self.unique_rooms:
            return self.grid[randrow][randcol]
        else:
            return self.find_rand_room()

    def set_entrance_and_exit(self):
        self.unique_rooms.clear()
        entrance = self.find_rand_room()
        entrance.set_entrance()
        self.unique_rooms.append(entrance)
        exit = self.find_rand_room()
        exit.set_exit()
        self.unique_rooms.append(exit)
        # test line
        # print(f'Entrance at {entrance} \nExit at {exit}')

    def check_traversal(self, row, col):
        found_path = False
        if self.grid[row][col] not in self.visited_rooms:
            self.visited_rooms.append(self.grid[row][col])
            if all(items in self.visited_rooms for items in self.unique_rooms):
                # test lines
                # for items in self.visited_rooms:
                #     print(items)
                # self.visited_rooms.clear()
                found_path = True
            else:
                if not found_path and self.check_north(row, col):
                    found_path = self.check_traversal(row - 1, col)
                if not found_path and self.check_west(row, col):
                    found_path = self.check_traversal(row, col - 1)
                if not found_path and self.check_south(row, col):
                    found_path = self.check_traversal(row + 1, col)
                if not found_path and self.check_east(row, col):
                    found_path = self.check_traversal(row, col + 1)
        return found_path

    def in_bounds(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return True
        else:
            return False

    def check_north(self, row, col):
        if self.in_bounds(row - 1, col):
            if self.grid[row][col].north_door() > 2 or self.grid[row - 1][col].south_door() > 2:
                return True
        else:
            return False

    def check_south(self, row, col):
        if self.in_bounds(row + 1, col):
            if self.grid[row][col].south_door() > 2 or self.grid[row + 1][col].north_door() > 2:
                return True
        else:
            return False

    def check_east(self, row, col):
        if self.in_bounds(row, col + 1):
            if self.grid[row][col].east_door() > 2 or self.grid[row][col + 1].west_door() > 2:
                return True
        else:
            return False

    def check_west(self, row, col):
        if self.in_bounds(row, col - 1):
            if self.grid[row][col].west_door() > 2 or self.grid[row][col - 1].east_door() > 2:
                return True
        else:
            return False

    def print_surroundings(self, room):
        row, col = room.position()
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    print(self.grid[r][c])

    def draw(self):
        display = MapDisplay(self.rows, self.cols)
        display.draw_border()
        for list in self.grid:
            for room in list:
                display.draw_room(room)
        display.root.mainloop()


if __name__ == '__main__':
    test = Dungeon(4, 4)
    test.generate()

    test.draw()
