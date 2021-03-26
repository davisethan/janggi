# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess general


import unittest
from Board import Board
from Chariot import RedChariot, BlueChariot
from General import BlueGeneral, RedGeneral
from Guard import BlueGuard, RedGuard
from Horse import BlueHorse
from Soldier import RedSoldier


class TestBlueGeneral(unittest.TestCase):
    def test_blue_general(self):
        # Given
        cases = [
            {
                "name": "blue_general",
                "source": (8, 4),
                "layout": {
                    (8, 4): BlueGeneral(),
                    (9, 3): BlueGuard(),
                    (9, 5): BlueGuard()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4)),
                    (7, 4): ((8, 4), (7, 4)),
                    (7, 5): ((8, 4), (7, 5)),
                    (8, 5): ((8, 4), (8, 5)),
                    (9, 4): ((8, 4), (9, 4)),
                    (8, 3): ((8, 4), (8, 3)),
                    (7, 3): ((8, 4), (7, 3))
                }
            },
            {
                "name": "blue_general_and_red_general_face",
                "source": (8, 4),
                "layout": {
                    (8, 4): BlueGeneral(),
                    (9, 3): BlueGuard(),
                    (9, 5): BlueGuard(),
                    (1, 3): RedGeneral()
                },
                "expected_destinations": {
                    (8, 4): ((8, 4), (8, 4)),
                    (7, 4): ((8, 4), (7, 4)),
                    (7, 5): ((8, 4), (7, 5)),
                    (8, 5): ((8, 4), (8, 5)),
                    (9, 4): ((8, 4), (9, 4))
                }
            },
            {
                "name": "blue_general_board_edge",
                "source": (9, 4),
                "layout": {
                    (9, 4): BlueGeneral(),
                    (9, 3): BlueGuard(),
                    (9, 5): BlueGuard()
                },
                "expected_destinations": {
                    (9, 4): ((9, 4), (9, 4)),
                    (8, 3): ((9, 4), (8, 3)),
                    (8, 4): ((9, 4), (8, 4)),
                    (8, 5): ((9, 4), (8, 5))
                }
            },
            {
                "name": "blue_general_check",
                "source": (8, 4),
                "layout": {
                    (8, 4): BlueGeneral(),
                    (7, 4): RedSoldier()
                },
                "expected_destinations": {
                    (7, 4): ((8, 4), (7, 4)),
                    (8, 3): ((8, 4), (8, 3)),
                    (9, 3): ((8, 4), (9, 3)),
                    (9, 4): ((8, 4), (9, 4)),
                    (9, 5): ((8, 4), (9, 5)),
                    (8, 5): ((8, 4), (8, 5))
                }
            },
            {
                "name": "blue_general_check_two",
                "source": (8, 4),
                "layout": {
                    (8, 4): BlueGeneral(),
                    (4, 4): RedChariot(),
                    (7, 3): BlueGuard(),
                    (8, 3): BlueHorse(),
                    (9, 3): BlueGuard()
                },
                "expected_destinations": {
                    (7, 5): ((8, 4), (7, 5)),
                    (8, 5): ((8, 4), (8, 5)),
                    (9, 5): ((8, 4), (9, 5))
                }
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                blue_general = BlueGeneral()
                board = Board(case["layout"])

                # When
                actual_destinations = blue_general.destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


class TestRedGeneral(unittest.TestCase):
    def test_red_general(self):
        # Given
        cases = [
            {
                "name": "red_general",
                "source": (1, 4),
                "layout": {
                    (1, 4): RedGeneral(),
                    (0, 3): RedGuard(),
                    (0, 5): RedGuard()
                },
                "expected_destinations": {
                    (1, 4): ((1, 4), (1, 4)),
                    (0, 4): ((1, 4), (0, 4)),
                    (1, 5): ((1, 4), (1, 5)),
                    (2, 5): ((1, 4), (2, 5)),
                    (2, 4): ((1, 4), (2, 4)),
                    (2, 3): ((1, 4), (2, 3)),
                    (1, 3): ((1, 4), (1, 3))
                }
            },
            {
                "name": "red_general_board_edge",
                "source": (0, 3),
                "layout": {
                    (0, 3): RedGeneral(),
                    (2, 3): RedGuard(),
                    (0, 5): RedGuard()
                },
                "expected_destinations": {
                    (0, 3): ((0, 3), (0, 3)),
                    (0, 4): ((0, 3), (0, 4)),
                    (1, 4): ((0, 3), (1, 4)),
                    (1, 3): ((0, 3), (1, 3))
                }
            },
            {
                "name": "red_general_check",
                "source": (1, 4),
                "layout": {
                    (1, 4): RedGeneral(),
                    (4, 4): BlueChariot()
                },
                "expected_destinations": {
                    (0, 3): ((1, 4), (0, 3)),
                    (0, 5): ((1, 4), (0, 5)),
                    (1, 5): ((1, 4), (1, 5)),
                    (2, 5): ((1, 4), (2, 5)),
                    (2, 3): ((1, 4), (2, 3)),
                    (1, 3): ((1, 4), (1, 3))
                }
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_destinations = RedGeneral().destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


if __name__ == "__main__":
    unittest.main()
