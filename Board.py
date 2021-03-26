# Author: Ethan Davis
# Date: 2/27/21
# Description: Janggi Korean chess board


from General import BlueGeneral, RedGeneral
from Guard import BlueGuard, RedGuard
from Chariot import BlueChariot, RedChariot
from Elephant import BlueElephant, RedElephant
from Horse import BlueHorse, RedHorse
from Cannon import BlueCannon, RedCannon
from Soldier import BlueSoldier, RedSoldier


class Board:
    """
    Janggi Korean chess board details handled by Board using Piece(s) reports findings to JanggiGame
    """

    def __init__(self, layout=None):
        """
        Create Janggi Korean chess Board

        :member _moves: [List[Tuple[Tuple[int]]]] Source and destination coordinates each move
        :member _layout_copies: [List[Dict[Tuple[int], Piece]]] Board layout copies
        :member _layout: [Dict[Tuple[int], Piece]] Board coordinates with Piece(s)
        """
        # Constants
        self._ROWS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self._COLUMNS = ("a", "b", "c", "d", "e", "f", "g", "h", "i")
        self._BLUE_PALACE_ROW_MIN = 7
        self._BLUE_PALACE_ROW_MAX = 9
        self._BLUE_PALACE_COLUMN_MIN = 3
        self._BLUE_PALACE_COLUMN_MAX = 5
        self._RED_PALACE_ROW_MIN = 0
        self._RED_PALACE_ROW_MAX = 2
        self._RED_PALACE_COLUMN_MIN = 3
        self._RED_PALACE_COLUMN_MAX = 5
        self._ROWS_MIN = 0
        self._ROWS_MAX = len(self._ROWS)
        self._COLUMNS_MIN = 0
        self._COLUMNS_MAX = len(self._COLUMNS)
        self._BLUE_PIECES = {BlueGeneral, BlueGuard, BlueChariot, BlueElephant, BlueHorse, BlueCannon, BlueSoldier}
        self._RED_PIECES = {RedGeneral, RedGuard, RedChariot, RedElephant, RedHorse, RedCannon, RedSoldier}

        self._moves = list()
        self._layout_copies = list()
        self._layout = {
            (0, 0): RedChariot(),
            (0, 1): RedElephant(),
            (0, 2): RedHorse(),
            (0, 3): RedGuard(),
            (0, 4): None,
            (0, 5): RedGuard(),
            (0, 6): RedElephant(),
            (0, 7): RedHorse(),
            (0, 8): RedChariot(),
            (1, 0): None,
            (1, 1): None,
            (1, 2): None,
            (1, 3): None,
            (1, 4): RedGeneral(),
            (1, 5): None,
            (1, 6): None,
            (1, 7): None,
            (1, 8): None,
            (2, 0): None,
            (2, 1): RedCannon(),
            (2, 2): None,
            (2, 3): None,
            (2, 4): None,
            (2, 5): None,
            (2, 6): None,
            (2, 7): RedCannon(),
            (2, 8): None,
            (3, 0): RedSoldier(),
            (3, 1): None,
            (3, 2): RedSoldier(),
            (3, 3): None,
            (3, 4): RedSoldier(),
            (3, 5): None,
            (3, 6): RedSoldier(),
            (3, 7): None,
            (3, 8): RedSoldier(),
            (4, 0): None,
            (4, 1): None,
            (4, 2): None,
            (4, 3): None,
            (4, 4): None,
            (4, 5): None,
            (4, 6): None,
            (4, 7): None,
            (4, 8): None,
            (5, 0): None,
            (5, 1): None,
            (5, 2): None,
            (5, 3): None,
            (5, 4): None,
            (5, 5): None,
            (5, 6): None,
            (5, 7): None,
            (5, 8): None,
            (6, 0): BlueSoldier(),
            (6, 1): None,
            (6, 2): BlueSoldier(),
            (6, 3): None,
            (6, 4): BlueSoldier(),
            (6, 5): None,
            (6, 6): BlueSoldier(),
            (6, 7): None,
            (6, 8): BlueSoldier(),
            (7, 0): None,
            (7, 1): BlueCannon(),
            (7, 2): None,
            (7, 3): None,
            (7, 4): None,
            (7, 5): None,
            (7, 6): None,
            (7, 7): BlueCannon(),
            (7, 8): None,
            (8, 0): None,
            (8, 1): None,
            (8, 2): None,
            (8, 3): None,
            (8, 4): BlueGeneral(),
            (8, 5): None,
            (8, 6): None,
            (8, 7): None,
            (8, 8): None,
            (9, 0): BlueChariot(),
            (9, 1): BlueElephant(),
            (9, 2): BlueHorse(),
            (9, 3): BlueGuard(),
            (9, 4): None,
            (9, 5): BlueGuard(),
            (9, 6): BlueElephant(),
            (9, 7): BlueHorse(),
            (9, 8): BlueChariot()
        }

        if layout:
            for position in self._layout:
                if position in layout:
                    self._layout[position] = layout[position]
                else:
                    self._layout[position] = None

    def __repr__(self):
        characters = {
            RedGeneral: "RG",
            RedGuard: "RU",
            RedChariot: "RC",
            RedElephant: "RE",
            RedHorse: "RH",
            RedCannon: "RA",
            RedSoldier: "RS",
            BlueGeneral: "BG",
            BlueGuard: "BU",
            BlueChariot: "BC",
            BlueElephant: "BE",
            BlueHorse: "BH",
            BlueCannon: "BA",
            BlueSoldier: "BS"
        }
        layout_string = ""
        layout_string += "  A  B  C  D  E  F  G  H  I\n"

        for row in range(self._ROWS_MAX):
            row_string = f"{row + 1}|"
            for column in range(self._COLUMNS_MAX):
                piece = self._layout[(row, column)]
                if piece:
                    row_string += f"{characters[type(piece)]}|"
                else:
                    row_string += "  |"
            row_string += "\n"
            layout_string += row_string

        return layout_string

    def get_rows_min(self):
        """
        Get _ROWS_MIN
        :return: [int]
        """
        return self._ROWS_MIN

    def get_rows_max(self):
        """
        Get _ROWS_MAX
        :return: [int]
        """
        return self._ROWS_MAX

    def get_columns_min(self):
        """
        Get _COLUMNS_MIN
        :return: [int]
        """
        return self._COLUMNS_MIN

    def get_columns_max(self):
        """
        Get _COLUMNS_MAX
        :return: [int]
        """
        return self._COLUMNS_MAX

    def get_blue_pieces(self):
        """
        Get _BLUE_PIECES
        :return: [Set[Piece]]
        """
        return self._BLUE_PIECES

    def get_red_pieces(self):
        """
        Get _RED_PIECES
        :return: [Set[Piece]]
        """
        return self._RED_PIECES

    def get_layout(self):
        """
        Get Janggi Korean chess board layout
        :return: (Dict[Tuple[int], Piece])
        """
        return self._layout

    def position_string_to_tuple(self, position_string):
        """
        Convert position string to position tuple
        :param position_string: [str] [a-i][1-10]
        :return: [Tuple[int]]
        """
        row = self._ROWS.index(position_string[1:])
        column = self._COLUMNS.index(position_string[:1])
        position_tuple = (row, column)
        return position_tuple

    def destination_in_blue_palace(self, destination):
        """
        Destination is in blue palace
        :param destination: [Tuple[int]] Board coordinate
        :return: [bool]
        """
        row = destination[0]
        column = destination[1]
        inside = True
        inside = inside and self._BLUE_PALACE_ROW_MIN <= row
        inside = inside and row <= self._BLUE_PALACE_ROW_MAX
        inside = inside and self._BLUE_PALACE_COLUMN_MIN <= column
        inside = inside and column <= self._BLUE_PALACE_COLUMN_MAX
        return inside

    def destination_in_red_palace(self, destination):
        """
        Destination is in red palace
        :param destination: [Tuple[int]] Board coordinate
        :return: [bool]
        """
        row = destination[0]
        column = destination[1]
        inside = True
        inside = inside and self._RED_PALACE_ROW_MIN <= row
        inside = inside and row <= self._RED_PALACE_ROW_MAX
        inside = inside and self._RED_PALACE_COLUMN_MIN <= column
        inside = inside and column <= self._RED_PALACE_COLUMN_MAX
        return inside

    def destination_in_board(self, destination):
        """
        Destination is in board
        :param destination: [Tuple[int]] Board coordinate
        :return: [bool]
        """
        row = destination[0]
        column = destination[1]
        inside = True
        inside = inside and self._ROWS_MIN <= row
        inside = inside and row < self._ROWS_MAX
        inside = inside and self._COLUMNS_MIN <= column
        inside = inside and column < self._COLUMNS_MAX
        return inside

    def destination_captures_blue_piece(self, source, destination):
        """
        Destination taken by blue piece
        :param source: [Tuple[int]] Board source coordinate
        :param destination: [Tuple[int]] Board destination coordinate
        :return: [bool]
        """
        captures_blue = False
        if source != destination:
            piece = self._layout.get(destination, None)
            if piece and type(piece) in self._BLUE_PIECES:
                captures_blue = True
        return captures_blue

    def destination_captures_red_piece(self, source, destination):
        """
        Destination taken by red piece
        :param source: [Tuple[int]] Board source coordinate
        :param destination: [Tuple[int]] Board destination coordinate
        :return: [bool]
        """
        captures_red = False
        if source != destination:
            piece = self._layout.get(destination, None)
            if piece and type(piece) in self._RED_PIECES:
                captures_red = True
        return captures_red

    def try_move(self, source, destination):
        """
        Try to move from source to destination with board copy
        :param source: [Tuple[int]] Board source coordinate
        :param destination: [Tuple[int]] Board destination coordinate
        :return: [None]
        """
        self._layout_copies.append(dict(self._layout))
        if source != destination:
            self._layout[destination] = self._layout[source]
            self._layout[source] = None

    def undo_move(self):
        """
        Undo tried move by restoring layout from layout copy
        :return: [None]
        """
        self._layout = self._layout_copies.pop()

    def do_generals_face(self):
        """
        Generals are face to face
        :return: [bool]
        """
        blue_general_source = self.blue_general_source()
        red_general_source = self.red_general_source()
        do_generals_face = False

        if blue_general_source != tuple() and red_general_source != tuple():
            row = blue_general_source[0] - 1
            column = blue_general_source[1]
            piece = self._layout.get((row, column), None)
            while piece is None and row >= self._ROWS_MIN:
                row -= 1
                piece = self._layout.get((row, column), None)
            if piece is not None and (row, column) == red_general_source:
                do_generals_face = True

        return do_generals_face

    def blue_general_source(self):
        """
        Blue general source
        :return: [Tuple[int]] Board coordinate
        """
        blue_general_source = tuple()
        for source in self._layout:
            piece = self._layout[source]
            if piece and isinstance(piece, BlueGeneral):
                blue_general_source = source
        return blue_general_source

    def red_general_source(self):
        """
        Red general source
        :return: [Tuple[int]] Board coordinate
        """
        red_general_source = tuple()
        for source in self._layout:
            piece = self._layout[source]
            if piece and isinstance(piece, RedGeneral):
                red_general_source = source
        return red_general_source

    def elephant_path_blocked(self, path):
        """
        Elephant path blocked by another piece
        :param path: [Tuple[Tuple[int]]] Ordered board coordinates
        :return: [bool]
        """
        source = path[0]
        destination = path[-1]
        elephant_path_blocked = False
        if source != destination:
            elephant_path_blocked = self._layout[path[1]] is not None or self._layout[path[2]] is not None
        return elephant_path_blocked

    def horse_path_blocked(self, path):
        """
        Horse path blocked by another piece
        :param path: [Tuple[Tuple[int]]] Ordered board coordinates
        :return: [bool]
        """
        source = path[0]
        destination = path[-1]
        horse_path_blocked = False
        if source != destination:
            horse_path_blocked = self._layout[path[1]] is not None
        return horse_path_blocked

    def is_blue_in_check(self, deep_check=True):
        """
        Blue general is in check
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [bool]
        """
        blue_general_source = self.blue_general_source()
        is_in_check = False

        for source in self._layout:
            piece = self._layout[source]
            if piece and type(piece) in self._RED_PIECES:
                destinations = piece.destinations_from_source(source, self, deep_check)
                if blue_general_source in destinations:
                    is_in_check = True

        return is_in_check

    def is_red_in_check(self, deep_check=True):
        """
        Red general is in check
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [bool]
        """
        red_general_source = self.red_general_source()
        is_in_check = False

        for source in self._layout:
            piece = self._layout[source]
            if piece and type(piece) in self._BLUE_PIECES:
                destinations = piece.destinations_from_source(source, self, deep_check)
                if red_general_source in destinations:
                    is_in_check = True

        return is_in_check

    def is_blue_in_checkmate(self):
        """
        Blue General is in checkmate
        :return: [bool]
        """
        cannot_move = not self.can_move_blue_general()
        cannot_capture_red_attacker = not self.can_capture_blue_general_attacker()
        cannot_block_red_attacker = not self.can_block_blue_general_attacker()
        is_in_checkmate = cannot_move and cannot_capture_red_attacker and cannot_block_red_attacker
        return is_in_checkmate

    def is_red_in_checkmate(self):
        """
        Red General is in checkmate
        :return: [bool]
        """
        cannot_move = not self.can_move_red_general()
        cannot_capture_blue_attacker = not self.can_capture_red_general_attacker()
        cannot_block_blue_attacker = not self.can_block_red_general_attacker()
        is_in_checkmate = cannot_move and cannot_capture_blue_attacker and cannot_block_blue_attacker
        return is_in_checkmate

    def length_moves_even(self):
        """
        Number of game moves is even
        :return: [bool]
        """
        return len(self._moves) % 2 == 0

    def length_moves_odd(self):
        """
        Number of games moves is odd
        :return: [bool]
        """
        return len(self._moves) % 2 == 1

    def piece_at_source(self, source):
        """
        Piece at source in board
        :param source: [Tuple[int]] Board coordinate
        :return: [bool]
        """
        piece = self._layout[source]
        return piece is not None

    def piece_at_source_has_turn(self, source):
        """
        Piece at source in board has turn
        :param source: [Tuple[int]] Board coordinate
        :return: [bool]
        """
        has_turn = False
        piece = self._layout[source]

        if piece and type(piece) in self._BLUE_PIECES and self.length_moves_even():
            has_turn = True
        elif piece and type(piece) in self._RED_PIECES and self.length_moves_odd():
            has_turn = True

        return has_turn

    def legal_move(self, source, destination):
        """
        Legal move from source to destination
        :param source: [Tuple[int]] Board source coordinate
        :param destination: [Tuple[int]] Board source coordinate
        :return: [bool]
        """
        piece = self._layout[source]
        return piece and destination in piece.destinations_from_source(source, self)

    def do_move(self, source, destination):
        """
        Do move from source to destination
        :param source: [Tuple[int]] Board source coordinate
        :param destination: [Tuple[int]]] Board destination coordinate
        :return: [None]
        """
        # Do move
        if source != destination:
            self._layout[destination] = self._layout[source]
            self._layout[source] = None

        # Log move
        move = (source, destination)
        self._moves.append(move)

    def can_move_blue_general(self):
        """
        Blue General can move somewhere
        :return: [bool]
        """
        blue_general_source = self.blue_general_source()
        piece = self._layout[blue_general_source]
        destinations = piece.destinations_from_source(blue_general_source, self)
        return len(destinations) > 0

    def can_move_red_general(self):
        """
        Red General can move somewhere
        :return: [bool]
        """
        red_general_source = self.red_general_source()
        piece = self._layout[red_general_source]
        destinations = piece.destinations_from_source(red_general_source, self)
        return len(destinations) > 0

    def blue_sources_with_destination(self, destination):
        """
        Blue piece sources which can move to destination
        :param destination: [Tuple[int]] Board coordinate
        :return: [Set[Tuple[int]]] Unordered board source coordinates which can move to board destination coordinate
        """
        blue_sources = set()

        for source in self._layout:
            piece = self._layout[source]
            if piece and type(piece) in self._BLUE_PIECES and destination in piece.destinations_from_source(source, self):
                blue_sources.add(source)

        return blue_sources

    def red_sources_with_destination(self, destination):
        """
        Red piece sources which can move to destination
        :param destination: [Tuple[int]] Board coordinate
        :return: [Set[Tuple[int]]] Unordered board source coordinates which can move to board destination coordinate
        """
        red_sources = set()

        for source in self._layout:
            piece = self._layout[source]
            if piece and type(piece) in self._RED_PIECES and destination in piece.destinations_from_source(source, self):
                red_sources.add(source)

        return red_sources

    def blue_paths_with_destination(self, destination):
        """
        Blue piece paths which move to destination
        :param destination: [Tuple[int]] Board destination coordinate
        :return: [Set[Tuple[Tuple[int]]]] Unordered coordinate paths from source to destination
        """
        blue_paths = set()

        for source in self._layout:
            piece = self._layout[source]
            if piece and type(piece) in self._BLUE_PIECES:
                destinations = piece.destinations_from_source(source, self)
                if destination in destinations:
                    blue_paths.add(destinations[destination])

        return blue_paths

    def red_paths_with_destination(self, destination):
        """
        Red piece paths which move to destination
        :param destination: [Tuple[int]] Board destination coordinate
        :return: [Set[Tuple[Tuple[int]]]] Unordered coordinate paths from source to destination
        """
        red_paths = set()

        for source in self._layout:
            piece = self._layout[source]
            if piece and type(piece) in self._RED_PIECES:
                destinations = piece.destinations_from_source(source, self)
                if destination in destinations:
                    red_paths.add(destinations[destination])

        return red_paths

    def can_capture_blue_general_attacker(self):
        """
        Blue General attacker can be captured
        :return: [bool]
        """
        can_capture_blue_general_attacker = False
        blue_general_source = self.blue_general_source()
        red_attacker_sources = self.red_sources_with_destination(blue_general_source)

        for red_attacker_source in red_attacker_sources:
            blue_protector_sources = self.blue_sources_with_destination(red_attacker_source)
            for blue_protector_source in blue_protector_sources:
                self.try_move(blue_protector_source, red_attacker_source)
                blue_in_check = self.is_blue_in_check(deep_check=False)
                if not blue_in_check:
                    can_capture_blue_general_attacker = True
                self.undo_move()

        return can_capture_blue_general_attacker

    def can_capture_red_general_attacker(self):
        """
        Red General attacker can be captured
        :return: [bool]
        """
        can_capture_red_general_attacker = False
        red_general_source = self.red_general_source()
        blue_attacker_sources = self.blue_sources_with_destination(red_general_source)

        for blue_attacker_source in blue_attacker_sources:
            red_protector_sources = self.red_sources_with_destination(blue_attacker_source)
            for red_protector_source in red_protector_sources:
                self.try_move(red_protector_source, blue_attacker_source)
                red_in_check = self.is_red_in_check(deep_check=False)
                if not red_in_check:
                    can_capture_red_general_attacker = True
                self.undo_move()

        return can_capture_red_general_attacker

    def can_block_blue_general_attacker(self):
        """
        Blue General attacker can be blocked
        :return: [bool]
        """
        can_block_blue_general_attacker = False
        blue_general_source = self.blue_general_source()
        red_attacker_paths = self.red_paths_with_destination(blue_general_source)

        for red_attacker_path in red_attacker_paths:
            for destination in red_attacker_path[1:-1]:
                blue_protector_sources = self.blue_sources_with_destination(destination)
                for blue_protector_source in blue_protector_sources:
                    self.try_move(blue_protector_source, destination)
                    blue_in_check = self.is_blue_in_check(deep_check=False)
                    if not blue_in_check:
                        can_block_blue_general_attacker = True
                    self.undo_move()

        return can_block_blue_general_attacker

    def can_block_red_general_attacker(self):
        """
        Red General attacker can be blocked
        :return: [bool]
        """
        can_block_red_general_attacker = False
        red_general_source = self.red_general_source()
        blue_attacker_paths = self.blue_paths_with_destination(red_general_source)

        for blue_attacker_path in blue_attacker_paths:
            for destination in blue_attacker_path[1:-1]:
                red_protector_sources = self.red_sources_with_destination(destination)
                for red_protector_source in red_protector_sources:
                    self.try_move(red_protector_source, destination)
                    red_in_check = self.is_red_in_check(deep_check=False)
                    if not red_in_check:
                        can_block_red_general_attacker = True
                    self.undo_move()

        return can_block_red_general_attacker
