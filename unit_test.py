import unittest

from adventurer import Adventurer
from dungeon import Dungeon
from room import Room


class UnitTests(unittest.TestCase):
    ##############################################################################
    ##*******************test dungeon functionality*******************############
    ##############################################################################

    def test_dungeon_small_size(self):
        try:
            dungeon = Dungeon(2, 2)
            self.assertEqual(True, False, "exception not thrown for invalid argument")
        except ValueError:
            self.assertEqual(True, True)

    def test_dungeon_proper_size(self):
        try:
            dungeon = Dungeon(4, 4)
            self.assertEqual(True, True)
        except ValueError:
            self.assertEqual(True, False, "exception not thrown for invalid argument")

    def test_dungeon_big_size(self):
        try:
            dungeon = Dungeon(20, 20)
            self.assertEqual(True, False, "exception not thrown for invalid argument")
        except ValueError:
            self.assertEqual(True, True)

    def test_dungeon_get_rooms(self):
        dungeon = Dungeon(4, 4)
        dungeon.generate()
        room = dungeon.get_room(3, 3)
        self.assertTrue(dungeon.grid[3][3] == room)

    def test_dungeon_resize(self):
        dungeon = Dungeon(4, 4)
        dungeon.resize_dungeon(3, 3)
        self.assertTrue(dungeon.rows == 3)

    def test_dungeon_in_bound(self):
        dungeon = Dungeon(4, 4)
        is_in_bound = dungeon.in_bounds(3, 0)
        self.assertTrue(is_in_bound)

    def test_dungeon_out_bound(self):
        dungeon = Dungeon(4, 4)

        is_in_bound = dungeon.in_bounds(5, 5)
        self.assertFalse(is_in_bound)
        #self.assertEqual(is_in_bound, False)



    ##############################################################################
    #####*******************test room functionality*******************############
    ##############################################################################



    def test_room_set_exit(self):
        room = Room(3, 3)
        room.set_exit()
        self.assertTrue(room.exit())

    def test_room_set_entrance(self):
        room = Room(3, 3)
        entrance = room.set_entrance()
        self.assertTrue(room.entrance())

    def test_room_get_hit_point(self):
        room = Room(3, 3)
        hit_pont = room.hit_points()
        self.assertEqual(hit_pont, 0)

    def test_room_vision_potion(self):
        room = Room(3, 3)
        self.assertFalse(room.vision_potion())

    def test_room_take_vision_potion(self):
        room = Room(3, 3)
        room.take_vision_potion()
        self.assertFalse(room.vision_potion())

    def test_room_take_healing_potion(self):
        room = Room(3, 3)
        room.take_healing_potion()
        self.assertEqual(room.hit_points(), 0)

    def test_room_pillar(self):
        room = Room(3, 3)
        pillars = room.pillar()
        self.assertEqual(pillars, None)

    def test_room_set_pillar(self):
        room = Room(3, 3)
        room.set_pillar("P")
        self.assertEqual(room.pillar(), "P")

    def test_room_damage_points(self):
        room = Room(3, 3)
        self.assertEqual(room.damage_points(), 0)

    def test_get_Potion_HitPoint(self):
        room = Room(3, 3)
        self.assertEqual(room.get_Potion_HitPoint(), 0)

    def test_set_north_border(self):
        room = Room(3, 3)
        room.set_north_border()
        doors = room.doors()
        self.assertEqual(doors["north"], 0)

    def test_set_south_border(self):
        room = Room(3, 3)
        room.set_south_border()
        doors = room.doors()
        self.assertEqual(doors["south"], 0)

    def test_set_east_border(self):
        room = Room(3, 3)
        room.set_east_border()
        doors = room.doors()
        self.assertEqual(doors["east"], 0)

    def test_set_west_border(self):
        room = Room(3, 3)
        room.set_west_border()
        doors = room.doors()
        self.assertEqual(doors["west"], 0)

    ##############################################################################
    ##*******************test adventurer functionality*******************#########
    ##############################################################################

    def test_adventurer_current_location(self):
        player = Adventurer("player")
        player_location = player.current_location
        self.assertEqual(player_location, (0, 0))

    def test_adventurer_set_location(self):
        player = Adventurer("player")
        player.set_location(1, 2)
        self.assertEqual(player.current_location, (1, 2))

    def test_adventurer_decrease_hit_points(self):
        player = Adventurer("player")
        hit_point = player.hit_point()
        player.decrease_hit_points(5)
        decrease_hit_points = hit_point - 5
        self.assertEqual(player.hit_point(), decrease_hit_points)

    def test_adventurer_use_healing_potion(self):
        player = Adventurer("player")
        hit_point = player.hit_point()
        player.use_healing_potion()
        self.assertEqual(player.hit_point(), hit_point)

    def test_adventurer_has_all_pillars(self):
        player = Adventurer("player")
        self.assertFalse(player.has_all_pillars())






















