# room provides basic functionality for dungeon by giving all features required for room in dungeon.

import random

class Room:

    def __init__(self, row, column):
        self.__position = (row, column)      #gives location of adventurer.
        self.__doors = {"north": random.randint(0, 4),#select random value fron o to 4 and accordingly door value will be ie open/close.
                        "south": random.randint(0, 4),
                        "east": random.randint(0, 4),
                        "west": random.randint(0, 4)
                        }
        self.__HealingPotion = False
        self.__VisionPotion = False
        self.__pillar = None
        self.__pit = False
        self.__exit = False
        self.__entrance = False
        self.__MultipleItems = False
        self.__HitPoints = 0
        self.__DamagePoints = 0
        self.__EmptyRoom = False
        self.__impassable = False
        self.set_room_type()

    def doors(self):
        return self.__doors

    def set_exit(self):  # set room as exit room .
        self.__exit = True
        self.clear_room()

    def set_entrance(self):   # set room as entrance room.
        self.__entrance = True
        self.clear_room()

    def clear_room(self):    #take care of exit/entrance room should not contain anything else.
        self.__HealingPotion = False
        self.__VisionPotion = False
        self.__pit = False
        self.__MultipleItems = False
        self.__HitPoints = 0
        self.__DamagePoints = 0

    def position(self):  # gives location.
        return self.__position

    def healing_potion(self):
        return self.__HealingPotion

    def vision_potion(self):
        return self.__VisionPotion

    def pit(self):
        return self.__pit

    def entrance(self):
        return self.__entrance

    def pillar(self):
        return self.__pillar

    def exit(self):
        return self.__exit

    def hit_points(self):
        return self.__HitPoints

    def damage_points(self):
        return self.__DamagePoints

    def take_healing_potion(self):
        self.__HealingPotion = False
        self.__HitPoints = 0

    def take_vision_potion(self):
        self.__VisionPotion = False

    def get_Potion_HitPoint(self):
        return self.__HitPoints

    def take_pillar(self):
        self.__pillar = None

    def __str__(self):
        item_count = 0
        if self.__HealingPotion:
            item_count += 1
        if self.__VisionPotion:
            item_count += 1
        if self.__pit:
            item_count += 1
        if self.__pillar is not None:
            item_count += 1

        if item_count > 1:
            return "M"
        else:
            room_string = "H" + str(self.__HealingPotion) + "\n" \
                          + "V" + str(self.__VisionPotion) + "\n"
            if self.__pillar == "A":
                room_string += "A" + str(self.__pillar) + "\n"
            if self.__pillar == "E":
                room_string += "E" + str(self.__pillar) + "\n"
            if self.__pillar == "I":
                room_string += "I" + str(self.__pillar) + "\n"
            if self.__pillar == "P":
                room_string += "P" + str(self.__pillar) + "\n"

            room_string += "X" + str(self.__pit) + "\n" \
                           + "O" + str(self.__exit) + "\n" \
                           + "i" + str(self.__entrance) + "\n" \
                           + "< >" + str(self.__EmptyRoom) + "\n"
            if self.__doors["north"] > 2:       #if random value is grater than 2 door open.
                room_string += "north door: Yes"
            else:
                room_string += "north door: No"
            if self.__doors["south"] > 2:
                room_string += "south door: Yes"
            else:
                room_string += "south door: No"
            if self.__doors["east"] > 2:
                room_string += "east door: Yes"
            else:
                room_string += "east door: No"
            if self.__doors["west"] > 2:
                room_string += "west door: Yes"
            else:
                room_string += "west door: No"
            return room_string

    def set_room_type(self):  #set room type according the things present in room.
            choice_list = ["H", "V", "P", "H+V", "H+P", "V+P", "H+V+P", "E"]
            choice_weight = [10, 5, 6, 2, 4, 2, 1, 30]
            room_type = random.choices(choice_list, choice_weight).pop()
            if room_type == "H":
                self.set_healing_potion()
            elif room_type == "V":
                self.__VisionPotion = True
            elif room_type == "P":
                self.set_pit()
            elif room_type == "H+V":
                self.set_healing_potion()
                self.__VisionPotion = True
            elif room_type == "H+P":
                self.set_healing_potion()
                self.set_pit()
            elif room_type == "V+P":
                self.__VisionPotion = True
                self.set_pit()
            elif room_type == "H+V+P":
                self.set_healing_potion()
                self.__VisionPotion = True
                self.set_pit()
            else:
                pass

    def set_healing_potion(self):
        self.__HealingPotion = True
        self.__HitPoints = random.randint(10, 15)

    def set_pit(self):
        self.__pit = True
        self.__DamagePoints = random.randint(1, 20)

    def set_pillar(self, pillar):
        self.__pillar = pillar

    def is_empty_room(self):
        if self.__HealingPotion or self.__VisionPotion or self.__pillar is not None or self.__pit:
            self.__EmptyRoom = False  #if one of above present room is not empty.
        else:
            self.__EmptyRoom = True

    def set_north_border(self):   #take cares of no door codition on north border.
        self.__doors["north"] = 0

    def set_south_border(self):
        self.__doors["south"] = 0

    def set_east_border(self):
        self.__doors["east"] = 0

    def set_west_border(self):
        self.__doors["west"] = 0

