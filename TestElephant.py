# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess elephant


import unittest
from Board import Board
from Chariot import RedChariot, BlueChariot
from Elephant import BlueElephant, RedElephant
from General import BlueGeneral, RedGeneral
from Soldier import BlueSoldier, RedSoldier


class TestBlueElephant(unittest.TestCase):
    def test_blue_elephant(self):
        # Given
        cases = [
            {
                "name": "blue_elephant",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueElephant()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (1, 2): ((4, 4), (3, 4), (2, 3), (1, 2)),
                    (1, 6): ((4, 4), (3, 4), (2, 5), (1, 6)),
                    (2, 7): ((4, 4), (4, 5), (3, 6), (2, 7)),
                    (6, 7): ((4, 4), (4, 5), (5, 6), (6, 7)),
                    (7, 6): ((4, 4), (5, 4), (6, 5), (7, 6)),
                    (7, 2): ((4, 4), (5, 4), (6, 3), (7, 2)),
                    (6, 1): ((4, 4), (4, 3), (5, 2), (6, 1)),
                    (2, 1): ((4, 4), (4, 3), (3, 2), (2, 1))
                }
            },
            {
                "name": "blue_elephant_blocked",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueElephant(),
                    (8, 4): BlueGeneral(),
                    (4, 3): BlueSoldier(),
                    (2, 3): BlueSoldier(),
                    (2, 5): BlueSoldier(),
                    (2, 7): BlueSoldier(),
                    (6, 7): BlueSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (7, 2): ((4, 4), (5, 4), (6, 3), (7, 2)),
                    (7, 6): ((4, 4), (5, 4), (6, 5), (7, 6))
                }
            },
            {
                "name": "blue_elephant_board_edge",
                "source": (4, 8),
                "layout": {
                    (4, 8): BlueElephant()
                },
                "expected_destinations": {
                    (4, 8): ((4, 8), (4, 8)),
                    (7, 6): ((4, 8), (5, 8), (6, 7), (7, 6)),
                    (6, 5): ((4, 8), (4, 7), (5, 6), (6, 5)),
                    (2, 5): ((4, 8), (4, 7), (3, 6), (2, 5)),
                    (1, 6): ((4, 8), (3, 8), (2, 7), (1, 6))
                }
            },
            {
                "name": "blue_elephant_makes_blue_general_check",
                "source": (6, 4),
                "layout": {
                    (6, 4): BlueElephant(),
                    (5, 4): RedChariot(),
                    (7, 4): BlueGeneral()
                },
                "expected_destinations": {
                    (6, 4): ((6, 4), (6, 4))
                }
            }
        ]
        for case in cases:
            # Given
            blue_elephant = BlueElephant()
            board = Board(case["layout"])

            # When
            actual_destinations = blue_elephant.destinations_from_source(case["source"], board)

            # Then
            self.assertEqual(case["expected_destinations"], actual_destinations)


class TestRedElephant(unittest.TestCase):
    def test_red_elephant(self):
        # Given
        cases = [
            {
                "name": "red_elephant",
                "source": (4, 4),
                "layout": {
                    (4, 4): RedElephant()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (1, 2): ((4, 4), (3, 4), (2, 3), (1, 2)),
                    (1, 6): ((4, 4), (3, 4), (2, 5), (1, 6)),
                    (2, 7): ((4, 4), (4, 5), (3, 6), (2, 7)),
                    (6, 7): ((4, 4), (4, 5), (5, 6), (6, 7)),
                    (7, 6): ((4, 4), (5, 4), (6, 5), (7, 6)),
                    (7, 2): ((4, 4), (5, 4), (6, 3), (7, 2)),
                    (6, 1): ((4, 4), (4, 3), (5, 2), (6, 1)),
                    (2, 1): ((4, 4), (4, 3), (3, 2), (2, 1))
                }
            },
            {
                "name": "red_elephant_blocked",
                "source": (4, 4),
                "layout": {
                    (4, 4): RedElephant(),
                    (3, 4): RedSoldier(),
                    (3, 6): RedSoldier(),
                    (5, 6): RedSoldier(),
                    (7, 6): RedSoldier(),
                    (7, 2): RedSoldier(),
                    (4, 3): RedSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4))
                }
            },
            {
                "name": "red_elephant_board_edge",
                "source": (0, 1),
                "layout": {
                    (0, 1): RedElephant()
                },
                "expected_destinations": {
                    (0, 1): ((0, 1), (0, 1)),
                    (3, 3): ((0, 1), (1, 1), (2, 2), (3, 3)),
                    (2, 4): ((0, 1), (0, 2), (1, 3), (2, 4))
                }
            },
            {
                "name": "red_elephant_makes_red_general_check",
                "source": (3, 4),
                "layout": {
                    (3, 4): RedElephant(),
                    (2, 4): RedGeneral(),
                    (4, 4): BlueChariot()
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
                actual_destinations = RedElephant().destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


if __name__ == "__main__":
    unittest.main()
