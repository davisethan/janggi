# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess horse


import unittest
from Board import Board
from Chariot import RedChariot, BlueChariot
from General import BlueGeneral, RedGeneral
from Horse import BlueHorse, RedHorse
from Soldier import BlueSoldier, RedSoldier


class TestBlueHorse(unittest.TestCase):
    def test_blue_horse_at_board_center(self):
        # Given
        cases = [
            {
                "name": "blue_horse",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueHorse()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (2, 3): ((4, 4), (3, 4), (2, 3)),
                    (2, 5): ((4, 4), (3, 4), (2, 5)),
                    (3, 6): ((4, 4), (4, 5), (3, 6)),
                    (5, 6): ((4, 4), (4, 5), (5, 6)),
                    (6, 5): ((4, 4), (5, 4), (6, 5)),
                    (6, 3): ((4, 4), (5, 4), (6, 3)),
                    (5, 2): ((4, 4), (4, 3), (5, 2)),
                    (3, 2): ((4, 4), (4, 3), (3, 2))
                }
            },
            {
                "name": "blue_horse_blocked",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueHorse(),
                    (4, 3): BlueSoldier(),
                    (3, 4): BlueSoldier(),
                    (3, 6): BlueSoldier(),
                    (5, 6): BlueSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (6, 3): ((4, 4), (5, 4), (6, 3)),
                    (6, 5): ((4, 4), (5, 4), (6, 5))
                }
            },
            {
                "name": "blue_horse_board_edge",
                "source": (4, 8),
                "layout": {
                    (4, 8): BlueHorse()
                },
                "expected_destinations": {
                    (4, 8): ((4, 8), (4, 8)),
                    (2, 7): ((4, 8), (3, 8), (2, 7)),
                    (6, 7): ((4, 8), (5, 8), (6, 7)),
                    (5, 6): ((4, 8), (4, 7), (5, 6)),
                    (3, 6): ((4, 8), (4, 7), (3, 6))
                }
            },
            {
                "name": "blue_horse_makes_blue_general_check",
                "source": (6, 4),
                "layout": {
                    (6, 4): BlueHorse(),
                    (7, 4): BlueGeneral(),
                    (5, 4): RedChariot()
                },
                "expected_destinations": {
                    (6, 4): ((6, 4), (6, 4))
                }
            }
        ]
        for case in cases:
            # Given
            blue_horse = BlueHorse()
            board = Board(case["layout"])

            # When
            actual_destinations = blue_horse.destinations_from_source(case["source"], board)

            # Then
            self.assertEqual(case["expected_destinations"], actual_destinations)


class TestRedHorse(unittest.TestCase):
    def test_red_horse(self):
        # Given
        cases = [
            {
                "name": "red_horse",
                "source": (4, 4),
                "layout": {
                    (4, 4): RedHorse()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (2, 3): ((4, 4), (3, 4), (2, 3)),
                    (2, 5): ((4, 4), (3, 4), (2, 5)),
                    (3, 6): ((4, 4), (4, 5), (3, 6)),
                    (5, 6): ((4, 4), (4, 5), (5, 6)),
                    (6, 5): ((4, 4), (5, 4), (6, 5)),
                    (6, 3): ((4, 4), (5, 4), (6, 3)),
                    (5, 2): ((4, 4), (4, 3), (5, 2)),
                    (3, 2): ((4, 4), (4, 3), (3, 2))
                }
            },
            {
                "name": "red_horse_blocked",
                "source": (4, 4),
                "layout": {
                    (4, 4): BlueHorse(),
                    (4, 3): RedSoldier(),
                    (3, 4): RedSoldier(),
                    (3, 6): RedSoldier(),
                    (5, 6): RedSoldier()
                },
                "expected_destinations": {
                    (4, 4): ((4, 4), (4, 4)),
                    (6, 3): ((4, 4), (5, 4), (6, 3)),
                    (6, 5): ((4, 4), (5, 4), (6, 5))
                }
            },
            {
                "name": "red_horse_board_edge",
                "source": (4, 8),
                "layout": {
                    (4, 8): RedHorse()
                },
                "expected_destinations": {
                    (4, 8): ((4, 8), (4, 8)),
                    (2, 7): ((4, 8), (3, 8), (2, 7)),
                    (6, 7): ((4, 8), (5, 8), (6, 7)),
                    (5, 6): ((4, 8), (4, 7), (5, 6)),
                    (3, 6): ((4, 8), (4, 7), (3, 6))
                }
            },
            {
                "name": "red_horse_makes_red_general_check",
                "source": (3, 4),
                "layout": {
                    (3, 4): RedHorse(),
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
                actual_destinations = RedHorse().destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


if __name__ == "__main__":
    unittest.main()
