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

    def draw_room(self, room):
        row, col = room.position[0], room.position[1]
        self.draw_door(room.doors, row, col)
        if room.pillar:
            self.draw_pillar(room.pillar, row, col)
        if room.isexit:
            self.draw_exit(row, col)
        if room.isentrance:
            self.draw_entrance(row, col)

        # else:
        #     if room has potion:
        #         draw potion
        #     if room has pit:
        #         draw pit
        #     if room has other feature:
        #         draw feature

    def draw_door(self, doors, row, col):
        for key, value in doors.items():
            if value > 2:
                if key == "north":
                    self.canvas.create_rectangle(self.room_unit * col + 10, self.room_unit * row - 2, self.room_unit * col + 65,
                                                 self.room_unit * row + 2, fill="white", outline="")
                elif key == "south":
                    # row+=1
                    self.canvas.create_rectangle(self.room_unit * col + 10, self.room_unit * (row+1) - 2, self.room_unit * col + 65,
                                                 self.room_unit * (row+1) + 2, fill="white", outline="")
                elif key == "west":
                    self.canvas.create_rectangle(self.room_unit * col - 2, self.room_unit * row + 10, self.room_unit * col + 2,
                                                 self.room_unit * row + 65, fill="white", outline="")
                elif key == "east":
                    # col+=1
                    self.canvas.create_rectangle(self.room_unit * (col+1) + 2, self.room_unit * row + 10, self.room_unit * (col+1) - 2,
                                                 self.room_unit * row + 65, fill="white", outline="")

    def draw_pillar(self, pillar, row, col):
        offset = self.room_unit//2
        self.canvas.create_text(self.room_unit * col + offset, self.room_unit * row + offset, text=pillar[0],
                                font="Times 12")

    def draw_exit(self, row, col):
        # for testing, will replace with graphic
        offset = self.room_unit // 2
        self.canvas.create_text(self.room_unit * col + offset, self.room_unit * row + offset, text="Ex",
                                font="Times 12")
    def draw_entrance(self, row, col):
        # for testing, will replace with graphic
        offset = self.room_unit // 2
        self.canvas.create_text(self.room_unit * col + offset, self.room_unit * row + offset, text="En",
                                font="Times 12")