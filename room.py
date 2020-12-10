import random
class Room:

    def __init__(self):
        self.__HealingPotion = False
        self.__VisionPotion = False
        self.__pillars= "No pillar"
        self.__doors = {"north": 0,"south": 0,"east": 0,"west": 0}
        self.__pit = False
        self.__impassable = False
        self.__visited = False
        self.__exit = False
        self.__entrance = False
        self.__MultipleItems = False
        self.__HitPoints = 0
        self.__DamagePoints = 0
        self.__EmptyRoom=False
        self.set_room_type()
        self.set_pillars()
        self.set_doors()
        self.is_empty_room()

    def get_Potion_HitPoint(self):
        return self.__HitPoints


    def __str__(self):
        item_count=0
        if self.__HealingPotion:
            item_count += 1
        if self.__VisionPotion:
            item_count += 1
        if self.__pit:
            item_count += 1
        if self.__pillars!= "No pillar":
            item_count += 1

        if item_count > 1:
            return "M"
        else:
            room_string="H" + str(self.__HealingPotion) + "\n"\
                   + "V" + str(self.__VisionPotion) + "\n"
            if self.__pillars == "A":
                room_string += "A" + str(self.__pillars) + "\n"
            if self.__pillars == "E":
                 room_string += "E" + str(self.__pillars) + "\n"
            if self.__pillars == "I":
                room_string += "I" + str(self.__pillars) + "\n"
            if self.__pillars == "P":
                 room_string += "P" + str(self.__pillars) + "\n"

            room_string+= "X" + str(self.__pit) + "\n" \
            + "O" + str(self.__exit) + "\n" \
            + "i" + str(self.__entrance) + "\n" \
            + "< >" + str(self.__EmptyRoom) + "\n"
            return room_string



    def can_enter(self):
        return not self.__impassable and not self.__visited



    def set_visited(self, visited):
        self.__visited = visited



    def set_room_type(self):
        choice_list=["H","V","O","i","IP","X"]
        room_type= random.choice(choice_list)
        if room_type== "H":
            self.__HealingPotion = True
            self.__HitPoints = random.randint(10, 15)
        elif room_type== "V":
            self.__VisionPotion = True
            self.__HitPoints = random.randint(15, 25)
        elif room_type== "O":
            self.__exit =True
        elif room_type== "i":
            self.__entrance = True
        elif room_type== "IP":
            self.__impassable = True
        else :
            self.set_pit()


    def set_pit(self):
        self.__pit = True
        self.__DamagePoints = random.randint(1,20)

    def set_pillars(self):
        pillars_list = ["A", "E","I","P"]
        room_pillars = random.choice(pillars_list)
        self.__pillars = room_pillars

    def set_doors(self,N=0,S=0,W=0,E=0):
        self.__doors["north"]= N
        self.__doors["south"] = S
        self.__doors["east"] = E
        self.__doors["west"] = W

    def is_empty_room(self):
        if self.__HealingPotion or self.__VisionPotion or self.__pillars=="No pillar" or self.__pit:
            self.__EmptyRoom=False
        else:
            self.__EmptyRoom=True



















