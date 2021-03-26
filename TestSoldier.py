# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess soldier


import unittest
from Board import Board
from Chariot import RedChariot, BlueChariot
from General import BlueGeneral, RedGeneral
from Soldier import BlueSoldier, RedSoldier


class TestBlueSoldier(unittest.TestCase):
    def test_blue_soldier(self):
        # Given
        cases = [
            {
                "name": "blue_soldier",
                "source": (6, 4),
                "layout": {
                    (6, 4): BlueSoldier()
                },
                "expected_destinations": {
                    (6, 4): ((6, 4), (6, 4)),
                    (6, 3): ((6, 4), (6, 3)),
                    (5, 4): ((6, 4), (5, 4)),
                    (6, 5): ((6, 4), (6, 5))
                }
            },
            {
                "name": "blue_soldier_lower_left_red_palace",
                "source": (2, 3),
                "layout": {
                    (2, 3): BlueSoldier()
                },
                "expected_destinations": {
                    (2, 3): ((2, 3), (2, 3)),
                    (2, 2): ((2, 3), (2, 2)),
                    (1, 3): ((2, 3), (1, 3)),
                    (2, 4): ((2, 3), (2, 4)),
                    (1, 4): ((2, 3), (1, 4))
                }
            },
            {
                "name": "blue_solider_lower_right_red_palace",
                "source": (2, 5),
                "layout": {
                    (2, 5): BlueSoldier()
                },
                "expected_destinations": {
                    (2, 5): ((2, 5), (2, 5)),
                    (2, 4): ((2, 5), (2, 4)),
                    (1, 5): ((2, 5), (1, 5)),
                    (2, 6): ((2, 5), (2, 6)),
                    (1, 4): ((2, 5), (1, 4))
                }
            },
            {
                "name": "blue_soldier_center_red_palace",
                "source": (1, 4),
                "layout": {
                    (1, 4): BlueSoldier()
                },
                "expected_destinations": {
                    (1, 4): ((1, 4), (1, 4)),
                    (1, 3): ((1, 4), (1, 3)),
                    (0, 4): ((1, 4), (0, 4)),
                    (1, 5): ((1, 4), (1, 5)),
                    (0, 3): ((1, 4), (0, 3)),
                    (0, 5): ((1, 4), (0, 5))
                }
            },
            {
                "name": "blue_soldier_makes_blue_general_check",
                "source": (6, 4),
                "layout": {
                    (6, 4): BlueSoldier(),
                    (7, 4): BlueGeneral(),
                    (5, 4): RedChariot()
                },
                "expected_destinations": {
                    (6, 4): ((6, 4), (6, 4)),
                    (5, 4): ((6, 4), (5, 4))
                }
            }
        ]
        for case in cases:
            # Given
            blue_soldier = BlueSoldier()
            board = Board(case["layout"])

            # When
            actual_destinations = blue_soldier.destinations_from_source(case["source"], board)

            # Then
            self.assertEqual(case["expected_destinations"], actual_destinations)


class TestRedSoldier(unittest.TestCase):
    def test_red_soldier(self):
        # Given
        cases = [
            {
                "name": "red_soldier",
                "source": (3, 4),
                "layout": {
                    (3, 4): RedSoldier()
                },
                "expected_destinations": {
                    (3, 4): ((3, 4), (3, 4)),
                    (3, 3): ((3, 4), (3, 3)),
                    (3, 5): ((3, 4), (3, 5)),
                    (4, 4): ((3, 4), (4, 4))
                }
            },
            {
                "name": "red_soldier_upper_left_blue_palace",
                "source": (7, 3),
                "layout": {
                    (7, 3): RedSoldier()
                },
                "expected_destinations": {
                    (7, 3): ((7, 3), (7, 3)),
                    (7, 2): ((7, 3), (7, 2)),
                    (8, 3): ((7, 3), (8, 3)),
                    (7, 4): ((7, 3), (7, 4)),
                    (8, 4): ((7, 3), (8, 4))
                }
            },
            {
                "name": "red_solider_upper_right_blue_palace",
                "source": (7, 5),
                "layout": {
                    (7, 5): RedSoldier()
                },
                "expected_destinations": {
                    (7, 5): ((7, 5), (7, 5)),
                    (7, 4): ((7, 5), (7, 4)),
                    (8, 5): ((7, 5), (8, 5)),
                    (7, 6): ((7, 5), (7, 6)),
                    (8, 4): ((7, 5), (8, 4))
                }
            },
            {
                "name": "red_soldier_center_blue_palace",
                "source": (8, 4),
                "layout": {
                    (8, 4): RedSoldier()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4)),
                    (8, 3): ((8, 4), (8, 3)),
                    (9, 4): ((8, 4), (9, 4)),
                    (8, 5): ((8, 4), (8, 5)),
                    (9, 3): ((8, 4), (9, 3)),
                    (9, 5): ((8, 4), (9, 5))
                }
            },
            {
                "name": "red_soldier_makes_red_general_check",
                "source": (3, 4),
                "layout": {
                    (3, 4): RedSoldier(),
                    (2, 4): RedGeneral(),
                    (4, 4): BlueChariot()
                },
                "expected_destinations": {
                    (3, 4): ((3, 4), (3, 4)),
                    (4, 4): ((3, 4), (4, 4))
                }
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_destinations = RedSoldier().destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


if __name__ == "__main__":
    unittest.main()
