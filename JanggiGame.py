# Author: Ethan Davis
# Date: 2/27/21
# Description: Janggi Korean chess


from Board import Board


class JanggiGame:
    """
    Play Jangii Korean chess game at a high-level with Board handling chess game details
    """

    def __init__(self, layout=None):
        """
        Create JanggiGame Korean chess game
        :param layout: [Dict[Tuple[int], Piece]]

        :member _game_state: [str] UNFINISHED|RED_WON|BLUE_WON
        :member _board: [Board]
        """
        # Constants
        self._UNFINISHED = "UNFINISHED"
        self._RED_WON = "RED_WON"
        self._BLUE_WON = "BLUE_WON"

        self._game_state = self._UNFINISHED
        self._board = Board(layout)

    def __repr__(self):
        """
        String of Janggi Korean chess board
        """
        return str(self._board)

    def get_game_state(self):
        """
        REQUIRED METHOD SIGNATURE
        Get Janggi Korean chess game state
        :return: [str] UNFINISHED|RED_WON|BLUE_WON
        """
        return self._game_state

    def make_move(self, source, destination):
        """
        REQUIRED METHOD SIGNATURE
        Move piece from source to destination
        :param source: [str] [a-i][1-10]
        :param destination: [str] [a-i][1-10]
        :return: [bool]
        """
        make_move = True
        source = self._board.position_string_to_tuple(source)
        destination = self._board.position_string_to_tuple(destination)

        if not self.can_move(source, destination):
            make_move = False

        if make_move:
            self.do_move(source, destination)
            self.after_move()

        return make_move

    def can_move(self, source, destination):
        """
        Can move piece from source to destination
        :param source: [Tuple[int]]
        :param destination: [Tuple[int]]
        :return: [bool]
        """
        can_move = True

        if not self.game_is_unfinished():
            can_move = False

        if can_move and not self._board.piece_at_source(source):
            can_move = False

        if can_move and not self._board.piece_at_source_has_turn(source):
            can_move = False

        if can_move and not self._board.legal_move(source, destination):
            can_move = False

        return can_move

    def game_is_unfinished(self):
        """
        Game state is UNFINISHED
        :return: [bool]
        """
        return self._game_state == self._UNFINISHED

    def do_move(self, source, destination):
        """
        Do move piece from source to destination
        :param source: [Tuple[int]] [a-i][1-10]
        :param destination: [Tuple[int]] [a-i][1-10]
        :return: [None]
        """
        self._board.do_move(source, destination)

    def after_move(self):
        """
        After move from source to destination maybe game over
        :return: [None]
        """
        self.after_move_is_in_check() and self.after_move_is_in_checkmate()

    def after_move_is_in_check(self):
        """
        Even number of game moves and Blue General is in check, or
        Odd number of game moves and Red General is in check
        :return: [bool]
        """
        is_in_check = False

        if self._board.length_moves_even() and self._board.is_blue_in_check():
            is_in_check = True
        elif self._board.length_moves_odd() and self._board.is_red_in_check():
            is_in_check = True

        return is_in_check

    def after_move_is_in_checkmate(self):
        """
        Even number of game moves and Blue General is in checkmate, or
        Odd number of game moves and Red General is in checkmate
        :return: [None]
        """
        if self._board.length_moves_even() and self._board.is_blue_in_checkmate():
            self._game_state = self._RED_WON
        elif self._board.length_moves_odd() and self._board.is_red_in_checkmate():
            self._game_state = self._BLUE_WON

    def is_in_check(self, color):
        """
        REQUIRED METHOD SIGNATURE
        General with color is in check
        :param color: [str] RED|BLUE
        :return: [bool]
        """
        is_in_check = False
        color = color.upper()

        if color == "RED":
            is_in_check = self._board.is_red_in_check()
        elif color == "BLUE":
            is_in_check = self._board.is_blue_in_check()

        return is_in_check
