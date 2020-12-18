EC: There are unit tests for methods in room, adventurer, and dungeon. The main game is implemented graphically as well.

Group members: Pragati Dode, Gary Lam, Wenqian Li

Time spent:
	Pragati: 
	Gary: 30 hrs
	Wenqian:40 hrs

Project work
	Pragati:
	Gary: dungeon, adventureGUI
	Wenqian: adventurer, unit test

Shortcomings of the program:
There are two different classes in dungeondraw.py that are used to draw the maps and the game display. The two 
classes have very similar methods and could be combined into a single class with different scaling factors, but the
mathematics of actually implementing this solution ended up being too time consuming/buggy and was abandoned.
There are unused fields/methods in a couple of classes that came from a lack of a cohesive plan when the project 
was started. 


Questions:
1. In this program, many methods use random.randint() to produce random room(row, col). How to test these method?

Other info:
To start the game, run adventurerGUI.py, which has the lines for starting the game in main.
Entering "Tom" or "Kevin" as the adventurer name will enable a menu option that displays the entire map. This menu
will remain enabled until the window is closed.
