from tkinter import Tk, Canvas, Frame, Button, Entry

class MapDisplay:
    """Contains methods to create map objects for the adventure game."""
    def __init__(self, dungeon, root):
        self.dungeon = dungeon
        self.rows = self.dungeon.rows
        self.cols  = self.dungeon.cols
        self.room_unit = 75
        self.root = root
        self.player_map = Canvas(self.root, height=self.rows*self.room_unit, width=self.cols*self.room_unit, bg="white")
        self.entire_map = Canvas(self.root, height=self.rows*self.room_unit, width=self.cols*self.room_unit, bg="white")

    def draw_entire_map(self):
        """Draws all of the rooms in the dungeon along with their contents. Draws walls in a separate loop from the
        doors to avoid overlapping lines causing doors to be obscoured in the map. Returns the canvas object after
        drawing all features."""
        for list in self.dungeon.grid:
            for room in list:
                self.draw_walls(room, self.entire_map)
        for list in self.dungeon.grid:
            for room in list:
                self.draw_room_contents(room, self.entire_map)
                self.draw_door(room, self.entire_map)
        return self.entire_map

    def draw_player_map(self, adventurer):
        """Draws all of the rooms that are in the list of visited rooms in the dungeon. Takes the position of the
        adventurer and displays the adventurer's name in the corresponding room. Returns the canvas object after
        drawing all features."""
        for room in self.dungeon.visited_rooms:
            self.draw_walls(room, self.player_map)
        for room in self.dungeon.visited_rooms:
            self.draw_room_contents(room, self.player_map)
            self.draw_door(room, self.player_map)
        location = adventurer.current_location
        row, col = location[0], location[1]
        self.player_map.create_text(self.room_unit*col+37, self.room_unit*(row+1)-10, text=adventurer.name)
        return self.player_map

    def draw_walls(self, room, canvas):
        """Draws a rectangle representing a room in the dungeon in the canvas that is passed in. Uses the position of
        the room to position the rectangle within the canvas."""
        position = room.position()
        row, col = position[0], position[1]
        canvas.create_rectangle(self.room_unit * col, self.room_unit * row, self.room_unit * (col+1),
                                self.room_unit * (row+1), width=4)

    def draw_room_contents(self, room, canvas):
        """Draws the contents of the room passed in. Checks if the room contains the entrance or exit, then checks
        if the room has a pillar, pit, vision potion, or healing potion. Draws the corresponding object if any
        of the checks returns true."""
        position = room.position()
        row, col = position[0], position[1]
        offset = self.room_unit // 2

        if room.exit():
            canvas.create_text(self.room_unit * col + offset, self.room_unit * row + offset, text="Ex",
                               font="Times 14")
        elif room.entrance():
            canvas.create_text(self.room_unit * col + offset, self.room_unit * row + offset, text="En",
                               font="Times 14")
        else:
            if room.pillar():
                pillar = room.pillar()
                canvas.create_text(self.room_unit * col + 15, self.room_unit * (row + 1) - 15, text=pillar[0],
                                   font="Times 14")
            if room.healing_potion():
                canvas.create_oval(self.room_unit * col + 8, self.room_unit * row + 8,
                                   self.room_unit * col + 18, self.room_unit * row + 18, fill="red")
            if room.pit():
                canvas.create_oval(self.room_unit * col + 25, self.room_unit * row + 25,
                                   self.room_unit * col + 49, self.room_unit * row + 49, fill="light grey")
            if room.vision_potion():
                canvas.create_polygon(self.room_unit * col + 62, self.room_unit * row + 14,
                                      self.room_unit * col + 66, self.room_unit * row + 8,
                                      self.room_unit * col + 70, self.room_unit * row + 14,
                                      self.room_unit * col + 66, self.room_unit * row + 20, fill="blue")

    def draw_door(self, room, canvas):
        """Draws the doors of the rooms in the dungeon on the canvas that is passsed in. Checks if it is possible to
        travel in each direction using the dungeon's check_direction method and draws a door if it is possible to
        travel in that direction."""
        position = room.position()
        row, col = position[0], position[1]
        if self.dungeon.check_north(row, col):
            canvas.create_rectangle(self.room_unit * col + 10, self.room_unit * row - 2, self.room_unit * col + 65,
                                         self.room_unit * row + 2, fill="white", outline="")
        if self.dungeon.check_south(row, col):
            canvas.create_rectangle(self.room_unit * col + 10, self.room_unit * (row+1) - 2, self.room_unit * col + 65,
                                         self.room_unit * (row+1) + 2, fill="white", outline="")
        if self.dungeon.check_west(row, col):
            canvas.create_rectangle(self.room_unit * col - 2, self.room_unit * row + 10, self.room_unit * col + 2,
                                         self.room_unit * row + 65, fill="white", outline="")
        if self.dungeon.check_east(row, col):
            canvas.create_rectangle(self.room_unit * (col+1) + 2, self.room_unit * row + 10, self.room_unit * (col+1) - 2,
                                                 self.room_unit * row + 65, fill="white", outline="")


class GameDisplay:
    """Contains methods for drawing the main game display, which shows the room the adventurer is in and the adjacent
    rooms that can be reached from the current room."""
    def __init__(self, canvas, dungeon):
        self.canvas = canvas
        self.dungeon = dungeon
        entrance_location = self.dungeon.unique_rooms[0].position()
        self.row = entrance_location[0]
        self.col = entrance_location[1]

    def set_position(self, location):
        """Changes the position of the central room drawn in the game display."""
        self.row = location[0]
        self.col = location[1]

    def draw(self):
        """Clears the current display and redraws it. Checks if the adjacent rooms can be reached and if they can,
        draws out the room. Then draws the central room."""
        self.canvas.delete("all")
        if self.dungeon.check_north(self.row, self.col):
            north = self.dungeon.get_room(self.row-1, self.col)
            self.draw_room(north, self.row-1, self.col)
        if self.dungeon.check_south(self.row, self.col):
            south = self.dungeon.get_room(self.row+1, self.col)
            self.draw_room(south, self.row+1, self.col)
        if self.dungeon.check_east(self.row, self.col):
            east = self.dungeon.get_room(self.row, self.col+1)
            self.draw_room(east, self.row, self.col+1)
        if self.dungeon.check_west(self.row, self.col):
            west = self.dungeon.get_room(self.row, self.col-1)
            self.draw_room(west, self.row, self.col-1)
        room = self.dungeon.get_room(self.row, self.col)
        self.draw_room(room, self.row, self.col)


    def draw_room(self, room, row, col):
        """Converts the position of the room within the dungeon to the position on the game display. If the room has
        been visited, then the doors and contents of the room are drawn. If the room has not been visited, then a
        grey square is drawn."""
        row_offset = self.row-1
        col_offset = self.col-1
        display_row = row - row_offset
        display_col = col - col_offset
        if room in self.dungeon.visited_rooms:
            self.canvas.create_rectangle(display_col * 200 + 10, display_row * 200 + 10, (display_col + 1) * 200 + 10,
                                         (display_row + 1) * 200 + 10, fill="white", width=4)
            self.draw_doors(row, col)
            if room.exit():
                self.canvas.create_text(200 * display_col + 110, 200 * display_row + 110, text="Ex",
                                        font="Times 24")
            elif room.entrance():
                self.canvas.create_text(200 * display_col + 110, 200 * display_row + 110, text="En",
                                        font="Times 24")
            else:
                if room.pillar():
                    pillar = room.pillar()
                    self.canvas.create_text(200 * display_col + 30, 200 * (display_row + 1) - 15, text=pillar[0],
                                            font="Times 24")
                if room.healing_potion():
                    self.canvas.create_oval(200 * display_col + 15, 200 * display_row + 15,
                                            200 * display_col + 30, 200 * display_row + 30, fill="red")
                if room.pit():
                    self.canvas.create_oval(200 * display_col + 70, 200 * display_row + 70,
                                            200 * display_col + 150, 200 * display_row + 150, fill="light grey")
                if room.vision_potion():
                    self.canvas.create_polygon(200 * display_col + 189, 200 * display_row + 23,
                                               200 * display_col + 195, 200 * display_row + 15,
                                               200 * display_col + 201, 200 * display_row + 23,
                                               200 * display_col + 195, 200 * display_row + 31, fill="blue")

        else:
            self.canvas.create_rectangle(display_col * 200 + 10, display_row * 200 + 10, (display_col + 1) * 200 + 10,
                                         (display_row + 1) * 200 + 10, fill="light grey", width=4)


    def draw_doors(self, row, col):
        """Checks if it is possible to travel to the adjacent room. If true, then a door is drawn on the appropriate
        side"""
        row_offset = self.row - 1
        col_offset = self.col - 1
        display_row = row - row_offset
        display_col = col - col_offset
        if self.dungeon.check_north(row, col):
            self.canvas.create_line(200 * display_col + 55, 200 * (display_row)+10, 200 * display_col + 165,
                                    200 * (display_row) +10, fill="white", width=4)
        if self.dungeon.check_south(row, col):
            self.canvas.create_line(200 * display_col + 55, 200 * (display_row + 1) +10,
                                    200 * display_col + 165,
                                    200 * (display_row + 1) + 10, fill="white", width=4)
        if self.dungeon.check_west(row, col):
            self.canvas.create_line(200 * (display_col) + 10, 200 * display_row + 55, 200 * (display_col) + 10,
                                    200 * display_row + 165, fill="white", width=4)
        if self.dungeon.check_east(row, col):
            self.canvas.create_line(200 * (display_col + 1) + 10, 200 * display_row + 55,
                                    200 * (display_col + 1) + 10,
                                    200 * display_row + 165, fill="white", width=4)


if __name__ == '__main__':
    from adventurer import Adventurer

    root = Tk()
    test = Dungeon(6,6)
    test.generate()
    Tom = Adventurer("Tom")
    mapdrawer = MapDisplay(test, root)
    # entire_map = mapdrawer.draw_entire_map()
    # entire_map.pack()
    player_map = mapdrawer.draw_player_map(Tom)
    player_map.pack()
    root.mainloop()
