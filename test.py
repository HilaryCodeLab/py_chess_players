import unittest
from binary_search import binary_search 
from sort import bubble_sort
from read_csv import read_csv
import random
from chess_player import Chessplayer
from operator import attrgetter
from binary_search import find

class Test(unittest.TestCase):
    
    def setUp(self):
        
        self.chessPlayers = []
        self.playerA = Chessplayer('Corr','Fiona','Fiona Corr','USA','14/07/1998','n/a')
        self.playerB = Chessplayer('Patterson','Peter','Petter Patterson','UK','21/05/1957','n/a')
        self.playerC = Chessplayer('Ramsay','Gordon','Gordon Ramsey','UK','03/02/1977','n/a')
        self.chessPlayers.append(self.playerA)
        self.chessPlayers.append(self.playerB)
        self.chessPlayers.append(self.playerC)

        self.players = read_csv('chess-players.csv')
        # bubble_sort(self.players)


# test if non-player not found in the list 
    def test_search_not_found(self):
        bubble_sort(self.players)
        result = binary_search(self.players,self.playerA)
        self.assertNotEqual(result,self.playerA)
       

# test if right player found in the list 
    # def test_search_found(self):
    #     by_full_name = attrgetter('full_name')
    #     self.chessPlayers.sort(key='full_name')
    #     result = find(self.chessPlayers, value='Gordon Ramsey', key=by_full_name)
    #     self.assertEqual(result,0)


# test binary search method algorithm
    def test_binary_search(self):
        result = binary_search(self.chessPlayers, self.playerA)
        self.assertEqual(result,0)


# test bubble_sort method
    def test_bubble_sort(self):
        expected = [self.playerA,self.playerB,self.playerC]
        result = bubble_sort(self.chessPlayers)
        self.assertEqual(expected,result)

# check if bubble_sort method algorithm works properly
    def test_bubble_sort_algorithm(self):
        expected = [self.playerC,self.playerB,self.playerA]
        result = bubble_sort(self.chessPlayers)
        self.assertNotEqual(expected,result)

