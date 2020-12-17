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

    def start(self):
        """Creates the tkinter window containing the game. Used to delay startup so that changes can be made to
        the dungeon and adventurer for testing specific cases."""
        self.root.mainloop()

    def start_menu_init(self):
        """Builds the start menu for the game. Has a button to start a new game, display instructions and exit the
        program."""
        self.startmenu = Frame(self.root)
        self.startmenu.grid(row=0,column=0)
        menu_spacer = Frame(self.startmenu, height=100, width=600).grid(row=0, column=0)

        title = Label(self.startmenu, text="502 Dungeon Adventure", font="Times 40", pady=50).grid(row=1, column=0)

        new_game_button = Button(self.startmenu, text="New Game", font="Times 20",
                                 command=self.game_init).grid(row=2,column=0)

        instructions_button = Button(self.startmenu, text="Instructions", font="Times 20",
                                     command=self.display_instructions).grid(row=3, column=0)

        exit_button = Button(self.startmenu, text="Exit", font="Times 20",
                             command=self.root.destroy).grid(row=4, column=0)
        menu_spacer2 = Frame(self.startmenu, height=100, width=600).grid(row=5, column=0)

    def display_instructions(self):
        """Displays basic instructions for the game. Hides the start menu and replaces it with a screen containing
        text from a separate text file. Creates a button that will return the user to the start menu."""
        self.startmenu.grid_forget()
        instruction_file = open("dungeon_instruct.txt", 'r')
        instruction_text = instruction_file.read()
        instruct_frame = Frame(self.root, height=600, width=600)
        instruct_frame.grid(row=0,column=0)
        t = Text(instruct_frame, wrap="word", font="Times 16")
        t.grid(row=0, column=0)
        t.insert("1.0", instruction_text)
        instruction_file.close()

        back_button = Button(instruct_frame, text="Back", font="Times 20",
                             command= lambda: self.return_to_start(instruct_frame)).grid(row=1, column=0)

    def return_to_start(self, current):
        """Hides the tkinter object that is passed in and displays the start menu object."""
        current.grid_forget()
        self.startmenu.grid(row=0, column=0)

    def game_init(self):
        """Creates a menu for choosing game settings. Provides an entry for setting an adventurer name and buttons
        for selecting the game difficulty. The default difficulty is easy and buttons are toggled."""
        def set_difficulty(difficulty):
            if difficulty == "Hard":
                dungeon.resize_dungeon(10, 10)
                easy_button["relief"] = "raised"
                medium_button["relief"] = "raised"
                hard_button["relief"] = "sunken"
            elif difficulty == "Medium":
                dungeon.resize_dungeon(7, 7)
                easy_button["relief"] = "raised"
                medium_button["relief"] = "sunken"
                hard_button["relief"] = "raised"
            elif difficulty == "Easy":
                dungeon.resize_dungeon(4, 4)
                easy_button["relief"] = "sunken"
                medium_button["relief"] = "raised"
                hard_button["relief"] = "raised"
            else:
                pass

        dungeon = self.dungeon
        adventurer = self.adventurer
        self.startmenu.grid_forget()
        creation_menu = Frame(self.root)
        creation_menu.grid(row=0, column=0)
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
        confirm_button = Button(creation_menu, text="Confirm", font="Times 16",
                                command=lambda:self.start_game(name_entry.get(), creation_menu))
        confirm_button.grid(row=6, column=0)
        back_button = Button(creation_menu, text="Back", font="Times 16",
                             command=lambda:self.return_to_start(creation_menu))
        back_button.grid(row=6, column=1)


    def start_game(self, name, current_canvas):
        """Checks if an adventurer name was given, if not, creates a popup prompting for a name. If a name is given,
        the creation menu is hidden, the dungeon is generated, and the adventurer is placed at the entrance. The
        main game logic is started by the Main_Game class. Adds the start menu to the window behind the main game
        to allow the game to restart if the main game ends."""
        if name.strip() == "":
            error_window = Toplevel()
            error_window.title("Error")
            message = Label(error_window, text="Please enter a name", font="Times 20").grid(row=0, column=0)
        else:
            current_canvas.grid_forget()
            self.adventurer.name = name
            self.dungeon.generate()
            self.dungeon.visited_rooms.clear()
            self.dungeon.visited_rooms.append(self.dungeon.unique_rooms[0])
            entrance = self.dungeon.unique_rooms[0].position()
            entrance_row, entrance_col = entrance[0], entrance[1]
            self.adventurer.set_location(entrance_row, entrance_col)
            self.startmenu.grid(row=0, column=0)
            main_game = Main_Game(self.root, self.dungeon, self.adventurer)
            main_game.frame.grid(row=0, column=0)


if __name__ == '__main__':
    game = AdventureGUI()
    game.start()