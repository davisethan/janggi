# Author: Ethan Davis
# Date: 2/27/21
# Description: Janggi Korean chess piece


class Piece:
    """
    Janggi Korean chess Piece handles finding move destinations from source filtering moves with Board layout
    """

    def all_destinations_from_source(self, source):
        """
        All destinations piece can move to from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]] Board destination coordinate goes to board source to destination path
        """
        pass

    def destinations_from_source(self, source, board, deep_check=True):
        """
        Destinations piece can move to from source with paths
        :param source: [Tuple[int]] Board source coordinate
        :param board: [Board]
        :param deep_check: [bool] Piece which checks other general must protect own general
        :return: [Dict[Tuple[int], Tuple[Tuple[int]]]
        """
        pass
