# Author: Ethan Davis
# Date: 2/27/21
# Description: Janggi Korean chess guard piece


from Piece import Piece


class Guard(Piece):
    """
    Guard (Piece) handles finding guard move destinations from source filtering moves with board layout
    """

    def all_destinations_from_source(self, source):
        """
        Guard unfiltered destinations from source
        :param source: [Tuple[int]] Board source coordinate
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        row = source[0]
        column = source[1]
        own_destination = source
        own_path = (source, source)
        up_destination = (row - 1, column)
        up_path = (source, up_destination)
        up_right_destination = (row - 1, column + 1)
        up_right_path = (source, up_right_destination)
        right_destination = (row, column + 1)
        right_path = (source, right_destination)
        down_right_destination = (row + 1, column + 1)
        down_right_path = (source, down_right_destination)
        down_destination = (row + 1, column)
        down_path = (source, down_destination)
        down_left_destination = (row + 1, column - 1)
        down_left_path = (source, down_left_destination)
        left_destination = (row, column - 1)
        left_path = (source, left_destination)
        up_left_destination = (row - 1, column - 1)
        up_left_path = (source, up_left_destination)
        destinations = {
            own_destination: own_path,
            up_destination: up_path,
            up_right_destination: up_right_path,
            right_destination: right_path,
            down_right_destination: down_right_path,
            down_destination: down_path,
            down_left_destination: down_left_path,
            left_destination: left_path,
            up_left_destination: up_left_path
        }

        return destinations


class BlueGuard(Guard):
    """
    BlueGuard (Piece) handles finding guard move destinations from source filtering moves with board layout
    """

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Blue Guard destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :param board: [Board]
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        all_destinations = self.all_destinations_from_source(source)
        destinations = dict()

        for destination in all_destinations:
            add_destination = True

            if not board.destination_in_blue_palace(destination):
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


class RedGuard(Guard):
    """
    RedGuard (Piece) handles finding guard move destinations from source filtering moves with board layout
    """

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Red Guard destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :param board: [Board]
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        all_destinations = self.all_destinations_from_source(source)
        destinations = dict()

        for destination in all_destinations:
            add_destination = True

            if not board.destination_in_red_palace(destination):
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
