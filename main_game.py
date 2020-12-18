from tkinter import Menu, Button, scrolledtext, Frame, Canvas, Toplevel, Label
from tkinter.constants import END
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
        self.display = Canvas(self.frame, height=620, width=620, bg="white")
        self.drawer = GameDisplay(self.display, self.dungeon)
        self.drawer.draw()
        self.display.grid(row=0, column=0, columnspan=4)
        self.locate_position()
        self.stats = {"Rooms explored": 0,
                      "Rooms traversed": 0,
                      "Damage taken": 0,
                      "Pits fell in": 0,
                      "Health healed": 0,
                      "Healing potions found": 0,
                      "Vision potions found": 0,
                      "Vision potions used": 0}

    @property
    def frame(self):
        return self._frame

    def locate_position(self):
        """Changes the location to the adventurer's current location and informs the game display object of which room
        to draw."""
        self.location = self.adventurer.current_location
        self.drawer.set_position(self.location)

    def _menu_init(self):
        """Creates the menu bar and contains the methods that the menu options call. Includes the entire map display
        button if the adventurer name is either "Tom" or "Kevin"."""
        def confirm_exit(root):
            """Creates a popup that makes sure the user wishes to exit the program."""
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
            """Prints out the instruction text from the in the text display."""
            instruction_file = open("dungeon_instruct.txt", 'r')
            instruction_text = instruction_file.read()
            text_display.configure(state="normal")
            text_display.insert(END, instruction_text)
            text_display.configure(state="disabled")
            instruction_file.close()

        def show_player_map(dungeon, adventurer):
            """Creates a popup containing the player map created with MapDisplay."""
            map_window = Toplevel()
            map_window.title("Map")
            drawer = MapDisplay(dungeon, map_window)
            player_map = drawer.draw_player_map(adventurer)
            player_map.pack()

        def show_entire_map(dungeon):
            """Creates a popup containing the entire map of the dungeon created with MapDisplay."""
            map_window = Toplevel()
            map_window.title("This should help quite a bit!")
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
        """Creates the interface containing player actions, including movement, using potions and displaying player info."""
        self.text_display = scrolledtext.ScrolledText(self.frame, height=8, font="Times 12", wrap="word")
        self.text_display.grid(row=1, column=0, rowspan=3)
        intro_text = "Welcome to the 502 Dungeon.\nFind all four pillars to unlock the exit.\n"
        self.add_text(intro_text)
        self.north = Button(self.frame, text="North", command=lambda:self._move_adventurer("north"), pady=5)
        self.north.grid(row=1, column=2, columnspan=2)
        self.south = Button(self.frame, text="South", command=lambda:self._move_adventurer("south"), pady=5)
        self.south.grid(row=3, column=2, columnspan=2)
        self.east = Button(self.frame, text="East", command=lambda:self._move_adventurer("east"), pady=5)
        self.east.grid(row=2, column=4)
        self.west = Button(self.frame, text="West", command=lambda:self._move_adventurer("west"), pady=5)
        self.west.grid(row=2, column=1)
        self._set_move_button_state()
        player_info = Button(self.frame, text="Profile", command=self._show_adventurer_info)
        player_info.grid(row=2, column=2, columnspan=2)
        use_health = Button(self.frame, text="Use Health Potion", command=self.use_healing_pot)
        use_health.grid(row=4, column=1, columnspan=2)
        use_vision = Button(self.frame, text="Use Vision Potion", command=self.use_vision_pot)
        use_vision.grid(row=4, column=3, columnspan=2)

    def use_healing_pot(self):
        """Displays text indicating a potion has been used. Calls a method in adventurer to add the health points
        and remove the potion. If the adventurer has no potions, an error will be caught and text will be displayed
        indicating no potions are avaliable."""
        try:
            healing_text = f'You use a healing potion and regain {self.adventurer.healing_potion[0]} health points.\n'
            self.add_text(healing_text)
            self.stats["Health healed"] += self.adventurer.healing_potion[0]
            self.adventurer.use_healing_potion()
        except IndexError:
            no_potion = "You have no healing potions to use!\n"
            self.add_text(no_potion)

    def use_vision_pot(self):
        """If the adventurer has vision potions to use, removes one from adventurer and displays text. Creates a list
        of the adjacent rooms if the rooms exist and add them to the dungeon's list of visited room if the rooms aren't
        already in the list. Then redraws the game display. If the adventurer has no vision potions, the appropriate
        text will be displayed instead."""
        if self.adventurer.vision_potion > 0:
            vision_text = "You use a vision potion and gain knowledge of the adjacent rooms.\n"
            self.add_text(vision_text)
            self.stats["Vision potions used"] += 1
            self.adventurer.use_vision_potion()
            row = self.location[0]
            col = self.location[1]
            adjacent_rooms = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if self.dungeon.in_bounds(row+i, col+j):
                        adjacent_rooms.append(self.dungeon.get_room(row+i, col+j))
            print(adjacent_rooms)
            for room in adjacent_rooms:
                if room not in self.dungeon.visited_rooms:
                    self.dungeon.visited_rooms.append(room)
            self.drawer.draw()
        else:
            no_potion = "You have no vision potions to use!\n"
            self.add_text(no_potion)

    def _move_adventurer(self, direction):
        """Changes the adventurer's location depending on the passed in direction. Conducts the room check then
        changes the drawer's location and redraws the game display. Then resets the move buttons."""
        self.stats["Rooms traversed"] += 1
        if direction == "north":
            self.adventurer.set_location(self.location[0]-1, self.location[1])
        elif direction =="south":
            self.adventurer.set_location(self.location[0]+1, self.location[1])
        elif direction == "east":
            self.adventurer.set_location(self.location[0], self.location[1]+1)
        elif direction == "west":
            self.adventurer.set_location(self.location[0], self.location[1]-1)
        self.locate_position()
        if self.dungeon.get_room(self.location[0], self.location[1]) not in self.dungeon.visited_rooms:
            text = "\nYou cautiously explore a new room."
            self.add_text(text)
        self.check_room()
        self.drawer.draw()
        self._set_move_button_state()

    def check_room(self):
        """If the room has not been visited before, adds it to the dungeon's list of visited rooms. Checks the room for
        pillars, healing potions and vision potions and automatically adds them to the adventurer and removes them
        from the room. Checks if the room contains a pit and removes the health from the adventurer, if health is less
        than 0 afterwards, ends the game with the lost condition. Checks if the room is the exit, if it is, checks if
        the adventurer has all 4 pillars. Without all pillars, a message is displayed and the game continues, if the
        adventurer has all pillars, ends game with the win condition."""
        self.add_text("\n")
        room = self.dungeon.get_room(self.location[0], self.location[1])
        if room not in self.dungeon.visited_rooms:
            self.dungeon.visited_rooms.append(room)
            self.stats["Rooms explored"] += 1
        if room.pit():
            self.adventurer.decrease_hit_points(room.damage_points())
            damage_text = f'You take {room.damage_points()} of damage from falling into a pit! ' \
                          f'You have {self.adventurer.hit_point()}hp left.\n'
            self.add_text(damage_text)
            self.stats["Damage taken"] += room.damage_points()
            self.stats["Pits fell in"] += 1
            if self.adventurer.hit_point() <= 0:
                self.game_over("lost")
        if room.healing_potion():
            potion = room.get_Potion_HitPoint()
            self.adventurer.take_healing_potion(potion)
            room.take_healing_potion()
            healing_pot_text = "You find a healing potion and quickly take it.\n"
            self.add_text(healing_pot_text)
            self.stats["Healing potions found"] += 1
        if room.vision_potion():
            self.adventurer.take_vision_potion()
            room.take_vision_potion()
            vision_pot_text = "You find a vision potion, this will come in handy!\n"
            self.add_text(vision_pot_text)
            self.stats["Vision potions used"] += 1
        if room.pillar():
            pillar = room.pillar()
            self.adventurer.take_pillar(pillar)
            room.take_pillar()
            pillar_text = f'You find the physical embodiment of the concept of {pillar}. When you touch the pillar,' \
                          f' it disappears and you feel slighly better at programming.\n'
            self.add_text(pillar_text)
        if room.exit():
            if self.adventurer.has_all_pillars():
                self.game_over("win")
            else:
                more_pillars_text = "You do not have all the pillars needed to open the exit, keep on looking!"
                self.add_text(more_pillars_text)

    def _set_move_button_state(self):
        """Sets the state of the movement buttons depending on if the adjacent rooms can be reached from the current
        room or not."""
        row, col = self.location[0], self.location[1]
        if self.dungeon.check_north(row, col):
            self.north["state"] = "normal"
        else:
            self.north["state"] = "disabled"
        if self.dungeon.check_south(row, col):
            self.south["state"] = "normal"
        else:
            self.south["state"] = "disabled"
        if self.dungeon.check_east(row, col):
            self.east["state"] = "normal"
        else:
            self.east["state"] = "disabled"
        if self.dungeon.check_west(row, col):
            self.west["state"] = "normal"
        else:
            self.west["state"] = "disabled"

    def _show_adventurer_info(self):
        """Creates a popup that displays the adventurer's name, current health, vision potions, healing potions,
        and pillars."""
        player_info = Toplevel()
        player_info.title(self.adventurer.name)
        hp = Label(player_info, text="Health:", font="Times 16").grid(row=0, column=0, rowspan=2)
        total_hp_bar = Label(player_info, bg="white", padx=100).grid(row=1, column=1)
        actual_hp_bar = Label(player_info, bg="red", padx=self.adventurer.hit_point()).grid(row=1, column=1)
        hp_text = Label(player_info, text=f'{self.adventurer.hit_point()}/100', font="Times 12").grid(row=0, column=1)
        potions = Label(player_info, text="Potions:", font="Times 16").grid(row=2, column=0)
        potion_text = f'{self.adventurer.vision_potion} Vision Potion(s)\n'
        if len(self.adventurer.healing_potion) == 0:
            potion_text += "0 Health Potions"
        else:
            for potion in self.adventurer.healing_potion:
                potion_text += f'Health Potion({potion}hp)\n'
        potion_list = Label(player_info, text=potion_text, font="Times 14").grid(row=3, column=1)
        pillars = Label(player_info, text="Pillars:", font="Times 16").grid(row=4, column=0)
        pillar_text = ""
        for pillar in self.adventurer.pillars:
            pillar_text += f'{pillar}\n'
        pillar_list = Label(player_info, text=pillar_text, font="Times 14").grid(row=5, column=1)

    def add_text(self, string):
        """Helper function for displaying text in the text display. The state needs to be set to normal to add text and
        set to diabled afterwards to prevent the player from entering their own text."""
        self.text_display.configure(state="normal")
        self.text_display.insert(END, string)
        self.text_display.configure(state="disabled")
        self.text_display.see(END)

    def game_over(self, condition):
        """Creates a popup with a replay and exit button. If the game ends in a lost, a consolation message is displayed,
        if the game ends in a win, a congratulation message and an image of the entire dungeon is displayed."""
        def close_game(root):
            root.destroy()
        def replay_game(current):
            end.destroy()
            current.destroy()
        end = Toplevel()
        replay = Button(end, text="Replay", font="Times 16", command=lambda:replay_game(self.frame))
        replay.grid(row=3, column=1)
        exit = Button(end, text="Exit", font="Times 16", command=lambda:close_game(self.root))
        exit.grid(row=3, column=2)
        stats_text = "STATS\n"
        for key, item in self.stats.items():
            stats_text += f'{key}: {item}\n'
        stats = Label(end, text=stats_text, font="Times 14")
        stats.grid(row=1, column=1, columnspan=2)
        if condition == "lost":
            end.title("GAME OVER")
            text = Label(end, font="Times 20",
                         text="You've lost all of your health and lose conciousness.\nBetter luck next time.")
            self.frame.grid_forget()
        else:
            end.title("CONGRATULATIONS")
            text = Label(end, font="Times 20",
                         text="You've sucessfully escaped the dungeon!\nFeel free to try again on a higher difficulty.")
            drawer = MapDisplay(self.dungeon, end)
            entire_map = drawer.draw_entire_map()
            entire_map.grid(row=0, column=1, columnspan=2)
        text.grid(row=2, column=0, columnspan=4)
