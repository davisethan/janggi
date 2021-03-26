# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess chariot


import unittest
from Board import Board
from Chariot import BlueChariot, RedChariot
from General import BlueGeneral, RedGeneral
from Guard import BlueGuard, RedGuard
from Horse import BlueHorse, RedHorse
from Soldier import BlueSoldier, RedSoldier


class TestBlueChariot(unittest.TestCase):
    def test_blue_chariot(self):
        # Given
        cases = [
            {
                "name": "blue_chariot",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueChariot()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (3, 4): ((4, 4), (3, 4)),
                    (2, 4): ((4, 4), (3, 4), (2, 4)),
                    (1, 4): ((4, 4), (3, 4), (2, 4), (1, 4)),
                    (0, 4): ((4, 4), (3, 4), (2, 4), (1, 4), (0, 4)),
                    (4, 5): ((4, 4), (4, 5)),
                    (4, 6): ((4, 4), (4, 5), (4, 6)),
                    (4, 7): ((4, 4), (4, 5), (4, 6), (4, 7)),
                    (4, 8): ((4, 4), (4, 5), (4, 6), (4, 7), (4, 8)),
                    (5, 4): ((4, 4), (5, 4)),
                    (6, 4): ((4, 4), (5, 4), (6, 4)),
                    (7, 4): ((4, 4), (5, 4), (6, 4), (7, 4)),
                    (8, 4): ((4, 4), (5, 4), (6, 4), (7, 4), (8, 4)),
                    (9, 4): ((4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4)),
                    (4, 3): ((4, 4), (4, 3)),
                    (4, 2): ((4, 4), (4, 3), (4, 2)),
                    (4, 1): ((4, 4), (4, 3), (4, 2), (4, 1)),
                    (4, 0): ((4, 4), (4, 3), (4, 2), (4, 1), (4, 0))
                }
            },
            {
                "name": "blue_chariot_blocked",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueChariot(),
                    (2, 4): BlueSoldier(),
                    (4, 6): BlueSoldier(),
                    (6, 4): RedSoldier(),
                    (4, 2): RedSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (3, 4): ((4, 4), (3, 4)),
                    (4, 5): ((4, 4), (4, 5)),
                    (5, 4): ((4, 4), (5, 4)),
                    (6, 4): ((4, 4), (5, 4), (6, 4)),
                    (4, 3): ((4, 4), (4, 3)),
                    (4, 2): ((4, 4), (4, 3), (4, 2))
                }
            },
            {
                "name": "blue_chariot_palace_lower_left_corner",
                "source": (9, 3),
                "layout": {
                    (9, 3): BlueChariot(),
                    (8, 3): BlueGuard(),
                    (9, 2): BlueHorse(),
                    (9, 4): BlueGuard()
                },
                "expected_destinations": {
                    (9, 3): ((9, 3), (9, 3)),
                    (8, 4): ((9, 3), (8, 4)),
                    (7, 5): ((9, 3), (8, 4), (7, 5))
                }
            },
            {
                "name": "blue_chariot_palace_upper_left_corner",
                "source": (7, 3),
                "layout": {
                    (7, 3): BlueChariot(),
                    (7, 2): BlueHorse(),
                    (6, 3): BlueSoldier(),
                    (7, 4): BlueGuard(),
                    (8, 3): BlueGuard()
                },
                "expected_destinations": {
                    (7, 3): ((7, 3), (7, 3)),
                    (8, 4): ((7, 3), (8, 4)),
                    (9, 5): ((7, 3), (8, 4), (9, 5))
                }
            },
            {
                "name": "blue_chariot_palace_upper_right_corner",
                "source": (7, 5),
                "layout": {
                    (7, 5): BlueChariot(),
                    (6, 5): BlueSoldier(),
                    (7, 6): BlueHorse(),
                    (8, 5): BlueGuard(),
                    (7, 4): BlueGuard()
                },
                "expected_destinations": {
                    (7, 5): ((7, 5), (7, 5)),
                    (8, 4): ((7, 5), (8, 4)),
                    (9, 3): ((7, 5), (8, 4), (9, 3))
                }
            },
            {
                "name": "blue_chariot_palace_lower_right_corner",
                "source": (9, 5),
                "layout": {
                    (9, 5): BlueChariot(),
                    (8, 5): BlueGuard(),
                    (9, 4): BlueGuard(),
                    (9, 6): BlueHorse()
                },
                "expected_destinations": {
                    (9, 5): ((9, 5), (9, 5)),
                    (8, 4): ((9, 5), (8, 4)),
                    (7, 3): ((9, 5), (8, 4), (7, 3))
                }
            },
            {
                "name": "blue_chariot_palace_center",
                "source": (8, 4),
                "layout": {
                    (8, 4): BlueChariot(),
                    (7, 4): BlueHorse(),
                    (8, 5): BlueHorse(),
                    (9, 4): BlueGuard(),
                    (8, 3): BlueGuard()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4)),
                    (7, 3): ((8, 4), (7, 3)),
                    (7, 5): ((8, 4), (7, 5)),
                    (9, 5): ((8, 4), (9, 5)),
                    (9, 3): ((8, 4), (9, 3))
                }
            },
            {
                "name": "blue_chariot_makes_generals_face",
                "source": (6, 4),
                "layout": {
                    (6, 4): BlueChariot(),
                    (8, 4): BlueGeneral(),
                    (1, 4): RedGeneral()
                },
                "expected_destinations": {
                    (6, 4): ((6, 4), (6, 4)),
                    (7, 4): ((6, 4), (7, 4)),
                    (5, 4): ((6, 4), (5, 4)),
                    (4, 4): ((6, 4), (5, 4), (4, 4)),
                    (3, 4): ((6, 4), (5, 4), (4, 4), (3, 4)),
                    (2, 4): ((6, 4), (5, 4), (4, 4), (3, 4), (2, 4)),
                    (1, 4): ((6, 4), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4))
                }
            },
            {
                "name": "blue_chariot_makes_blue_general_check",
                "source": (6, 4),
                "layout": {
                    (6, 4): BlueChariot(),
                    (5, 4): RedChariot(),
                    (7, 4): BlueGeneral()
                },
                "expected_destinations": {
                    (6, 4): ((6, 4), (6, 4)),
                    (5, 4): ((6, 4), (5, 4))
                }
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                blue_chariot = BlueChariot()
                board = Board(case["layout"])

                # When
                actual_destinations = blue_chariot.destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


class TestRedChariot(unittest.TestCase):
    def test_red_chariot(self):
        # Given
        cases = [
            {
                "name": "red_chariot",
                "source": (4, 4),
                "layout": {
                    (4, 4): RedChariot()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (3, 4): ((4, 4), (3, 4)),
                    (2, 4): ((4, 4), (3, 4), (2, 4)),
                    (1, 4): ((4, 4), (3, 4), (2, 4), (1, 4)),
                    (0, 4): ((4, 4), (3, 4), (2, 4), (1, 4), (0, 4)),
                    (4, 5): ((4, 4), (4, 5)),
                    (4, 6): ((4, 4), (4, 5), (4, 6)),
                    (4, 7): ((4, 4), (4, 5), (4, 6), (4, 7)),
                    (4, 8): ((4, 4), (4, 5), (4, 6), (4, 7), (4, 8)),
                    (5, 4): ((4, 4), (5, 4)),
                    (6, 4): ((4, 4), (5, 4), (6, 4)),
                    (7, 4): ((4, 4), (5, 4), (6, 4), (7, 4)),
                    (8, 4): ((4, 4), (5, 4), (6, 4), (7, 4), (8, 4)),
                    (9, 4): ((4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4)),
                    (4, 3): ((4, 4), (4, 3)),
                    (4, 2): ((4, 4), (4, 3), (4, 2)),
                    (4, 1): ((4, 4), (4, 3), (4, 2), (4, 1)),
                    (4, 0): ((4, 4), (4, 3), (4, 2), (4, 1), (4, 0))
                }
            },
            {
                "name": "red_chariot_blocked",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueChariot(),
                    (2, 4): RedSoldier(),
                    (4, 6): RedSoldier(),
                    (6, 4): BlueSoldier(),
                    (4, 2): BlueSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (3, 4): ((4, 4), (3, 4)),
                    (4, 5): ((4, 4), (4, 5)),
                    (5, 4): ((4, 4), (5, 4)),
                    (6, 4): ((4, 4), (5, 4), (6, 4)),
                    (4, 3): ((4, 4), (4, 3)),
                    (4, 2): ((4, 4), (4, 3), (4, 2))
                }
            },
            {
                "name": "red_chariot_palace_lower_left_corner",
                "source": (9, 3),
                "layout": {
                    (9, 3): RedChariot(),
                    (8, 3): RedGuard(),
                    (9, 2): RedHorse(),
                    (9, 4): RedGuard()
                },
                "expected_destinations": {
                    (9, 3): ((9, 3), (9, 3)),
                    (8, 4): ((9, 3), (8, 4)),
                    (7, 5): ((9, 3), (8, 4), (7, 5))
                }
            },
            {
                "name": "red_chariot_palace_upper_left_corner",
                "source": (7, 3),
                "layout": {
                    (7, 3): RedChariot(),
                    (7, 2): RedHorse(),
                    (6, 3): RedSoldier(),
                    (7, 4): RedGuard(),
                    (8, 3): RedGuard()
                },
                "expected_destinations": {
                    (7, 3): ((7, 3), (7, 3)),
                    (8, 4): ((7, 3), (8, 4)),
                    (9, 5): ((7, 3), (8, 4), (9, 5))
                }
            },
            {
                "name": "red_chariot_palace_upper_right_corner",
                "source": (7, 5),
                "layout": {
                    (7, 5): RedChariot(),
                    (6, 5): RedSoldier(),
                    (7, 6): RedHorse(),
                    (8, 5): RedGuard(),
                    (7, 4): RedGuard()
                },
                "expected_destinations": {
                    (7, 5): ((7, 5), (7, 5)),
                    (8, 4): ((7, 5), (8, 4)),
                    (9, 3): ((7, 5), (8, 4), (9, 3))
                }
            },
            {
                "name": "red_chariot_palace_lower_right_corner",
                "source": (9, 5),
                "layout": {
                    (9, 5): RedChariot(),
                    (8, 5): RedGuard(),
                    (9, 4): RedGuard(),
                    (9, 6): RedHorse()
                },
                "expected_destinations": {
                    (9, 5): ((9, 5), (9, 5)),
                    (8, 4): ((9, 5), (8, 4)),
                    (7, 3): ((9, 5), (8, 4), (7, 3))
                }
            },
            {
                "name": "red_chariot_palace_center",
                "source": (8, 4),
                "layout": {
                    (8, 4): RedChariot(),
                    (7, 4): RedHorse(),
                    (8, 5): RedHorse(),
                    (9, 4): RedGuard(),
                    (8, 3): RedGuard()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4)),
                    (7, 3): ((8, 4), (7, 3)),
                    (7, 5): ((8, 4), (7, 5)),
                    (9, 5): ((8, 4), (9, 5)),
                    (9, 3): ((8, 4), (9, 3))
                }
            },
            {
                "name": "red_chariot_makes_red_general_check",
                "source": (3, 4),
                "layout": {
                    (3, 4): RedChariot(),
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
                actual_destinations = RedChariot().destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


if __name__ == "__main__":
    unittest.main()
