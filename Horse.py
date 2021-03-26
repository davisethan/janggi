# Author: Ethan Davis
# Date: 2/27/21
# Description: Janggi Korean chess horse piece


from Piece import Piece


class Horse(Piece):
    """
    Horse (Piece) handles finding horse move destinations from source filtering moves with board layout
    """

    def all_destinations_from_source(self, source):
        """
        Horse all destinations from source
        :param source: [Tuple[int]] Board source coordinate
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        row = source[0]
        column = source[1]
        own_destination = source
        own_path = (source, source)
        up_left_destination = (row - 2, column - 1)
        up_left_path = (source, (row - 1, column), up_left_destination)
        up_right_destination = (row - 2, column + 1)
        up_right_path = (source, (row - 1, column), up_right_destination)
        right_up_destination = (row - 1, column + 2)
        right_up_path = (source, (row, column + 1), right_up_destination)
        right_down_destination = (row + 1, column + 2)
        right_down_path = (source, (row, column + 1), right_down_destination)
        down_right_destination = (row + 2, column + 1)
        down_right_path = (source, (row + 1, column), down_right_destination)
        down_left_destination = (row + 2, column - 1)
        down_left_path = (source, (row + 1, column), down_left_destination)
        left_down_destination = (row + 1, column - 2)
        left_down_path = (source, (row, column - 1), left_down_destination)
        left_up_destination = (row - 1, column - 2)
        left_up_path = (source, (row, column - 1), left_up_destination)
        destinations = {
            own_destination: own_path,
            up_left_destination: up_left_path,
            up_right_destination: up_right_path,
            right_up_destination: right_up_path,
            right_down_destination: right_down_path,
            down_right_destination: down_right_path,
            down_left_destination: down_left_path,
            left_down_destination: left_down_path,
            left_up_destination: left_up_path
        }

        return destinations


class BlueHorse(Horse):
    """
    BlueHorse (Piece) handles finding horse move destinations from source filtering moves with board layout
    """

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Blue horse destinations from source with paths
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

            path = all_destinations[destination]
            if add_destination and board.horse_path_blocked(path):
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


class RedHorse(Horse):
    """
    RedHorse (Piece) handles finding horse move destinations from source filtering moves with board layout
    """

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Red horse destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :param board: [Board]
        :param deep_check: [bool] Must piece which checks other general protect own general
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        all_destinations = self.all_destinations_from_source(source)
        destinations = dict()

        for destination in all_destinations:
            add_destination = True

            if not board.destination_in_board(destination):
                add_destination = False

            path = all_destinations[destination]
            if add_destination and board.horse_path_blocked(path):
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
