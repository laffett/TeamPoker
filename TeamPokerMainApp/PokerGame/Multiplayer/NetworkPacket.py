from TeamPokerMainApp.Common.VariableDefinitions import *
from PyQt5.Qt import QMutex


class NetworkPacketClass:

    def __init__(self):

        # Player fields decided by the Player.
        # PINFO_tableSpot = 0
        # PINFO_status = 1
        # PINFO_name = 2
        # PINFO_icon = 3
        # PINFO_actionID = 4

        self.PLAYER_INFO_FIELDS = list((int(0), STATUS_EMPTY_SEAT, str(""), str(""), int(0)))

        # Player fields decided by the Dealer.
        # PGAME_moneyAvailable = 0
        # PGAME_dealerIcon = 1
        # PGAME_playerCards = 2

        self.PLAYER_GAME_FIELDS = list((float(0.0), str(""), [NO_CARD, NO_CARD]))

        # The complete network packet definition

        self.GAME_DATA_PACKET = {"Dealer": {"TableCards": [NO_CARD, NO_CARD, NO_CARD, NO_CARD, NO_CARD],
                                            "BurnedCards": int(0),
                                            "TablePot": float(0.0)},
                                 "PlayersInfo": {0: list.copy(self.PLAYER_INFO_FIELDS),  # this will be the host-dealer-client
                                                 1: list.copy(self.PLAYER_INFO_FIELDS),
                                                 2: list.copy(self.PLAYER_INFO_FIELDS),
                                                 3: list.copy(self.PLAYER_INFO_FIELDS),
                                                 4: list.copy(self.PLAYER_INFO_FIELDS),
                                                 5: list.copy(self.PLAYER_INFO_FIELDS),
                                                 6: list.copy(self.PLAYER_INFO_FIELDS),
                                                 7: list.copy(self.PLAYER_INFO_FIELDS)
                                                 },
                                 "PlayersGame": {0: list.copy(self.PLAYER_GAME_FIELDS),  # this will be the host-dealer-client
                                                 1: list.copy(self.PLAYER_GAME_FIELDS),
                                                 2: list.copy(self.PLAYER_GAME_FIELDS),
                                                 3: list.copy(self.PLAYER_GAME_FIELDS),
                                                 4: list.copy(self.PLAYER_GAME_FIELDS),
                                                 5: list.copy(self.PLAYER_GAME_FIELDS),
                                                 6: list.copy(self.PLAYER_GAME_FIELDS),
                                                 7: list.copy(self.PLAYER_GAME_FIELDS)
                                                 }
                                 }

    def get_game_data(self):
        return self.GAME_DATA_PACKET
