from tkinter import Menu, Button, scrolledtext, Frame, Canvas, Toplevel, Label
from dungeondraw import MapDisplay, GameDisplay

class Main_Game:
    def __init__(self, root, dungeon, adventurer):
        self.root = root
        self._frame = Frame(self.root)
        self.dungeon = dungeon
        self.adventurer = adventurer
        self.location = self.adventurer.current_location

        self._menu_init()
        self._interface_init()
        self._display_init()

    @property
    def frame(self):
        return self._frame

    def _menu_init(self):
        def confirm_exit(root):
            def close():
                root.destroy()
            def back():
                warning.destroy()
            warning = Toplevel()
            warning_text = Label(warning, font="Times 16", pady=10, text="Are you sure you wish to exit? \n"
                                                                "Progress in the dungeon will not be saved")
            warning_text.grid(row=0, column=0, columnspan=4)
            ok_button = Button(warning, text="Ok", command=close).grid(row=1, column=1)
            back_button = Button(warning, text="Back", command=back).grid(row=1, column=2)

        def insert_help_text(text_display):
            instruction_file = open("dungeon_instruct.txt", 'r')
            instruction_text = instruction_file.read()
            text_display.configure(state="normal")
            text_display.insert("insert", instruction_text)
            text_display.configure(state="disabled")
            instruction_file.close()

        def show_player_map(dungeon, adventurer):
            map_window = Toplevel()
            map_window.title("Map")
            drawer = MapDisplay(dungeon, map_window)
            player_map = drawer.draw_player_map(adventurer)
            player_map.pack()

        def show_entire_map(dungeon):
            map_window = Toplevel()
            map_window.title("I hope you're allowed to see this :)")
            drawer = MapDisplay(dungeon, map_window)
            entire_map = drawer.draw_entire_map()
            entire_map.pack()

        menubar = Menu(self.root)
        menubar.add_command(label="Help", command=lambda:insert_help_text(self.text_display))
        menubar.add_command(label="Show Map", command=lambda:show_player_map(self.dungeon, self.adventurer))
        menubar.add_command(label="Exit", command=lambda:confirm_exit(self.root))
        if self.adventurer.name == "Tom" or self.adventurer.name == "Kevin":
            menubar.add_command(label="Show Entire Map", command=lambda:show_entire_map(self.dungeon))
        self.root.config(menu=menubar)

    def _interface_init(self):
        self.text_display = scrolledtext.ScrolledText(self.frame, height=10, font="Times 14", wrap="word")
        self.text_display.grid(row=1, column=0, rowspan=3)
        self.text_display.insert("1.0", "Welcome to the 502 Dungeon.\nFind all four pillars to unlock the exit.")
        self.text_display.configure(state="disabled")
        north = Button(self.frame, text="North", command=lambda:self._move_adventurer("north"), pady=5)
        north.grid(row=1, column=2, columnspan=2)
        south = Button(self.frame, text="South", command=lambda:self._move_adventurer("south"), pady=5)
        south.grid(row=3, column=2, columnspan=2)
        east = Button(self.frame, text="East", command=lambda:self._move_adventurer("east"), pady=5)
        east.grid(row=2, column=4)
        west = Button(self.frame, text="West", command=lambda:self._move_adventurer("west"), pady=5)
        west.grid(row=2, column=1)
        self._set_move_button_state(north, south, east, west)
        player_info = Button(self.frame, text="Profile", command=self._show_adventurer_info)
        player_info.grid(row=2, column=2, columnspan=2)
        use_health = Button(self.frame, text="Use Health Potion")
        use_health.grid(row=4, column=1, columnspan=2)
        use_vision = Button(self.frame, text="Use Vision Potion")
        use_vision.grid(row=4, column=3, columnspan=2)
        
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
        player_info = Toplevel()
        player_info.title(self.adventurer.name)
        hp = Label(player_info, text="Health:", font="Times 16").grid(row=0, column=0, rowspan=2)
        total_hp_bar = Label(player_info, bg="white", padx=100).grid(row=1, column=1)
        actual_hp_bar = Label(player_info, bg="red", padx=self.adventurer.hit_point).grid(row=1, column=1)
        hp_text = Label(player_info, text=f'{self.adventurer.hit_point}/100', font="Times 12").grid(row=0, column=1)
        potions = Label(player_info, text="Potions:", font="Times 16").grid(row=2, column=0)
        potion_text = f'{self.adventurer.vision_potion} Vision Potion(s)\n'
        if len(self.adventurer.healing_potion) == 0:
            potion_text += "0 Health Potions"
        else:
            for potion in self.adventurer.healing_potion:
                potion_text += f'Health Potion({potion})\n'
        potion_list = Label(player_info, text=potion_text, font="Times 14").grid(row=3, column=1)
        pillars = Label(player_info, text="Pillars:", font="Times 16").grid(row=4, column=0)
        pillar_text = ""
        for pillar in self.adventurer.pillars:
            pillar_text += f'{pillar}\n'
        pillar_list = Label(player_info, text=pillar_text, font="Times 14").grid(row=5, column=1)

    def _display_init(self):
        self.display = Canvas(self.frame, height=900, width=900, bg="white")
        # drawer = GameDisplay(self.display, self.dungeon, self.adventurer)
        # drawer.draw()
        self.display.grid(row=0, column=0, columnspan=4)

