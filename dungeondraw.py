from tkinter import Tk, Canvas, Frame, Button, Entry

class MapDisplay:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns  = columns
        self.room_unit = 75
        self.root = Tk()
        self.canvas = Canvas(self.root, height=rows*self.room_unit, width=columns*self.room_unit, bg="white")
        self.canvas.pack()

    def draw_border(self):
        for i in range(1, self.rows):
            self.canvas.create_line(0,i*self.room_unit, self.columns*self.room_unit, i*self.room_unit, width=4)
        for i in range(1, self.columns):
            self.canvas.create_line(i * self.room_unit, 0, i * self.room_unit, self.rows * self.room_unit, width=4)

    def draw_room(self, x, y, doors):
        for key, value in doors.items():
            if value > 2:
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
            self.canvas.create_rectangle(self.room_unit * x + 10, self.room_unit * y - 2, self.room_unit * x + 65,
                                         self.room_unit * y + 2, fill="white", outline="")
        elif key == "south":
            y+=1
            self.canvas.create_rectangle(self.room_unit * x + 10, self.room_unit * y - 2, self.room_unit * x + 65,
                                         self.room_unit * y + 2, fill="white", outline="")
        elif key == "west":
            self.canvas.create_rectangle(self.room_unit * x - 2, self.room_unit * y + 10, self.room_unit * x + 2,
                                         self.room_unit * y + 65, fill="white", outline="")
        elif key == "east":
            x+=1
            self.canvas.create_rectangle(self.room_unit * x + 2, self.room_unit * y + 10, self.room_unit * x - 2,
                                         self.room_unit * y + 65, fill="white", outline="")