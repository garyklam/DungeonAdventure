from tkinter import Tk, Canvas, Frame, Button, Entry

class MapDisplay:

    def __init__(self, dungeon, root):
        self.dungeon = dungeon
        self.rows = self.dungeon.rows
        self.cols  = self.dungeon.cols
        self.room_unit = 75
        self.root = root
        self.player_map = Canvas(self.root, height=self.rows*self.room_unit, width=self.cols*self.room_unit, bg="white")
        self.entire_map = Canvas(self.root, height=self.rows*self.room_unit, width=self.cols*self.room_unit, bg="white")

    def draw_entire_map(self):
        for list in self.dungeon.grid:
            for room in list:
                self.draw_walls(room, self.entire_map)
        for list in self.dungeon.grid:
            for room in list:
                self.draw_room_contents(room, self.entire_map)
                self.draw_door(room, self.entire_map)
        return self.entire_map

    def draw_player_map(self, adventurer):
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
        position = room.position()
        row, col = position[0], position[1]
        canvas.create_rectangle(self.room_unit * col, self.room_unit * row, self.room_unit * (col+1),
                                self.room_unit * (row+1), width=4)

    def draw_room_contents(self, room, canvas):
        def draw_pillar(pillar):
            canvas.create_text(room_unit * col + 15, room_unit * (row+1) - 15, text=pillar[0],
                                    font="Times 14")

        def draw_exit():
            canvas.create_text(room_unit * col + offset, room_unit * row + offset, text="Ex",
                                    font="Times 14")

        def draw_entrance():
            canvas.create_text(room_unit * col + offset, room_unit * row + offset, text="En",
                                    font="Times 14")

        def draw_potion():
            canvas.create_oval(room_unit * col + 8, room_unit * row +8, room_unit * col + 18, room_unit * row + 18,
                               fill="red")

        def draw_pit():
            canvas.create_oval(room_unit * col + 25, room_unit * row + 25, room_unit * col + 49, room_unit * row + 49,
                               fill="light grey", outline="black")

        def draw_vision():
            canvas.create_polygon(room_unit * col + 62, room_unit * row + 14, room_unit * col + 66, room_unit * row + 8,
                                  room_unit * col + 70, room_unit * row + 14, room_unit * col + 66, room_unit * row + 20,
                                  fill="blue")

        position = room.position()
        row, col = position[0], position[1]
        room_unit = self.room_unit
        offset = room_unit // 2


        if room.exit():
            draw_exit()
        elif room.entrance():
            draw_entrance()
        else:
            if room.pillar():
                draw_pillar(room.pillar())
            if room.healing_potion():
                draw_potion()
            if room.pit():
                draw_pit()
            if room.vision_potion():
                draw_vision()

    def draw_door(self, room, canvas):
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
    def __init__(self, canvas, dungeon, adventurer):
        self.canvas = canvas
        self.dungeon = dungeon
        location = adventurer.current_location
        self.row = location[0]
        self.col = location[1]

    def draw(self):
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
        row_offset = self.row-1
        col_offset = self.col-1
        display_row = row - row_offset
        display_col = col - col_offset
        if room in self.dungeon.visited_rooms:
            self.canvas.create_rectangle(display_col * 200 + 10, display_row * 200 + 10, (display_col + 1) * 200 + 10,
                                         (display_row + 1) * 200 + 10, fill="white", width=4)
            self.draw_doors(row, col)
            if room.exit():
                self.draw_exit(display_row, display_col)
            elif room.entrance():
                self.draw_entrance(display_row, display_col)
            else:
                if room.pillar():
                    self.draw_pillar(room.pillar(), display_row, display_col)
                if room.healing_potion():
                    self.draw_potion(display_row, display_col)
                if room.pit():
                    self.draw_pit(display_row, display_col)
                if room.vision_potion():
                    self.draw_vision(display_row, display_col)

        else:
            self.canvas.create_rectangle(display_col * 200 + 10, display_row * 200 + 10, (display_col + 1) * 200 + 10,
                                         (display_row + 1) * 200 + 10, fill="light grey", width=4)


    def draw_doors(self, row, col):
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

    def draw_pillar(self, pillar, row, col):
        self.canvas.create_text(200 * col + 30, 200 * (row + 1) - 15, text=pillar[0],
                           font="Times 24")

    def draw_exit(self, row, col):
        self.canvas.create_text(200 * col + 110, 200 * row + 110, text="Ex",
                           font="Times 24")

    def draw_entrance(self, row, col):
        self.canvas.create_text(200 * col + 110, 200 * row + 110, text="En",
                           font="Times 24")

    def draw_potion(self, row, col):
        self.canvas.create_oval(200 * col + 15, 200 * row + 15, 200 * col + 30, 200 * row + 30,
                           fill="red")

    def draw_pit(self, row, col):
        self.canvas.create_oval(200 * col + 70, 200 * row + 70, 200 * col + 150, 200 * row + 150,
                           fill="light grey", outline="black")

    def draw_vision(self, row, col):
        self.canvas.create_polygon(200 * col + 189, 200 * row + 23, 200 * col + 195, 200 * row + 15,
                                200 * col + 201, 200 * row + 23, 200 * col + 195, 200 * row + 31,
                                fill="blue")





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
