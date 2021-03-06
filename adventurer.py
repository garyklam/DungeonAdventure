import random
from room import Room


class Adventurer:
    def __init__(self, name: str):
        self.name = name
        self._hit_point = random.randint(75, 100)
        self.healing_potion = []
        self.vision_potion = 0
        self.pillars = []
        self._current_location = (0,0)

    @property
    def current_location(self):
        return self._current_location

    def set_location(self, row, col):
        self._current_location = (row, col)

    def hit_point(self):
        return self._hit_point

    def take_healing_potion(self, potion):
        self.healing_potion.append(potion)

    def take_vision_potion(self):
        self.vision_potion += 1

    def take_pillar(self, pillar):
        self.pillars.append(pillar)

    def decrease_hit_points(self, points):
        self._hit_point -= points
        # if self._hit_point < 0:
        #     need to discuss how to show the message
            # print('You lose')

    def use_healing_potion(self):
        if len(self.healing_potion) > 0:
            self._hit_point += self.healing_potion.pop(0)
        if self._hit_point > 100:
            self._hit_point = 100

    def use_vision_potion(self):
        self.vision_potion = self.vision_potion - 1
        # added print_surroundings in dungeon as it's unable to do it in

    def enter_room(self, room):
        if room.get_Potion_HitPoint():
            self.healing_potion.append(room.hit_points())
            room.take_healing_potion()

        if room.vision_potion():
            self.vision_potion = self.vision_potion + 1
            room.take_vision_potion()

        if room.pit():
            self.decrease_hit_points(room.damage_points())

        if room.exit():
            if self.has_all_pillars():
                # need to discuss how to show the message
                print('You win')

    def has_all_pillars(self):
        pillars = ("Abstraction", "Encapsulation", "Inheritance", "Polymorphism")
        # if self.pillars != 4:
        #     return False

        for pillar in pillars:
            if pillar not in self.pillars:
                return False
        return True

    def __str__(self):
        return "%s hit point: %s, healing potion: %s, vision potion: %s, pillars: %s" % (
            self.name, self.hit_point, self.healing_potion, self.vision_potion, self.pillars)
