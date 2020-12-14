from tkinter import Menu, Button, scrolledtext, Frame, Canvas, Toplevel
from dungeondraw import MapDisplay

class Main_Game:
    def __init__(self, root, dungeon, adventurer):
        self.root = root
        self.frame = Frame(self.root)
        self.dungeon = dungeon
        self.adventurer = adventurer
        self.location = self.adventurer.current_location

        self._menu_init()
        self._interface_init()
        self._display_init()

    def display(self):
        return self.frame

    def _menu_init(self):
        menubar = Menu(self.root)
        menubar.add_command(label="Help")
        menubar.add_command(label="Show Map", command=self._show_player_map)
        menubar.add_command(label="Exit")
        if self.adventurer.name == "Tom" or self.adventurer.name == "Kevin":
            menubar.add_command(label="Show Entire Map", command=self._show_entire_map)
        self.root.config(menu=menubar)

    def _show_entire_map(self):
        map_window = Toplevel()
        map_window.title("I hope you're allowed to see this :)")
        drawer = MapDisplay(self.dungeon, map_window)
        entire_map = drawer.draw_entire_map()
        entire_map.pack()

    def _show_player_map(self):
        map_window = Toplevel()
        map_window.title("Map")
        drawer = MapDisplay(self.dungeon, map_window)
        player_map = drawer.draw_player_map(self.adventurer)
        player_map.pack()

    def _interface_init(self):
        self.text_display = scrolledtext.ScrolledText(self.frame, height=5, font="Times 14", wrap="word")
        self.text_display.grid(row=1, column=0, rowspan=3)
        self.text_display.insert("1.0", "Welcome to the 502 Dungeon.\nFind all four pillars to unlock the exit.")
        self.text_display.configure(state="disabled")
        north = Button(self.frame, text="North", command=lambda:self._move_adventurer("north"), pady=5)
        north.grid(row=1, column=2)
        south = Button(self.frame, text="South", command=lambda:self._move_adventurer("south"), pady=5)
        south.grid(row=3, column=2)
        east = Button(self.frame, text="East", command=lambda:self._move_adventurer("east"), pady=5)
        east.grid(row=2, column=1)
        west = Button(self.frame, text="West", command=lambda:self._move_adventurer("west"), pady=5)
        west.grid(row=2, column=3)
        self._set_move_button_state(north, south, east, west)
        player_info = Button(self.frame, text=self.adventurer.name, command=self._show_adventurer_info)
        player_info.grid(row=2, column=2)
        
    def _move_adventurer(self, direction):
        if direction == "north":
            pass
        elif direction =="south":
            pass
        elif direction == "east":
            pass
        elif direction == "west":
            pass

    def _set_move_button_state(self, north, south, east, west):
        row, col = self.location[0], self.location[1]
        if self.dungeon.check_north(row, col):
            north["state"] = "normal"
        else:
            north["state"] = "disabled"
        if self.dungeon.check_south(row, col):
            south["state"] = "normal"
        else:
            south["state"] = "disabled"
        if self.dungeon.check_east(row, col):
            east["state"] = "normal"
        else:
            east["state"] = "disabled"
        if self.dungeon.check_west(row, col):
            west["state"] = "normal"
        else:
            west["state"] = "disabled"

    def _show_adventurer_info(self):
        pass

    def _display_init(self):
        display = Canvas(self.frame, height=900, width=900, bg="white")
        display.grid(row=0, column=0, columnspan=4)
        display.create_rectangle(0,0,100,100, fill="black")
