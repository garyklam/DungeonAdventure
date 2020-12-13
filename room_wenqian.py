import random


class Room:

    def __init__(self, row, column):
        self.__position = (row, column)
        self.__doors = {"north": random.randint(0, 4),
                        "south": random.randint(0, 4),
                        "east": random.randint(0, 4),
                        "west": random.randint(0, 4)
                        }
        self.__HealingPotion = False
        self.__VisionPotion = False
        self.__pillar = None
        self.__pit = False
        self.__impassable = False
        self.__visited = False
        self.__exit = False
        self.__entrance = False
        self.__MultipleItems = False
        self.__HitPoints = 0
        self.__DamagePoints = 0
        self.__EmptyRoom = False
        self.set_room_type()

    def doors(self):
        return self.__doors

    def set_north_door(self, value):
        self.__doors['north'] = value

    def set_south_door(self, value):
        self.__doors['south'] = value

    def set_east_door(self, value):
        self.__doors['east'] = value

    def set_west_door(self, value):
        self.__doors['west'] = value

    def north_door(self):
        return self.__doors['north']

    def south_door(self):
        return self.__doors['south']

    def east_door(self):
        return self.__doors['east']

    def west_door(self):
        return self.__doors['west']

    def set_exit(self):
        self.__exit = True

    def set_entrance(self):
        self.__entrance = True

    def position(self):
        return self.__position

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

    def unset_healing_potion(self):
        self.__HealingPotion = False
        self.__HitPoints = 0

    def unset_vision_potion(self):
        self.__VisionPotion = False

    def get_Potion_HitPoint(self):
        return self.__HitPoints

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
            return room_string

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def set_visited(self, visited):
        self.__visited = visited

    def set_room_type(self):
        choice_list = ["H", "V", "O", "i", "IP", "X"]
        room_type = random.choice(choice_list)
        if room_type == "H":
            self.__HealingPotion = True
            self.__HitPoints = random.randint(10, 15)
        elif room_type == "V":
            self.__VisionPotion = True
            self.__HitPoints = random.randint(15, 25)
        elif room_type == "O":
            self.__exit = True
        elif room_type == "i":
            self.__entrance = True
        elif room_type == "IP":
            self.__impassable = True
        else:
            self.set_pit()

    def set_pit(self):
        self.__pit = True
        self.__DamagePoints = random.randint(1, 20)

    def set_pillar(self, pillar):
        self.__pillar = pillar

    def set_doors(self, N=0, S=0, W=0, E=0):
        self.__doors["north"] = N
        self.__doors["south"] = S
        self.__doors["east"] = E
        self.__doors["west"] = W

    def is_empty_room(self):
        if self.__HealingPotion or self.__VisionPotion or self.__pillar is not None or self.__pit:
            self.__EmptyRoom = False
        else:
            self.__EmptyRoom = True
