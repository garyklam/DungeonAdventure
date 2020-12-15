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
        self.__exit = False
        self.__entrance = False
        self.__MultipleItems = False
        self.__HitPoints = 0
        self.__DamagePoints = 0
        self.__EmptyRoom = False
        self.set_room_type()

    def doors(self):
        return self.__doors

    def set_exit(self):
        self.__exit = True
        self.clear_room()

    def set_entrance(self):
        self.__entrance = True
        self.clear_room()

    def clear_room(self):
        self.__HealingPotion = False
        self.__VisionPotion = False
        self.__pit = False
        self.__MultipleItems = False
        self.__HitPoints = 0
        self.__DamagePoints = 0

    def position(self):
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
            return room_string

    def set_room_type(self):
        # choice_list = ["H", "V", "O", "i", "IP", "X"]
        room_type = random.randint(1,101)
        if room_type%10 == 0:
            self.__HealingPotion = True
            self.__HitPoints = random.randint(10, 15)
        if room_type%15== 0:
            self.__VisionPotion = True
        if room_type%7 == 0:
            self.set_pit()
        # elif room_type == "O":
        #     self.__exit = True
        # elif room_type == "i":
        #     self.__entrance = True
        # elif room_type == "IP":
        #     self.__impassable = True

    def set_pit(self):
        self.__pit = True
        self.__DamagePoints = random.randint(1, 20)

    def set_pillar(self, pillar):
        self.__pillar = pillar

    def is_empty_room(self):
        if self.__HealingPotion or self.__VisionPotion or self.__pillar is not None or self.__pit:
            self.__EmptyRoom = False
        else:
            self.__EmptyRoom = True

    def set_north_border(self):
        self.__doors["north"] = 0

    def set_south_border(self):
        self.__doors["south"] = 0

    def set_east_border(self):
        self.__doors["east"] = 0

    def set_west_border(self):
        self.__doors["west"] = 0

