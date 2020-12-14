from tkinter import Tk, Canvas, Frame, Button, Entry
from dungeon import Dungeon

class MapDisplay:

    def __init__(self, rows, columns, root):
        self.rows = rows
        self.columns  = columns
        self.room_unit = 75
        self.root = root
        self.player_map = Canvas(self.root, height=rows*self.room_unit, width=columns*self.room_unit, bg="white")
        self.entire_map = Canvas(self.root, height=rows*self.room_unit, width=columns*self.room_unit, bg="white")

    def draw_entire_map(self, dungeon):
        for list in dungeon.grid:
            for room in list:
                self.draw_walls(room, self.entire_map)
        for list in dungeon.grid:
            for room in list:
                self.draw_room_contents(room, self.entire_map)
                self.draw_door(room, self.entire_map, dungeon)
        return self.entire_map

    def draw_player_map(self, dungeon, adventurer):
        for room in dungeon.visited_rooms:
            self.draw_walls(room, self.player_map)
        for room in dungeon.visited_rooms:
            self.draw_room_contents(room, self.player_map)
            self.draw_door(room, self.player_map, dungeon)
        location = adventurer.current_location
        row, col = location[0], location[1]
        self.player_map.create_text(self.room_unit*col+5, self.room_unit*row+5, text=adventurer.name)
        return self.player_map

    def draw_walls(self, room, canvas):
        position = room.position()
        row, col = position[0], position[1]
        canvas.create_rectangle(self.room_unit * row, self.room_unit * col, self.room_unit * (row+1),
                                self.room_unit * (col+1), width=4)

    def draw_room_contents(self, room, canvas):
        def draw_pillar(pillar):
            canvas.create_text(room_unit * col + offset, room_unit * row + offset, text=pillar[0],
                                    font="Times 12")

        def draw_exit():
            # for testing, will replace with graphic
            canvas.create_text(room_unit * col + offset, room_unit * row + offset, text="Ex",
                                    font="Times 12")

        def draw_entrance():
            # for testing, will replace with graphic
            canvas.create_text(room_unit * col + offset, room_unit * row + offset, text="En",
                                    font="Times 12")


        position = room.position()
        row, col = position[0], position[1]
        room_unit = self.room_unit
        offset = room_unit // 2

        if room.pillar():
            draw_pillar(room.pillar())
        if room.exit():
            draw_exit()
        if room.entrance():
            draw_entrance()

        # else:
        #     if room has potion:
        #         draw potion
        #     if room has pit:
        #         draw pit
        #     if room has other feature:
        #         draw feature

    def draw_door(self, room, canvas, dungeon):
        position = room.position()
        row, col = position[0], position[1]
        # canvas.create_rectangle(self.room_unit * row, self.room_unit * col, self.room_unit * (row+1),
        #                         self.room_unit * (col+1), width=4)
        if dungeon.check_north(row, col):
            canvas.create_rectangle(self.room_unit * col + 10, self.room_unit * row - 2, self.room_unit * col + 65,
                                         self.room_unit * row + 2, fill="white", outline="")
        if dungeon.check_south(row, col):
            canvas.create_rectangle(self.room_unit * col + 10, self.room_unit * (row+1) - 2, self.room_unit * col + 65,
                                         self.room_unit * (row+1) + 2, fill="white", outline="")
        if dungeon.check_west(row, col):
            canvas.create_rectangle(self.room_unit * col - 2, self.room_unit * row + 10, self.room_unit * col + 2,
                                         self.room_unit * row + 65, fill="white", outline="")
        if dungeon.check_east(row, col):
            canvas.create_rectangle(self.room_unit * (col+1) + 2, self.room_unit * row + 10, self.room_unit * (col+1) - 2,
                                                 self.room_unit * row + 65, fill="white", outline="")


if __name__ == '__main__':
    from adventurer import Adventurer

    root = Tk()
    test = Dungeon(6,6)
    test.generate()
    Tom = Adventurer("Tom")
    mapdrawer = MapDisplay(6,6, root)
    # entire_map = mapdrawer.draw_entire_map(test)
    # entire_map.pack()
    player_map = mapdrawer.draw_player_map(test, Tom)
    player_map.pack()
    root.mainloop()
