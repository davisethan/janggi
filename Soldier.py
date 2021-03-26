# Author: Ethan Davis
# Date: 2/27/21
# Description: Janggi Korean chess soldier piece


from Piece import Piece


class Soldier(Piece):
    """
    Soldier (Piece) handles finding soldier move destinations from source filtering moves with board layout
    """
    pass


class BlueSoldier(Soldier):
    """
    BlueSoldier (Piece) handles finding soldier move destinations from source filtering moves with board layout
    """

    def all_destinations_from_source(self, source):
        """
        All blue soldier destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        row = source[0]
        column = source[1]
        own_destination = (row, column)
        own_path = (source, own_destination)
        left_destination = (row, column - 1)
        left_path = (source, left_destination)
        up_destination = (row - 1, column)
        up_path = (source, up_destination)
        right_destination = (row, column + 1)
        right_path = (source, right_destination)
        destinations = {
            own_destination: own_path,
            left_destination: left_path,
            up_destination: up_path,
            right_destination: right_path
        }

        lower_left_red_palace_source = (2, 3)
        lower_right_red_palace_source = (2, 5)
        if source == lower_left_red_palace_source or source == lower_right_red_palace_source:
            diagonal_destination = (1, 4)
            diagonal_path = (source, diagonal_destination)
            destinations[diagonal_destination] = diagonal_path

        center_red_palace_source = (1, 4)
        if source == center_red_palace_source:
            left_diagonal_destination = (0, 3)
            left_diagonal_path = (source, left_diagonal_destination)
            right_diagonal_destination = (0, 5)
            right_diagonal_path = (source, right_diagonal_destination)
            destinations[left_diagonal_destination] = left_diagonal_path
            destinations[right_diagonal_destination] = right_diagonal_path

        return destinations

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Blue soldier destinations from source with paths
        :param source: [Tuple[int]] Board source destination
        :param board: [Board]
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        all_destinations = self.all_destinations_from_source(source)
        destinations = dict()

        for destination in all_destinations:
            add_destination = True

            if not board.destination_in_board(destination):
                add_destination = False

            if add_destination and board.destination_captures_blue_piece(source, destination):
                add_destination = False

            if deep_check:
                board.try_move(source, destination)

                if add_destination and board.do_generals_face():
                    add_destination = False

                if add_destination and board.is_blue_in_check(deep_check=False):
                    add_destination = False

                board.undo_move()

            if add_destination:
                destinations[destination] = all_destinations[destination]

        return destinations


class RedSoldier(Soldier):
    """
    RedSoldier (Piece) handles finding soldier move destinations from source filtering moves with board layout
    """

    def all_destinations_from_source(self, source):
        """
        All red soldier destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        row = source[0]
        column = source[1]
        own_destination = (row, column)
        own_path = (source, own_destination)
        left_destination = (row, column - 1)
        left_path = (source, left_destination)
        down_destination = (row + 1, column)
        down_path = (source, down_destination)
        right_destination = (row, column + 1)
        right_path = (source, right_destination)
        destinations = {
            own_destination: own_path,
            left_destination: left_path,
            down_destination: down_path,
            right_destination: right_path
        }

        upper_left_blue_palace_source = (7, 3)
        upper_right_blue_palace_source = (7, 5)
        if source == upper_left_blue_palace_source or source == upper_right_blue_palace_source:
            diagonal_destination = (8, 4)
            diagonal_path = (source, diagonal_destination)
            destinations[diagonal_destination] = diagonal_path

        center_blue_palace_source = (8, 4)
        if source == center_blue_palace_source:
            left_diagonal_destination = (9, 3)
            left_diagonal_path = (source, left_diagonal_destination)
            right_diagonal_destination = (9, 5)
            right_diagonal_path = (source, right_diagonal_destination)
            destinations[left_diagonal_destination] = left_diagonal_path
            destinations[right_diagonal_destination] = right_diagonal_path

        return destinations

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Red soldier destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :param board: [Board]
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        all_destinations = self.all_destinations_from_source(source)
        destinations = dict()

        for destination in all_destinations:
            add_destination = True

            if not board.destination_in_board(destination):
                add_destination = False

            if add_destination and board.destination_captures_red_piece(source, destination):
                add_destination = False

            if deep_check:
                board.try_move(source, destination)

                if add_destination and board.do_generals_face():
                    add_destination = False

                if add_destination and board.is_red_in_check(deep_check=False):
                    add_destination = False

                board.undo_move()

            if add_destination:
                destinations[destination] = all_destinations[destination]

        return destinations
