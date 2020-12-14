from dungeon import Dungeon
from adventurer import Adventurer
from main_game import Main_Game
from tkinter import Tk, Frame, Button, Label, Canvas, Text, Entry, Toplevel

class AdventureGUI:
    def __init__(self):
        self.dungeon = Dungeon(4, 4)
        self.dungeon.generate()
        self.adventurer = Adventurer("")

        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title("Dungeon Adventure")
        self.start_menu_init()
        self.root.mainloop()

    def start_menu_init(self):

        self.startmenu = Frame(self.root)
        self.startmenu.pack()
        menu_spacer = Frame(self.startmenu, height=100, width=600).pack()

        title = Label(self.startmenu, text="502 Dungeon Adventure", font="Times 40", pady=50).pack()

        new_game_button = Button(self.startmenu, text="New Game", font="Times 20", command=self.game_init).pack()

        instructions_button = Button(self.startmenu, text="Instructions", font="Times 20",
                                     command=self.display_instructions).pack()

        exit_button = Button(self.startmenu, text="Exit", font="Times 20", command=self.root.destroy).pack()
        menu_spacer2 = Frame(self.startmenu, height=100, width=600).pack()


    def display_instructions(self):
        self.startmenu.pack_forget()
        instruction_file = open("dungeon_instruct.txt", 'r')
        instruction_text = instruction_file.read()
        instruct_frame = Frame(self.root, height=600, width=600)
        instruct_frame.pack()
        t = Text(instruct_frame, wrap="word", font="Times 16")
        t.pack()
        t.insert("1.0", instruction_text)
        instruction_file.close()

        back_button = Button(instruct_frame, text="Back", font="Times 20",
                             command= lambda: self.return_to_start(instruct_frame)).pack()

    def return_to_start(self, current):
        current.pack_forget()
        self.startmenu.pack()

    def game_init(self):
        def set_difficulty(difficulty):
            if difficulty == "Hard":
                dungeon.resize_dungeon(10, 10)
                # set adventurer.hp
                easy_button["relief"] = "raised"
                medium_button["relief"] = "raised"
                hard_button["relief"] = "sunken"
            elif difficulty == "Medium":
                dungeon.resize_dungeon(7, 7)
                # set adventurer.hp
                easy_button["relief"] = "raised"
                medium_button["relief"] = "sunken"
                hard_button["relief"] = "raised"
            elif difficulty == "Easy":
                dungeon.resize_dungeon(4, 4)
                # set adventurer.hp
                easy_button["relief"] = "sunken"
                medium_button["relief"] = "raised"
                hard_button["relief"] = "raised"
            else:
                pass

        dungeon = self.dungeon
        adventurer = self.adventurer
        self.startmenu.pack_forget()
        creation_menu = Frame(self.root)
        creation_menu.pack()
        new_name = Label(creation_menu, text="Adventurer Name: ", font="Times 14")
        new_name.grid(row=0, column=0, columnspan=2)
        name_entry = Entry(creation_menu, width=40)
        name_entry.grid(row=0, column=2)
        difficulty = Label(creation_menu, text="Choose difficulty:", font="Times 14")
        difficulty.grid(row=1, column=0, columnspan=2)
        hard_button = Button(creation_menu, text="Hard", command=lambda:set_difficulty("Hard"))
        hard_button.grid(row=2, column=2)
        medium_button = Button(creation_menu, text="Medium", command=lambda:set_difficulty("Medium"))
        medium_button.grid(row=3, column=2)
        easy_button = Button(creation_menu, text="Easy", relief="sunken", command=lambda:set_difficulty("Easy"))
        easy_button.grid(row=4, column=2)
        custom = Button(creation_menu, text="Custom", command=lambda:set_difficulty("Custom"))
        # custom.grid(row=5, column=2)
        confirm_button = Button(creation_menu, text="Confirm", font="Times 16",
                                command=lambda:self.start_game(name_entry.get(), creation_menu))
        confirm_button.grid(row=6, column=0)
        back_button = Button(creation_menu, text="Back", font="Times 16",
                             command=lambda:self.return_to_start(creation_menu))
        back_button.grid(row=6, column=1)


    def start_game(self, name, current_canvas):

        if name.strip() == "":
            error_window = Toplevel()
            error_window.title("Error")
            message = Label(error_window, text="Please enter a name", font="Times 20").pack()

        else:
            current_canvas.pack_forget()
            self.adventurer.name = name
            self.dungeon.generate()
            self.dungeon.visited_rooms.clear()
            self.dungeon.visited_rooms.append(self.dungeon.unique_rooms[0])
            entrance = self.dungeon.unique_rooms[0].position()
            entrance_row, entrance_col = entrance[0], entrance[1]
            self.adventurer.set_location(entrance_row, entrance_col)
            # start main game logic
            main_game = Main_Game(self.root, self.dungeon, self.adventurer)
            main_game.display().grid(row=0, column=0)





if __name__ == '__main__':
    game = AdventureGUI()