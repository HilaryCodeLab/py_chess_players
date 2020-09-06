from dataclasses import dataclass
from collections import namedtuple

@dataclass(order=True)
# parameter order set to true, so __lt__(), __le__(),__gt__(),__ge__() are generated
class Chessplayer:
        lname: str 
        fname: str 
        full_name: str 
        country: str 
        born: str 
        died: str 

# Chessplayer = namedtuple('Chessplayer', 'lname fname full_name country born died')

# Define magic operator methods (lt, le, gt, ge, eq, ne) as follow:

def __lt__(self,other):
        player1 = Chessplayer(self.lname,self.fname,self.full_name,self.country,self.born,self.died)
        player2 = Chessplayer(other.lname,other.fname,other.full_name,other.country,other.born,other.died)
        return player1 < player2


def __ge__(self,other):
        return not self.__lt__(other)


def __gt__(self,other):
        player1 = Chessplayer(self.lname,self.fname,self.full_name,self.country,self.born,self.died)
        player2 = Chessplayer(other.lname,other.fname,other.full_name,other.country,other.born,other.died)
        return player1 > player2


def __le__(self,other):
        return not self.__gt__(other)


def __eq__(self,other):
        player1 = Chessplayer(self.lname,self.fname,self.full_name,self.country,self.born,self.died)
        player2 = Chessplayer(other.lname,other.fname,other.full_name,other.country,other.born,other.died)
        return player1 == player2


def __ne__(self,other):
        return not self.__eq__(other)


def print_details(self):
        print(f'First Name: {self.fname}, Last Name:{self.lname}, Country:{self.country}, Born:{self.born}, Died:{self.died}')





