# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess board


import unittest
from Board import Board
from Chariot import RedChariot, BlueChariot
from Elephant import BlueElephant
from General import BlueGeneral, RedGeneral
from Guard import BlueGuard
from Horse import BlueHorse, RedHorse
from Soldier import RedSoldier, BlueSoldier


class TestBoard(unittest.TestCase):
    def test_position_string_to_tuple(self):
        # Given
        cases = [
            {
                "name": "one",
                "position_string": "a10",
                "expected_position_tuple": (9, 0)
            },
            {
                "name": "two",
                "position_string": "e2",
                "expected_position_tuple": (1, 4)
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board()

                # When
                actual_position_tuple = board.position_string_to_tuple(case["position_string"])

                # Then
                self.assertEqual(case["expected_position_tuple"], actual_position_tuple)

    def test_destination_in_blue_palace(self):
        # Given
        cases = [
            {
                "name": "one",
                "destination": (8, 4),
                "expected_inside": True
            },
            {
                "name": "two",
                "destination": (1, 4),
                "expected_inside": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board()

                # When
                actual_inside = board.destination_in_blue_palace(case["destination"])

                # Then
                self.assertEqual(case["expected_inside"], actual_inside)

    def test_destination_in_board(self):
        # Given
        cases = [
            {
                "name": "inside",
                "destination": (8, 4),
                "expected_inside": True
            },
            {
                "name": "outside",
                "destination": (10, 9),
                "expected_inside": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board()

                # When
                actual_inside = board.destination_in_board(case["destination"])

                # Then
                self.assertEqual(case["expected_inside"], actual_inside)

    def test_destination_captures_blue_piece(self):
        # Given
        cases = [
            {
                "name": "one",
                "source": (8, 4),
                "destination": (8, 5),
                "layout": {
                    (8, 4): BlueGeneral(),
                    (8, 5): BlueGuard()
                },
                "expected_capture": True
            },
            {
                "name": "two",
                "source": (8, 4),
                "destination": (8, 4),
                "layout": {
                    (8, 4): BlueGeneral()
                },
                "expected_capture": False
            },
            {
                "name": "three",
                "source": (8, 4),
                "destination": (8, 5),
                "layout": {
                    (8, 4): BlueGeneral()
                },
                "expected_capture": False
            },
            {
                "name": "four",
                "source": (8, 4),
                "destination": (8, 5),
                "layout": {
                    (8, 4): BlueGeneral(),
                    (8, 5): RedSoldier()
                },
                "expected_capture": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_capture = board.destination_captures_blue_piece(case["source"], case["destination"])

                # Then
                self.assertEqual(case["expected_capture"], actual_capture)

    def test_try_move(self):
        # Given
        cases = [
            {
                "name": "one",
                "source": (8, 4),
                "destination": (8, 5),
                "layout": {
                    (8, 4): BlueGeneral()
                },
                "expected_source_type": type(None),
                "expected_destination_type": BlueGeneral
            },
            {
                "name": "two",
                "source": (8, 4),
                "destination": (8, 4),
                "layout": {
                    (8, 4): BlueGeneral()
                },
                "expected_source_type": BlueGeneral,
                "expected_destination_type": BlueGeneral
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                board.try_move(case["source"], case["destination"])
                layout = board.get_layout()
                actual_source_type = type(layout[case["source"]])
                actual_destination_type = type(layout[case["destination"]])

                # Then
                self.assertEqual(case["expected_source_type"], actual_source_type)
                self.assertEqual(case["expected_destination_type"], actual_destination_type)

    def test_undo_move(self):
        # Given
        source = (8, 4)
        destination = (8, 5)
        layout = {
            (8, 4): BlueGeneral()
        }
        board = Board(layout)
        board.try_move(source, destination)

        # When
        board.undo_move()
        layout = board.get_layout()
        actual_source_type = type(layout[source])
        actual_destination_type = type(layout[destination])

        # Then
        expected_source_type = BlueGeneral
        expected_destination_type = type(None)
        self.assertEqual(expected_source_type, actual_source_type)
        self.assertEqual(expected_destination_type, actual_destination_type)

    def test_do_generals_face(self):
        # Given
        cases = [
            {
                "name": "one",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (1, 4): RedGeneral()
                },
                "expected_face": True
            },
            {
                "name": "two",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (1, 5): RedGeneral()
                },
                "expected_face": False
            },
            {
                "name": "three",
                "layout": {
                    (8, 4): BlueGeneral()
                },
                "expected_face": False
            },
            {
                "name": "four",
                "layout": {
                    (1, 4): RedGeneral()
                },
                "expected_face": False
            },
            {
                "name": "five",
                "layout": dict(),
                "expected_face": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_face = board.do_generals_face()

                # Then
                self.assertEqual(case["expected_face"], actual_face)

    def test_is_blue_in_check(self):
        # Given
        cases = [
            {
                "name": "blue_in_check",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (4, 4): RedChariot()
                },
                "expected_check": True
            },
            {
                "name": "blue_not_in_check",
                "layout": {
                    (8, 4): BlueGeneral()
                },
                "expected_check": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_check = board.is_blue_in_check()

                # Then
                self.assertEqual(case["expected_check"], actual_check)

    def test_piece_at_source(self):
        # Given
        cases = [
            {
                "name": "piece_at_source",
                "source": (6, 4),
                "expected_piece": True
            },
            {
                "name": "piece_not_at_source",
                "source": (5, 4),
                "expected_piece": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board()

                # When
                actual_piece = board.piece_at_source(case["source"])

                # Then
                self.assertEqual(case["expected_piece"], actual_piece)

    def test_piece_at_source_has_turn(self):
        # Given
        cases = [
            {
                "name": "has_turn",
                "source": (6, 4),
                "expected_has_turn": True
            },
            {
                "name": "doesnt_have_turn",
                "source": (3, 4),
                "expected_has_turn": False
            },
            {
                "name": "no_piece",
                "source": (4, 4),
                "expected_has_turn": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board()

                # When
                actual_has_turn = board.piece_at_source_has_turn(case["source"])

                # Then
                self.assertEqual(case["expected_has_turn"], actual_has_turn)

    def test_legal_move(self):
        # Given
        cases = [
            {
                "name": "legal_move",
                "source": (6, 4),
                "destination": (5, 4),
                "expected_legal_move": True
            },
            {
                "name": "not_legal_move",
                "source": (6, 4),
                "destination": (4, 4),
                "expected_legal_move": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board()

                # When
                actual_legal_move = board.legal_move(case["source"], case["destination"])

                # Then
                self.assertEqual(case["expected_legal_move"], actual_legal_move)

    def test_can_move_blue_general(self):
        # Given
        cases = [
            {
                "name": "can_move_blue_general",
                "layout": None,
                "expected_can_move_blue_general": True
            },
            {
                "name": "cant_move_blue_general",
                "layout": {
                    (7, 3): BlueSoldier(),
                    (7, 4): BlueSoldier(),
                    (7, 5): BlueSoldier(),
                    (8, 3): BlueGuard(),
                    (8, 4): BlueGeneral(),
                    (9, 3): BlueSoldier(),
                    (9, 4): BlueSoldier(),
                    (9, 5): BlueSoldier(),
                    (8, 6): RedChariot()
                },
                "expected_can_move_blue_general": False
            },
            {
                "name": "blue_general_checkmate",
                "layout": {
                    (7, 4): BlueGeneral(),
                    (8, 4): RedChariot(),
                    (8, 6): RedChariot()
                },
                "expected_can_move_blue_general": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_can_move_blue_general = board.can_move_blue_general()

                # Then
                self.assertEqual(case["expected_can_move_blue_general"], actual_can_move_blue_general)

    def test_blue_sources_with_destination(self):
        # Given
        destination = (4, 4)
        layout = {
            (6, 1): BlueElephant(),
            (5, 4): BlueChariot(),
            (5, 6): BlueHorse(),
            (8, 4): BlueGeneral()
        }
        board = Board(layout)

        # When
        actual_sources = board.blue_sources_with_destination(destination)

        # Then
        expected_sources = {(6, 1), (5, 4), (5, 6)}
        self.assertEqual(expected_sources, actual_sources)

    def test_blue_paths_with_destination(self):
        # Given
        destination = (4, 4)
        layout = {
            (6, 1): BlueElephant(),
            (5, 4): BlueChariot(),
            (5, 6): BlueHorse(),
            (8, 4): BlueGeneral()
        }
        board = Board(layout)

        # When
        actual_paths = board.blue_paths_with_destination(destination)

        # Then
        expected_paths = {
            ((6, 1), (6, 2), (5, 3), (4, 4)),
            ((5, 4), (4, 4)),
            ((5, 6), (5, 5), (4, 4))
        }
        self.assertEqual(expected_paths, actual_paths)

    def test_can_capture_blue_general_attacker(self):
        # Given
        cases = [
            {
                "name": "can_capture_blue_general_attacker",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (4, 4): RedChariot(),
                    (4, 6): BlueChariot()
                },
                "expected_can_capture": True
            },
            {
                "name": "cant_capture_blue_general_attacker",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (4, 4): RedChariot()
                },
                "expected_can_capture": False
            },
            {
                "name": "cant_capture_two_blue_general_attackers",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (6, 5): RedHorse(),
                    (3, 4): RedChariot(),
                    (3, 5): BlueChariot()
                },
                "expected_can_capture": False
            },
            {
                "name": "blue_general_capture_checks_self",
                "layout": {
                    (7, 4): BlueGeneral(),
                    (8, 4): RedChariot(),
                    (8, 6): RedChariot()
                },
                "expected_can_capture": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_can_capture = board.can_capture_blue_general_attacker()

                # Then
                self.assertEqual(case["expected_can_capture"], actual_can_capture)

    def test_can_block_blue_general_attacker(self):
        # Given
        cases = [
            {
                "name": "can_block_blue_general_attacker",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (4, 4): RedChariot(),
                    (7, 5): BlueGuard()
                },
                "expected_can_block": True
            },
            {
                "name": "cant_block_blue_general_attacker",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (4, 4): RedChariot(),
                    (9, 4): BlueGuard()
                },
                "expected_can_block": False
            },
            {
                "name": "cant_block_two_blue_general_attackers",
                "layout": {
                    (8, 4): BlueGeneral(),
                    (8, 7): RedChariot(),
                    (3, 4): RedChariot(),
                    (4, 5): BlueChariot()
                },
                "expected_can_block": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_can_block = board.can_block_blue_general_attacker()

                # Then
                self.assertEqual(case["expected_can_block"], actual_can_block)

    def test_is_blue_in_checkmate(self):
        # Given
        cases = [
            {
                "name": "blue_in_checkmate",
                "layout": {
                    (7, 4): BlueGeneral(),
                    (8, 4): RedChariot(),
                    (8, 6): RedChariot()
                },
                "expected_checkmate": True
            },
            {
                "name": "blue_not_in_checkmate",
                "layout": {
                    (7, 4): BlueGeneral(),
                    (8, 4): RedChariot()
                },
                "expected_checkmate": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                board = Board(case["layout"])

                # When
                actual_checkmate = board.is_blue_in_checkmate()

                # Then
                self.assertEqual(case["expected_checkmate"], actual_checkmate)


if __name__ == "__main__":
    unittest.main()
