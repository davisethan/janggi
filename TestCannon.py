# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess cannon


import unittest
from Board import Board
from Cannon import BlueCannon, RedCannon
from Chariot import RedChariot, BlueChariot
from General import BlueGeneral, RedGeneral
from Soldier import BlueSoldier, RedSoldier


class TestBlueCannon(unittest.TestCase):
    def test_blue_cannon(self):
        # Given
        cases = [
            {
                "name": "blue_cannon",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueCannon()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4))
                }
            },
            {
                "name": "blue_cannon_jumps",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueCannon(),
                    (2, 4): BlueSoldier(),
                    (4, 6): BlueSoldier(),
                    (6, 4): BlueSoldier(),
                    (4, 2): BlueSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (1, 4): ((4, 4), (1, 4)),
                    (0, 4): ((4, 4), (1, 4), (0, 4)),
                    (4, 7): ((4, 4), (4, 7)),
                    (4, 8): ((4, 4), (4, 7), (4, 8)),
                    (7, 4): ((4, 4), (7, 4)),
                    (8, 4): ((4, 4), (7, 4), (8, 4)),
                    (9, 4): ((4, 4), (7, 4), (8, 4), (9, 4)),
                    (4, 1): ((4, 4), (4, 1)),
                    (4, 0): ((4, 4), (4, 1), (4, 0))
                }
            },
            {
                "name": "blue_cannon_cant_jump_cannon",
                "source": (8, 4),
                "layout": {
                    (8, 4): BlueCannon(),
                    (5, 4): BlueCannon(),
                    (8, 6): RedCannon()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4))
                }
            },
            {
                "name": "blue_cannon_cant_capture_cannon",
                "source": (8, 4),
                "layout": {
                    (8, 4): BlueCannon(),
                    (5, 4): BlueSoldier(),
                    (2, 4): BlueCannon(),
                    (8, 6): RedSoldier(),
                    (8, 7): RedCannon()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4)),
                    (4, 4): ((8, 4), (4, 4)),
                    (3, 4): ((8, 4), (4, 4), (3, 4))
                }
            },
            {
                "name": "blue_cannon_lower_left_corner_palace",
                "source": (9, 3),
                "layout": {
                    (9, 3): BlueCannon(),
                    (8, 4): RedSoldier()
                },
                "expected_destinations": {
                    (9, 3): ((9, 3), (9, 3)),
                    (7, 5): ((9, 3), (7, 5))
                }
            },
            {
                "name": "blue_cannon_upper_left_corner_palace",
                "source": (7, 3),
                "layout": {
                    (7, 3): BlueCannon(),
                    (8, 4): RedSoldier()
                },
                "expected_destinations": {
                    (7, 3): ((7, 3), (7, 3)),
                    (9, 5): ((7, 3), (9, 5))
                }
            },
            {
                "name": "blue_cannon_upper_right_corner_palace",
                "source": (7, 5),
                "layout": {
                    (7, 5): BlueCannon(),
                    (8, 4): RedSoldier()
                },
                "expected_destinations": {
                    (7, 5): ((7, 5), (7, 5)),
                    (9, 3): ((7, 5), (9, 3))
                }
            },
            {
                "name": "blue_cannon_lower_right_corner_palace",
                "source": (9, 5),
                "layout": {
                    (9, 5): BlueCannon(),
                    (8, 4): RedSoldier()
                },
                "expected_destinations": {
                    (9, 5): ((9, 5), (9, 5)),
                    (7, 3): ((9, 5), (7, 3))
                }
            },
            {
                "name": "blue_cannon_makes_generals_face",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueCannon(),
                    (8, 4): BlueGeneral(),
                    (1, 4): RedGeneral(),
                    (4, 2): BlueSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4))
                }
            },
            {
                "name": "blue_cannon_makes_blue_general_check",
                "source": (6, 4),
                "layout": {
                    (6, 4): BlueCannon(),
                    (6, 3): BlueSoldier(),
                    (6, 5): BlueSoldier(),
                    (7, 4): BlueGeneral(),
                    (4, 4): RedChariot()
                },
                "expected_destinations": {
                    (6, 4): ((6, 4), (6, 4))
                }
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                blue_cannon = BlueCannon()
                board = Board(case["layout"])

                # When
                actual_destinations = BlueCannon().destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


class TestRedCannon(unittest.TestCase):
    def test_red_cannon(self):
        # Given
        cases = [
            {
                "name": "red_cannon",
                "source": (4, 4),
                "layout": {
                    (4, 4): RedCannon()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4))
                }
            },
            {
                "name": "red_cannon_jumps",
                "source": (4, 4),
                "layout": {
                    (4, 4): RedCannon(),
                    (2, 4): RedSoldier(),
                    (4, 6): RedSoldier(),
                    (6, 4): RedSoldier(),
                    (4, 2): RedSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (1, 4): ((4, 4), (1, 4)),
                    (0, 4): ((4, 4), (1, 4), (0, 4)),
                    (4, 7): ((4, 4), (4, 7)),
                    (4, 8): ((4, 4), (4, 7), (4, 8)),
                    (7, 4): ((4, 4), (7, 4)),
                    (8, 4): ((4, 4), (7, 4), (8, 4)),
                    (9, 4): ((4, 4), (7, 4), (8, 4), (9, 4)),
                    (4, 1): ((4, 4), (4, 1)),
                    (4, 0): ((4, 4), (4, 1), (4, 0))
                }
            },
            {
                "name": "red_cannon_cant_jump_cannon",
                "source": (8, 4),
                "layout": {
                    (8, 4): RedCannon(),
                    (5, 4): RedCannon(),
                    (8, 6): BlueCannon()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4))
                }
            },
            {
                "name": "red_cannon_cant_capture_cannon",
                "source": (8, 4),
                "layout": {
                    (8, 4): RedCannon(),
                    (5, 4): RedSoldier(),
                    (2, 4): RedCannon(),
                    (8, 6): BlueSoldier(),
                    (8, 7): BlueCannon()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4)),
                    (4, 4): ((8, 4), (4, 4)),
                    (3, 4): ((8, 4), (4, 4), (3, 4))
                }
            },
            {
                "name": "red_cannon_lower_left_corner_palace",
                "source": (9, 3),
                "layout": {
                    (9, 3): RedCannon(),
                    (8, 4): BlueSoldier()
                },
                "expected_destinations": {
                    (9, 3): ((9, 3), (9, 3)),
                    (7, 5): ((9, 3), (7, 5))
                }
            },
            {
                "name": "red_cannon_upper_left_corner_palace",
                "source": (7, 3),
                "layout": {
                    (7, 3): RedCannon(),
                    (8, 4): BlueSoldier()
                },
                "expected_destinations": {
                    (7, 3): ((7, 3), (7, 3)),
                    (9, 5): ((7, 3), (9, 5))
                }
            },
            {
                "name": "red_cannon_upper_right_corner_palace",
                "source": (7, 5),
                "layout": {
                    (7, 5): RedCannon(),
                    (8, 4): BlueSoldier()
                },
                "expected_destinations": {
                    (7, 5): ((7, 5), (7, 5)),
                    (9, 3): ((7, 5), (9, 3))
                }
            },
            {
                "name": "red_cannon_lower_right_corner_palace",
                "source": (9, 5),
                "layout": {
                    (9, 5): RedCannon(),
                    (8, 4): BlueSoldier()
                },
                "expected_destinations": {
                    (9, 5): ((9, 5), (9, 5)),
                    (7, 3): ((9, 5), (7, 3))
                }
            },
            {
                "name": "red_cannon_makes_red_general_check",
                "source": (3, 4),
                "layout": {
                    (3, 4): RedCannon(),
                    (3, 3): RedSoldier(),
                    (3, 5): RedSoldier(),
                    (2, 4): RedGeneral(),
                    (5, 4): BlueChariot()
                },
                "expected_destinations": {
                    (3, 4): ((3, 4), (3, 4))
                }
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_destinations = RedCannon().destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


if __name__ == "__main__":
    unittest.main()
