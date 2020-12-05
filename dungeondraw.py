from tkinter import Tk, Canvas, Frame, Button, Entry

class MapDisplay:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns  = columns
        self.room_unit = 75
        self.root = Tk()
        self.canvas = Canvas(self.root, height=rows*self.room_unit, width=columns*self.room_unit)
        self.canvas.pack(fill="both")

    def draw_border(self):
        self.canvas.create_rectangle(0, 0, self.rows*self.room_unit,self.columns*self.room_unit, fill="white")
        for i in range(1, self.rows - 1):
            self.canvas.create_line(0,i*self.room_unit, self.columns*self.room_unit, i*self.room_unit)
        for i in range(1, self.columns - 1):
            self.canvas.create_line(i * self.room_unit, 0, i * self.room_unit, self.rows * self.room_unit)

    def draw_room(self, x, y, doors):
        self.canvas.create_rectangle(self.room_unit*x, self.room_unit*y, self.room_unit*(x+1), self.room_unit*(y+1))
        for key in doors:
            if key:
                self.draw_door(key, x, y)

        # if room is unique_room:
        #     draw pillar, exit, or entrance
        # else:
        #     if room has potion:
        #         draw potion
        #     if room has pit:
        #         draw pit
        #     if room has other feature:
        #         draw feature

    def draw_door(self, key, x, y):
        if key == "north":
            self.canvas.create_rectangle(
        elif key ==