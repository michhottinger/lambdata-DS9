"""Classes to represent games"""

from random import random


class Game:
    def __init__(self, rounds=2, player1="Nicole", player2="Kumar"):
        self.rounds = 3
        self.steps = 5
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """
        Print the game players
        """
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_round(self):
        """
        Increment rounds by 1
        """
        self.rounds += 1

    def winner(self):
        """randomly pick and return winner"""
        return self.player1 if random() > 0.5 else self.player2


class Tic(Game):
    """
    Tictactoe subclass of Game
    """

    def __init__(self, rounds=3, player1='Superman', player2='Stephanie'):
        super().__init__(rounds, player1, player2)

    def print_players(self):
        print('{} is playing Tic Tac Toe with {}'.format(self.player1,
                                                         self.player2))
