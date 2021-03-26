# Author: Ethan Davis
# Date: 2/27/21
# Description: Janggi Korean chess cannon piece


from Piece import Piece


class Cannon(Piece):
    """
    Janggi Korean chess Cannon (Piece) handles finding cannon move destinations from source filtering moves with board layout
    """

    def all_destinations_from_source(self, source, board):
        """
        Cannon all destinations from source with paths
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
        return destinations


class BlueCannon(Cannon):
    """
    BlueCannon (Piece) handles finding cannon move destinations from source filtering moves with board layout
    """

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Blue cannon destinations from source with paths
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
        Blue cannon up destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0] - 1
        column = source[1]
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        # Find up jump piece

        while piece is None and row >= board.get_rows_min():
            row -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) not in {BlueCannon, RedCannon}:
            row -= 1
            piece = board.get_layout().get((row, column), None)

        # Find paths after up jump piece

        while piece is None and row >= board.get_rows_min():
            path += ((row, column),)
            destinations[(row, column)] = path
            row -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_red_pieces() and not isinstance(piece, RedCannon):
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def right_destinations_from_source(self, source, board):
        """
        Blue cannon right destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0]
        column = source[1] + 1
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        # Find jump piece

        while piece is None and column < board.get_columns_max():
            column += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) not in {BlueCannon, RedCannon}:
            column += 1
            piece = board.get_layout().get((row, column), None)

        # Find paths after jump piece

        while piece is None and column < board.get_columns_max():
            path += ((row, column),)
            destinations[(row, column)] = path
            column += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_red_pieces() and not isinstance(piece, RedCannon):
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def down_destinations_from_source(self, source, board):
        """
        Blue cannon down destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0] + 1
        column = source[1]
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        # Find jump piece

        while piece is None and row < board.get_rows_max():
            row += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) not in {BlueCannon, RedCannon}:
            row += 1
            piece = board.get_layout().get((row, column), None)

        # Find paths after jump piece

        while piece is None and row < board.get_rows_max():
            path += ((row, column),)
            destinations[(row, column)] = path
            row += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_red_pieces() and not isinstance(piece, RedCannon):
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def left_destinations_from_source(self, source, board):
        """
        Blue cannon left destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0]
        column = source[1] - 1
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        # Find jump piece

        while piece is None and column >= board.get_columns_min():
            column -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) not in {BlueCannon, RedCannon}:
            column -= 1
            piece = board.get_layout().get((row, column), None)

        # Find paths after jump piece

        while piece is None and column >= board.get_columns_min():
            path += ((row, column),)
            destinations[(row, column)] = path
            column -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_red_pieces() and not isinstance(piece, RedCannon):
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def diagonal_destinations_from_lower_left_palace_source(self, source, board):
        """
        Blue cannon diagonal destinations from lower left palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        lower_left_blue_palace_source = (9, 3)
        lower_left_red_palace_source = (2, 3)

        if source == lower_left_blue_palace_source or source == lower_left_red_palace_source:
            row = source[0]
            column = source[1]
            center_source = (row - 1, column + 1)
            center_piece = board.get_layout().get(center_source, None)
            upper_right_corner_source = (row - 2, column + 2)
            upper_right_corner_piece = board.get_layout().get(upper_right_corner_source, None)

            center_piece_ok = center_piece is not None and type(center_piece) not in {BlueCannon, RedCannon}
            upper_right_corner_piece_ok = upper_right_corner_piece is None or (upper_right_corner_piece is not None and type(upper_right_corner_piece) in board.get_red_pieces() and not isinstance(upper_right_corner_piece, RedCannon))
            if center_piece_ok and upper_right_corner_piece_ok:
                destinations[upper_right_corner_source] = (source, upper_right_corner_source)

        return destinations

    def diagonal_destinations_from_upper_left_palace_source(self, source, board):
        """
        Blue cannon diagonal destinations from upper left palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        upper_left_blue_palace_source = (7, 3)
        upper_left_red_palace_source = (0, 3)

        if source == upper_left_blue_palace_source or source == upper_left_red_palace_source:
            row = source[0]
            column = source[1]
            center_source = (row + 1, column + 1)
            center_piece = board.get_layout().get(center_source, None)
            lower_right_corner_source = (row + 2, column + 2)
            lower_right_corner_piece = board.get_layout().get(lower_right_corner_source, None)

            center_piece_ok = center_piece is not None and type(center_piece) not in {BlueCannon, RedCannon}
            lower_right_corner_piece_ok = lower_right_corner_piece is None or (lower_right_corner_piece is not None and type(lower_right_corner_piece) in board.get_red_pieces() and not isinstance(lower_right_corner_piece, RedCannon))
            if center_piece_ok and lower_right_corner_piece_ok:
                destinations[lower_right_corner_source] = (source, lower_right_corner_source)

        return destinations

    def diagonal_destinations_from_upper_right_palace_source(self, source, board):
        """
        Blue cannon diagonal destinations from upper right palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        upper_right_blue_palace_source = (7, 5)
        upper_right_red_palace_source = (0, 5)

        if source == upper_right_blue_palace_source or source == upper_right_red_palace_source:
            row = source[0]
            column = source[1]
            center_source = (row + 1, column - 1)
            center_piece = board.get_layout().get(center_source, None)
            lower_left_corner_source = (row + 2, column - 2)
            lower_left_corner_piece = board.get_layout().get(lower_left_corner_source, None)

            center_piece_ok = center_piece is not None and type(center_piece) not in {BlueCannon, RedCannon}
            lower_left_corner_piece_ok = lower_left_corner_piece is None or (lower_left_corner_piece is not None and type(lower_left_corner_piece) in board.get_red_pieces() and not isinstance(lower_left_corner_piece, RedCannon))
            if center_piece_ok and lower_left_corner_piece_ok:
                destinations[lower_left_corner_source] = (source, lower_left_corner_source)

        return destinations

    def diagonal_destinations_from_lower_right_palace_source(self, source, board):
        """
        Blue cannon diagonal destinations from lower right palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        lower_right_blue_palace_source = (9, 5)
        lower_right_red_palace_source = (2, 5)

        if source == lower_right_blue_palace_source or source == lower_right_red_palace_source:
            row = source[0]
            column = source[1]
            center_source = (row - 1, column - 1)
            center_piece = board.get_layout().get(center_source, None)
            upper_left_corner_source = (row - 2, column - 2)
            upper_left_corner_piece = board.get_layout().get(upper_left_corner_source, None)

            center_piece_ok = center_piece is not None and type(center_piece) not in {BlueCannon, RedCannon}
            upper_left_corner_piece_ok = upper_left_corner_piece is None or (upper_left_corner_piece is not None and type(upper_left_corner_piece) in board.get_red_pieces() and not isinstance(upper_left_corner_piece, RedCannon))
            if center_piece_ok and upper_left_corner_piece_ok:
                destinations[upper_left_corner_source] = (source, upper_left_corner_source)

        return destinations


class RedCannon(Cannon):
    """
    RedCannon (Piece) handles finding cannon move destinations from source filtering moves with board layout
    """

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Red cannon destinations from source with paths
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
        Red cannon up destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0] - 1
        column = source[1]
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        # Find up jump piece

        while piece is None and row >= board.get_rows_min():
            row -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) not in {BlueCannon, RedCannon}:
            row -= 1
            piece = board.get_layout().get((row, column), None)

        # Find paths after up jump piece

        while piece is None and row >= board.get_rows_min():
            path += ((row, column),)
            destinations[(row, column)] = path
            row -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_blue_pieces() and not isinstance(piece, BlueCannon):
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def right_destinations_from_source(self, source, board):
        """
        Red cannon right destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0]
        column = source[1] + 1
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        # Find jump piece

        while piece is None and column < board.get_columns_max():
            column += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) not in {BlueCannon, RedCannon}:
            column += 1
            piece = board.get_layout().get((row, column), None)

        # Find paths after jump piece

        while piece is None and column < board.get_columns_max():
            path += ((row, column),)
            destinations[(row, column)] = path
            column += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_blue_pieces() and not isinstance(piece, BlueCannon):
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def down_destinations_from_source(self, source, board):
        """
        Red cannon down destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0] + 1
        column = source[1]
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        # Find jump piece

        while piece is None and row < board.get_rows_max():
            row += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) not in {BlueCannon, RedCannon}:
            row += 1
            piece = board.get_layout().get((row, column), None)

        # Find paths after jump piece

        while piece is None and row < board.get_rows_max():
            path += ((row, column),)
            destinations[(row, column)] = path
            row += 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_blue_pieces() and not isinstance(piece, BlueCannon):
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def left_destinations_from_source(self, source, board):
        """
        Red cannon left destinations from source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        row = source[0]
        column = source[1] - 1
        path = (source,)
        piece = board.get_layout().get((row, column), None)

        # Find jump piece

        while piece is None and column >= board.get_columns_min():
            column -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) not in {BlueCannon, RedCannon}:
            column -= 1
            piece = board.get_layout().get((row, column), None)

        # Find paths after jump piece

        while piece is None and column >= board.get_columns_min():
            path += ((row, column),)
            destinations[(row, column)] = path
            column -= 1
            piece = board.get_layout().get((row, column), None)

        if piece is not None and type(piece) in board.get_blue_pieces() and not isinstance(piece, BlueCannon):
            path += ((row, column),)
            destinations[(row, column)] = path

        return destinations

    def diagonal_destinations_from_lower_left_palace_source(self, source, board):
        """
        Red cannon diagonal destinations from lower left palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        lower_left_blue_palace_source = (9, 3)
        lower_left_red_palace_source = (2, 3)

        if source == lower_left_blue_palace_source or source == lower_left_red_palace_source:
            row = source[0]
            column = source[1]
            center_source = (row - 1, column + 1)
            center_piece = board.get_layout().get(center_source, None)
            upper_right_corner_source = (row - 2, column + 2)
            upper_right_corner_piece = board.get_layout().get(upper_right_corner_source, None)

            center_piece_ok = center_piece is not None and type(center_piece) not in {BlueCannon, RedCannon}
            upper_right_corner_piece_ok = upper_right_corner_piece is None or (upper_right_corner_piece is not None and type(upper_right_corner_piece) in board.get_blue_pieces() and not isinstance(upper_right_corner_piece, BlueCannon))
            if center_piece_ok and upper_right_corner_piece_ok:
                destinations[upper_right_corner_source] = (source, upper_right_corner_source)

        return destinations

    def diagonal_destinations_from_upper_left_palace_source(self, source, board):
        """
        Red cannon diagonal destinations from upper left palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        upper_left_blue_palace_source = (7, 3)
        upper_left_red_palace_source = (0, 3)

        if source == upper_left_blue_palace_source or source == upper_left_red_palace_source:
            row = source[0]
            column = source[1]
            center_source = (row + 1, column + 1)
            center_piece = board.get_layout().get(center_source, None)
            lower_right_corner_source = (row + 2, column + 2)
            lower_right_corner_piece = board.get_layout().get(lower_right_corner_source, None)

            center_piece_ok = center_piece is not None and type(center_piece) not in {BlueCannon, RedCannon}
            lower_right_corner_piece_ok = lower_right_corner_piece is None or (lower_right_corner_piece is not None and type(lower_right_corner_piece) in board.get_blue_pieces() and not isinstance(lower_right_corner_piece, BlueCannon))
            if center_piece_ok and lower_right_corner_piece_ok:
                destinations[lower_right_corner_source] = (source, lower_right_corner_source)

        return destinations

    def diagonal_destinations_from_upper_right_palace_source(self, source, board):
        """
        Red cannon diagonal destinations from upper right palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        upper_right_blue_palace_source = (7, 5)
        upper_right_red_palace_source = (0, 5)

        if source == upper_right_blue_palace_source or source == upper_right_red_palace_source:
            row = source[0]
            column = source[1]
            center_source = (row + 1, column - 1)
            center_piece = board.get_layout().get(center_source, None)
            lower_left_corner_source = (row + 2, column - 2)
            lower_left_corner_piece = board.get_layout().get(lower_left_corner_source, None)

            center_piece_ok = center_piece is not None and type(center_piece) not in {BlueCannon, RedCannon}
            lower_left_corner_piece_ok = lower_left_corner_piece is None or (lower_left_corner_piece is not None and type(lower_left_corner_piece) in board.get_blue_pieces() and not isinstance(lower_left_corner_piece, BlueCannon))
            if center_piece_ok and lower_left_corner_piece_ok:
                destinations[lower_left_corner_source] = (source, lower_left_corner_source)

        return destinations

    def diagonal_destinations_from_lower_right_palace_source(self, source, board):
        """
        Red cannon diagonal destinations from lower right palace source with paths
        :param source: [Tuple[int]]
        :param board: [Board]
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]]
        """
        destinations = dict()
        lower_right_blue_palace_source = (9, 5)
        lower_right_red_palace_source = (2, 5)

        if source == lower_right_blue_palace_source or source == lower_right_red_palace_source:
            row = source[0]
            column = source[1]
            center_source = (row - 1, column - 1)
            center_piece = board.get_layout().get(center_source, None)
            upper_left_corner_source = (row - 2, column - 2)
            upper_left_corner_piece = board.get_layout().get(upper_left_corner_source, None)

            center_piece_ok = center_piece is not None and type(center_piece) not in {BlueCannon, RedCannon}
            upper_left_corner_piece_ok = upper_left_corner_piece is None or (upper_left_corner_piece is not None and type(upper_left_corner_piece) in board.get_blue_pieces() and not isinstance(upper_left_corner_piece, BlueCannon))
            if center_piece_ok and upper_left_corner_piece_ok:
                destinations[upper_left_corner_source] = (source, upper_left_corner_source)

        return destinations
