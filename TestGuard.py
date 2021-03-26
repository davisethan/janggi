# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess guard


import unittest
from Board import Board
from Chariot import RedChariot, BlueChariot
from Guard import BlueGuard, RedGuard
from General import BlueGeneral, RedGeneral


class TestBlueGuard(unittest.TestCase):
    def test_blue_guard(self):
        # Given
        cases = [
            {
                "name": "blue_guard_board_edge",
                "source": (9, 3),
                "layout": {
                    (9, 3): BlueGuard(),
                    (8, 4): BlueGeneral(),
                    (9, 5): BlueGuard()
                },
                "expected_destinations": {
                    (9, 3): ((9, 3), (9, 3)),
                    (8, 3): ((9, 3), (8, 3)),
                    (9, 4): ((9, 3), (9, 4))
                }
            },
            {
                "name": "blue_guard_makes_generals_face",
                "source": (7, 4),
                "layout": {
                    (7, 4): BlueGuard(),
                    (8, 4): BlueGeneral(),
                    (8, 5): BlueGuard(),
                    (1, 4): RedGeneral()
                },
                "expected_destinations": {
                    (7, 4): ((7, 4), (7, 4))
                }
            },
            {
                "name": "blue_guard_makes_blue_general_check",
                "source": (7, 4),
                "layout": {
                    (7, 4): BlueGuard(),
                    (8, 4): BlueGeneral(),
                    (4, 4): RedChariot()
                },
                "expected_destinations": {
                    (7, 4): ((7, 4), (7, 4))
                }
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                blue_guard = BlueGuard()
                board = Board(case["layout"])

                # When
                actual_destinations = blue_guard.destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


class TestRedGuard(unittest.TestCase):
    def test_red_guard(self):
        # Given
        cases = [
            {
                "name": "red_guard",
                "source": (0, 3),
                "layout": {
                    (0, 3): RedGuard(),
                    (1, 4): RedGeneral(),
                    (0, 5): RedGuard()
                },
                "expected_destinations": {
                    (0, 3): ((0, 3), (0, 3)),
                    (0, 4): ((0, 3), (0, 4)),
                    (1, 3): ((0, 3), (1, 3))
                }
            },
            {
                "name": "red_guard_doesnt_capture_red_guard",
                "source": (0, 3),
                "layout": {
                    (0, 3): RedGuard(),
                    (0, 4): RedGuard(),
                    (1, 4): RedGeneral()
                },
                "expected_destinations": {
                    (0, 3): ((0, 3), (0, 3)),
                    (1, 3): ((0, 3), (1, 3))
                }
            },
            {
                "name": "red_guard_makes_red_general_check",
                "source": (2, 4),
                "layout": {
                    (2, 4): RedGuard(),
                    (1, 4): RedGeneral(),
                    (4, 4): BlueChariot()
                },
                "expected_destinations": {
                    (2, 4): ((2, 4), (2, 4))
                }
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_destinations = RedGuard().destinations_from_source(case["source"], board)

                # Then
                self.assertEqual(case["expected_destinations"], actual_destinations)


if __name__ == "__main__":
    unittest.main()
