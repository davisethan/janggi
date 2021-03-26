# Author: Ethan Davis
# Date: 2/27/21
# Description: Test Janggi Korean chess


import unittest

from Chariot import RedChariot
from General import BlueGeneral
from Soldier import RedSoldier
from JanggiGame import JanggiGame


# Behavior Drive Development (BDD)
# Given-When-Then


class TestJanggiGame(unittest.TestCase):
    def test_janggi_game(self):
        # Given
        janggi_game = JanggiGame()

        # When
        actual_janggi_game = str(janggi_game)

        # Then
        expected_janggi_game = ""
        expected_janggi_game += "  A  B  C  D  E  F  G  H  I\n"
        expected_janggi_game += "1|RC|RE|RH|RU|  |RU|RE|RH|RC|\n"
        expected_janggi_game += "2|  |  |  |  |RG|  |  |  |  |\n"
        expected_janggi_game += "3|  |RA|  |  |  |  |  |RA|  |\n"
        expected_janggi_game += "4|RS|  |RS|  |RS|  |RS|  |RS|\n"
        expected_janggi_game += "5|  |  |  |  |  |  |  |  |  |\n"
        expected_janggi_game += "6|  |  |  |  |  |  |  |  |  |\n"
        expected_janggi_game += "7|BS|  |BS|  |BS|  |BS|  |BS|\n"
        expected_janggi_game += "8|  |BA|  |  |  |  |  |BA|  |\n"
        expected_janggi_game += "9|  |  |  |  |BG|  |  |  |  |\n"
        expected_janggi_game += "10|BC|BE|BH|BU|  |BU|BE|BH|BC|\n"

        self.assertEqual(expected_janggi_game, actual_janggi_game)

    def test_can_move(self):
        # Given
        cases = [
            {
                "name": "can_move",
                "source": (6, 4),
                "destination": (5, 4),
                "expected_can_move": True
            },
            {
                "name": "cannot_move_red_piece",
                "source": (6, 4),
                "destination": (4, 4),
                "expected_can_move": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                janggi_game = JanggiGame()

                # When
                actual_can_move = janggi_game.can_move(case["source"], case["destination"])

                # Then
                self.assertEqual(case["expected_can_move"], actual_can_move)

    def test_readme_example(self):
        # Given
        game = JanggiGame()

        # When
        move_result_one = game.make_move("c1", "e3")
        move_result_two = game.make_move("a7", "b7")
        blue_in_check = game.is_in_check("blue")
        move_result_three = game.make_move('a4', 'a5')
        state = game.get_game_state()
        move_result_four = game.make_move("b7", "b6")
        move_result_five = game.make_move("b3", "b6")
        move_result_six = game.make_move("a1", "a4")
        move_result_seven = game.make_move("c7", "d7")
        move_result_eight = game.make_move("a4", "a4")

        # Then
        self.assertFalse(move_result_one, "Not Red's turn")
        self.assertTrue(move_result_two)
        self.assertFalse(blue_in_check)
        self.assertTrue(move_result_three)
        self.assertEqual("UNFINISHED", state)
        self.assertTrue(move_result_four)
        self.assertFalse(move_result_five, "Invalid move")
        self.assertTrue(move_result_six)
        self.assertTrue(move_result_seven)
        self.assertTrue(move_result_eight, "Red passes turn")

    def test_make_move(self):
        # Given
        cases = [
            {
                "name": "two_move_checkmate",
                "layout": {
                    (9, 3): BlueGeneral(),
                    (4, 4): RedChariot(),
                    (7, 5): RedSoldier()
                },
                "source_one": "d10",
                "destination_one": "d9",
                "source_two": "e5",
                "destination_two": "e9",
                "expected_game_state": "RED_WON"
            },
            {
                "name": "two_move_checkmate_general_passes_turn",
                "layout": {
                    (9, 3): BlueGeneral(),
                    (4, 4): RedChariot(),
                    (7, 5): RedSoldier()
                },
                "source_one": "d10",
                "destination_one": "d10",
                "source_two": "e5",
                "destination_two": "e9",
                "expected_game_state": "RED_WON"
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                # Given
                game = JanggiGame(case["layout"])

                # When
                game.make_move(case["source_one"], case["destination_one"])
                game.make_move(case["source_two"], case["destination_two"])
                actual_game_state = game.get_game_state()

                # Then
                self.assertEqual(case["expected_game_state"], actual_game_state)


if __name__ == "__main__":
    unittest.main()
