import random
from room import Room

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

    def get_room(self, row, col):
        return self.grid[row][col]

    def resize_dungeon(self, row, col):
        """
        Alters dimension fields of the dungeon, does not create a new grid of rooms, needs to call generate to actually
        resize the dungeon.
        """
        self.rows = row
        self.cols = col

    def generate(self):
        """
        Creates a new grid of rooms, sets the borders, sets the entrance, exit and pillars, then checks if it is
        possible to reach the exit and all of the pillars from the entrance. If not, the dungeon is remade and checked
        again, repeating until the dungeon is traversable.
        """
        self.visited_rooms.clear()
        self.grid = [[Room(r,c) for c in range(self.cols)] for r in range(self.rows)]
        self.set_borders()
        self.set_entrance_and_exit()
        entrance = self.unique_rooms[0].position()
        self.set_pillars()
        completable = self.check_traversal(entrance[0], entrance[1])
        if not completable:
            # test lines
            # print("Invalid dungeon, regenerating")
            # path = ""
            # for item in self.visited_rooms:
            #     path += f'{item}, '
            # print(path)
            # self.draw()
            self.generate()
            completable = self.check_traversal(entrance[0], entrance[1])


    def set_borders(self):
        """Sets the door values of the rooms on the edge of the dungeon to be walls."""
        for Room in self.grid[0]:
            Room.set_north_border()
        for Room in self.grid[self.rows-1]:
            Room.set_south_border()
        for row in self.grid:
            row[0].set_west_border()
            row[self.cols-1].set_east_border()

    def set_pillars(self):
        """
        Finds a random room that is not already a pillar, the exit or entrance and sets it pillar field to one of
        the pillars in the list, then adds it to a list of unique rooms so that it cannot be chosen for the next pillar.
        """
        pillars = ("Abstraction", "Encapsulation", "Inheritance", "Polymorphism")

        for key in pillars:
            unique_room = self.find_rand_room()
            self.unique_rooms.append(unique_room)
            unique_room.set_pillar(key)
            # test line
            # print(f'{key} at {unique_room}')

    def find_rand_room(self):
        """
        Finds and returns a random room that is not already a unique room.
        :return: Room
        """
        randrow = random.randint(0, self.rows - 1)
        randcol = random.randint(0, self.cols - 1)
        if self.grid[randrow][randcol] not in self.unique_rooms:
            return self.grid[randrow][randcol]
        else:
            return self.find_rand_room()


    def set_entrance_and_exit(self):
        """
        Finds a random room to be the entrance and exit, adds these rooms to a list of unique rooms to avoid adding
        a pillar to either room.
        """
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
                    found_path = self.check_traversal(row-1, col)
                if not found_path and self.check_west(row, col):
                    found_path = self.check_traversal(row, col-1)
                if not found_path and self.check_south(row, col):
                    found_path = self.check_traversal(row+1, col)
                if not found_path and self.check_east(row, col):
                    found_path = self.check_traversal(row, col+1)
        return found_path

    def in_bounds(self, row, col):
        """
        Checks if the given row and column are within the bounds of the dungeon, returns true if it is, returns
        false if it is not
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return True
        else:
            return False

    def check_north(self, row, col):
        if self.in_bounds(row-1, col):
            curr = self.get_room(row, col)
            doors1 = curr.doors()
            south = self.get_room(row-1, col)
            doors2 = south.doors()
            if doors1["north"] > 2 or doors2["south"] > 2:
                return True
        else:
            return False

    def check_south(self, row, col):
        if self.in_bounds(row+1, col):
            curr = self.get_room(row, col)
            doors1 = curr.doors()
            north = self.get_room(row+1, col)
            doors2 = north.doors()
            if doors1["south"] > 2 or doors2["north"] > 2:
                return True
        else:
            return False

    def check_east(self, row, col):
        if self.in_bounds(row, col+1):
            curr = self.get_room(row, col)
            doors1 = curr.doors()
            west = self.get_room(row, col+1)
            doors2 = west.doors()
            if doors1["east"] > 2 or doors2["west"] > 2:
                return True
        else:
            return False

    def check_west(self, row, col):
        if self.in_bounds(row, col-1):
            curr = self.get_room(row, col)
            doors1 = curr.doors()
            east = self.get_room(row, col-1)
            doors2 = east.doors()
            if doors1["west"] > 2 or doors2["east"] > 2:
                return True
        else:
            return False


if __name__ == '__main__':

    test = Dungeon(6,6)
    test.generate()

    # test.show_map()
    # test.show_map_no_fog()
    # test.draw_path()


