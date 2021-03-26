# Author: Ethan Davis
# Date: 2/27/21
# Description: Janggi Korean chess chariot piece


from Piece import Piece


class Chariot(Piece):
    """
    Chariot (Piece) handles finding chariot move destinations from source filtering moves with board layout
    """

    def all_destinations_from_source(self, source, board):
        """
        Chariot all destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        destinations = dict()
        destinations[source] = (source, source)
        destinations = {**destinations, **self.up_destinations_from_source(source, board)}
        destinations = {**destinations, **self.right_destinations_from_source(source, board)}
        destinations = {**destinations, **self.down_destinations_from_source(source, board)}
        destinations = {**destinations, **self.left_destinations_from_source(source, board)}
        destinations = {**destinations, **self.diagonal_destinations_from_lower_left_palace_source(source, board)}
        destinations = {**destinations, **self.diagonal_destinations_from_upper_left_palace_source(source, board)}
        destinations = {**destinations, **self.diagonal_destinations_from_upper_right_palace_source(source, board)}
        destinations = {**destinations, **self.diagonal_destinations_from_lower_right_palace_source(source, board)}
        destinations = {**destinations, **self.diagonal_destinations_from_center_palace_source(source, board)}
        return destinations


class BlueChariot(Chariot):
    """
    BlueChariot (Piece) handles finding chariot move destinations from source filtering moves with board layout
    """

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Blue chariot destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :param board: [Board]
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        all_destinations = self.all_destinations_from_source(source, board)
        destinations = dict()

        for destination in all_destinations:
            add_destination = True

            if deep_check:
                board.try_move(source, destination)

                if board.do_generals_face():
                    add_destination = False

                if add_destination and board.is_blue_in_check(deep_check=False):
                    add_destination = False

                board.undo_move()

            if add_destination:
                destinations[destination] = all_destinations[destination]

        return destinations

    def up_destinations_from_source(self, source, board):
        """
        Blue chariot up destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0] - 1
        column = source[1]
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        while piece is None and row >= board.get_rows_min():
            path += ((row, column),)
            destinations[(row, column)] = path
            row -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_red_pieces():
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def right_destinations_from_source(self, source, board):
        """
        Blue chariot right destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0]
        column = source[1] + 1
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        while piece is None and column < board.get_columns_max():
            path += ((row, column),)
            destinations[(row, column)] = path
            column += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_red_pieces():
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def down_destinations_from_source(self, source, board):
        """
        Blue chariot down destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0] + 1
        column = source[1]
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        while piece is None and row < board.get_rows_max():
            path += ((row, column),)
            destinations[(row, column)] = path
            row += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_red_pieces():
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def left_destinations_from_source(self, source, board):
        """
        Blue chariot left destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0]
        column = source[1] - 1
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        while piece is None and column >= board.get_columns_min():
            path += ((row, column),)
            destinations[(row, column)] = path
            column -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_red_pieces():
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def diagonal_destinations_from_upper_left_palace_source(self, source, board):
        """
        Blue chariot diagonal destinations from upper left palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_upper_left_corner_source = (7, 3)
        red_palace_upper_left_corner_source = (0, 3)
        if source == blue_palace_upper_left_corner_source or source == red_palace_upper_left_corner_source:
            row = source[0]
            column = source[1]
            path = (source,)
            piece = board.get_layout().get((row + 1, column + 1), None)
            if piece and type(piece) in board.get_red_pieces():
                path += ((row + 1, column + 1),)
                destinations[(row + 1, column + 1)] = path
            elif not piece:
                path += ((row + 1, column + 1),)
                destinations[(row + 1, column + 1)] = path
                piece = board.get_layout().get((row + 2, column + 2), None)
                if piece and type(piece) in board.get_red_pieces():
                    path += ((row + 2, column + 2),)
                    destinations[(row + 2, column + 2)] = path
                elif not piece:
                    path += ((row + 2, column + 2),)
                    destinations[(row + 2, column + 2)] = path

        return destinations

    def diagonal_destinations_from_upper_right_palace_source(self, source, board):
        """
        Blue chariot diagonal destinations from upper right palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_upper_right_corner_source = (7, 5)
        red_palace_upper_right_corner_source = (0, 5)
        if source == blue_palace_upper_right_corner_source or source == red_palace_upper_right_corner_source:
            row = source[0]
            column = source[1]
            path = (source,)
            piece = board.get_layout().get((row + 1, column - 1), None)
            if piece and type(piece) in board.get_red_pieces():
                path += ((row + 1, column - 1),)
                destinations[(row + 1, column - 1)] = path
            elif not piece:
                path += ((row + 1, column - 1),)
                destinations[(row + 1, column - 1)] = path
                piece = board.get_layout().get((row + 2, column - 2), None)
                if piece and type(piece) in board.get_red_pieces():
                    path += ((row + 2, column - 2),)
                    destinations[(row + 2, column - 2)] = path
                elif not piece:
                    path += ((row + 2, column - 2),)
                    destinations[(row + 2, column - 2)] = path

        return destinations

    def diagonal_destinations_from_lower_right_palace_source(self, source, board):
        """
        Blue chariot diagonal destinations from lower right palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_lower_right_corner_source = (9, 5)
        red_palace_lower_right_corner_source = (2, 5)
        if source == blue_palace_lower_right_corner_source or source == red_palace_lower_right_corner_source:
            row = source[0]
            column = source[1]
            path = (source,)
            piece = board.get_layout().get((row - 1, column - 1), None)
            if piece and type(piece) in board.get_red_pieces():
                path += ((row - 1, column - 1),)
                destinations[(row - 1, column - 1)] = path
            elif not piece:
                path += ((row - 1, column - 1),)
                destinations[(row - 1, column - 1)] = path
                piece = board.get_layout().get((row - 2, column - 2), None)
                if piece and type(piece) in board.get_red_pieces():
                    path += ((row - 2, column - 2),)
                    destinations[(row - 2, column - 2)] = path
                elif not piece:
                    path += ((row - 2, column - 2),)
                    destinations[(row - 2, column - 2)] = path

        return destinations

    def diagonal_destinations_from_lower_left_palace_source(self, source, board):
        """
        Blue chariot diagonal destinations from lower left palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_lower_left_corner_source = (9, 3)
        red_palace_lower_left_corner_source = (2, 3)
        if source == blue_palace_lower_left_corner_source or source == red_palace_lower_left_corner_source:
            row = source[0]
            column = source[1]
            path = (source,)
            piece = board.get_layout().get((row - 1, column + 1), None)
            if piece and type(piece) in board.get_red_pieces():
                path += ((row - 1, column + 1),)
                destinations[(row - 1, column + 1)] = path
            elif not piece:
                path += ((row - 1, column + 1),)
                destinations[(row - 1, column + 1)] = path
                piece = board.get_layout().get((row - 2, column + 2), None)
                if piece and type(piece) in board.get_red_pieces():
                    path += ((row - 2, column + 2),)
                    destinations[(row - 2, column + 2)] = path
                elif not piece:
                    path += ((row - 2, column + 2),)
                    destinations[(row - 2, column + 2)] = path

        return destinations

    def diagonal_destinations_from_center_palace_source(self, source, board):
        """
        Blue chariot diagonal destinations from center palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_center_source = (8, 4)
        red_palace_center_source = (1, 4)
        if source == blue_palace_center_source or source == red_palace_center_source:
            row = source[0]
            column = source[1]
            up_left_destination = (row - 1, column - 1)
            up_left_piece = board.get_layout().get(up_left_destination, None)
            up_right_destination = (row - 1, column + 1)
            up_right_piece = board.get_layout().get(up_right_destination, None)
            down_right_destination = (row + 1, column + 1)
            down_right_piece = board.get_layout().get(down_right_destination, None)
            down_left_destination = (row + 1, column - 1)
            down_left_piece = board.get_layout().get(down_left_destination, None)

            if up_left_piece and type(up_left_piece) in board.get_red_pieces():
                destinations[up_left_destination] = (source, up_left_destination)
            elif not up_left_piece:
                destinations[up_left_destination] = (source, up_left_destination)

            if up_right_piece and type(up_right_piece) in board.get_red_pieces():
                destinations[up_right_destination] = (source, up_right_destination)
            elif not up_right_piece:
                destinations[up_right_destination] = (source, up_right_destination)

            if down_right_piece and type(down_right_piece) in board.get_red_pieces():
                destinations[down_right_destination] = (source, down_right_destination)
            elif not down_right_piece:
                destinations[down_right_destination] = (source, down_right_destination)

            if down_left_piece and type(down_left_piece) in board.get_red_pieces():
                destinations[down_left_destination] = (source, down_left_destination)
            elif not down_left_piece:
                destinations[down_left_destination] = (source, down_left_destination)

        return destinations


class RedChariot(Chariot):
    """
    RedChariot (Piece) handles finding chariot move destinations from source filtering moves with board layout
    """

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Red chariot destinations from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :param board: [Board]
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Destination goes to source to destination path
        """
        all_destinations = self.all_destinations_from_source(source, board)
        destinations = dict()

        for destination in all_destinations:
            add_destination = True

            if deep_check:
                board.try_move(source, destination)

                if board.do_generals_face():
                    add_destination = False

                if add_destination and board.is_red_in_check(deep_check=False):
                    add_destination = False

                board.undo_move()

            if add_destination:
                destinations[destination] = all_destinations[destination]

        return destinations

    def up_destinations_from_source(self, source, board):
        """
        Red chariot up destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0] - 1
        column = source[1]
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        while piece is None and row >= board.get_rows_min():
            path += ((row, column),)
            destinations[(row, column)] = path
            row -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_blue_pieces():
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def right_destinations_from_source(self, source, board):
        """
        Red chariot right destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0]
        column = source[1] + 1
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        while piece is None and column < board.get_columns_max():
            path += ((row, column),)
            destinations[(row, column)] = path
            column += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_blue_pieces():
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def down_destinations_from_source(self, source, board):
        """
        Red chariot down destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0] + 1
        column = source[1]
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        while piece is None and row < board.get_rows_max():
            path += ((row, column),)
            destinations[(row, column)] = path
            row += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_blue_pieces():
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def left_destinations_from_source(self, source, board):
        """
        Red chariot left destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0]
        column = source[1] - 1
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        while piece is None and column >= board.get_columns_min():
            path += ((row, column),)
            destinations[(row, column)] = path
            column -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_blue_pieces():
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def diagonal_destinations_from_lower_left_palace_source(self, source, board):
        """
        Red chariot diagonal destinations from lower left palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_lower_left_corner_source = (9, 3)
        red_palace_lower_left_corner_source = (2, 3)
        if source == blue_palace_lower_left_corner_source or source == red_palace_lower_left_corner_source:
            row = source[0]
            column = source[1]
            path = (source,)
            piece = board.get_layout().get((row - 1, column + 1), None)
            if piece and type(piece) in board.get_blue_pieces():
                path += ((row - 1, column + 1),)
                destinations[(row - 1, column + 1)] = path
            elif not piece:
                path += ((row - 1, column + 1),)
                destinations[(row - 1, column + 1)] = path
                piece = board.get_layout().get((row - 2, column + 2), None)
                if piece and type(piece) in board.get_blue_pieces():
                    path += ((row - 2, column + 2),)
                    destinations[(row - 2, column + 2)] = path
                elif not piece:
                    path += ((row - 2, column + 2),)
                    destinations[(row - 2, column + 2)] = path

        return destinations

    def diagonal_destinations_from_upper_left_palace_source(self, source, board):
        """
        Red chariot diagonal destinations from upper left palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_upper_left_corner_source = (7, 3)
        red_palace_upper_left_corner_source = (0, 3)
        if source == blue_palace_upper_left_corner_source or source == red_palace_upper_left_corner_source:
            row = source[0]
            column = source[1]
            path = (source,)
            piece = board.get_layout().get((row + 1, column + 1), None)
            if piece and type(piece) in board.get_blue_pieces():
                path += ((row + 1, column + 1),)
                destinations[(row + 1, column + 1)] = path
            elif not piece:
                path += ((row + 1, column + 1),)
                destinations[(row + 1, column + 1)] = path
                piece = board.get_layout().get((row + 2, column + 2), None)
                if piece and type(piece) in board.get_blue_pieces():
                    path += ((row + 2, column + 2),)
                    destinations[(row + 2, column + 2)] = path
                elif not piece:
                    path += ((row + 2, column + 2),)
                    destinations[(row + 2, column + 2)] = path

        return destinations

    def diagonal_destinations_from_upper_right_palace_source(self, source, board):
        """
        Red chariot diagonal destinations from upper right palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_upper_right_corner_source = (7, 5)
        red_palace_upper_right_corner_source = (0, 5)
        if source == blue_palace_upper_right_corner_source or source == red_palace_upper_right_corner_source:
            row = source[0]
            column = source[1]
            path = (source,)
            piece = board.get_layout().get((row + 1, column - 1), None)
            if piece and type(piece) in board.get_blue_pieces():
                path += ((row + 1, column - 1),)
                destinations[(row + 1, column - 1)] = path
            elif not piece:
                path += ((row + 1, column - 1),)
                destinations[(row + 1, column - 1)] = path
                piece = board.get_layout().get((row + 2, column - 2), None)
                if piece and type(piece) in board.get_blue_pieces():
                    path += ((row + 2, column - 2),)
                    destinations[(row + 2, column - 2)] = path
                elif not piece:
                    path += ((row + 2, column - 2),)
                    destinations[(row + 2, column - 2)] = path

        return destinations

    def diagonal_destinations_from_lower_right_palace_source(self, source, board):
        """
        Red chariot diagonal destinations from lower right palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_lower_right_corner_source = (9, 5)
        red_palace_lower_right_corner_source = (2, 5)
        if source == blue_palace_lower_right_corner_source or source == red_palace_lower_right_corner_source:
            row = source[0]
            column = source[1]
            path = (source,)
            piece = board.get_layout().get((row - 1, column - 1), None)
            if piece and type(piece) in board.get_blue_pieces():
                path += ((row - 1, column - 1),)
                destinations[(row - 1, column - 1)] = path
            elif not piece:
                path += ((row - 1, column - 1),)
                destinations[(row - 1, column - 1)] = path
                piece = board.get_layout().get((row - 2, column - 2), None)
                if piece and type(piece) in board.get_blue_pieces():
                    path += ((row - 2, column - 2),)
                    destinations[(row - 2, column - 2)] = path
                elif not piece:
                    path += ((row - 2, column - 2),)
                    destinations[(row - 2, column - 2)] = path

        return destinations

    def diagonal_destinations_from_center_palace_source(self, source, board):
        """
        Red chariot diagonal destinations from center palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()

        blue_palace_center_source = (8, 4)
        red_palace_center_source = (1, 4)
        if source == blue_palace_center_source or source == red_palace_center_source:
            row = source[0]
            column = source[1]
            up_left_destination = (row - 1, column - 1)
            up_left_piece = board.get_layout().get(up_left_destination, None)
            up_right_destination = (row - 1, column + 1)
            up_right_piece = board.get_layout().get(up_right_destination, None)
            down_right_destination = (row + 1, column + 1)
            down_right_piece = board.get_layout().get(down_right_destination, None)
            down_left_destination = (row + 1, column - 1)
            down_left_piece = board.get_layout().get(down_left_destination, None)

            if up_left_piece and type(up_left_piece) in board.get_blue_pieces():
                destinations[up_left_destination] = (source, up_left_destination)
            elif not up_left_piece:
                destinations[up_left_destination] = (source, up_left_destination)

            if up_right_piece and type(up_right_piece) in board.get_blue_pieces():
                destinations[up_right_destination] = (source, up_right_destination)
            elif not up_right_piece:
                destinations[up_right_destination] = (source, up_right_destination)

            if down_right_piece and type(down_right_piece) in board.get_blue_pieces():
                destinations[down_right_destination] = (source, down_right_destination)
            elif not down_right_piece:
                destinations[down_right_destination] = (source, down_right_destination)

            if down_left_piece and type(down_left_piece) in board.get_blue_pieces():
                destinations[down_left_destination] = (source, down_left_destination)
            elif not down_left_piece:
                destinations[down_left_destination] = (source, down_left_destination)

        return destinations
