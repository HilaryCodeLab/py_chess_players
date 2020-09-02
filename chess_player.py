from dataclasses import dataclass
from collections import namedtuple

@dataclass(order=True)
class Chessplayer:
        lname: str 
        fname: str 
        full_name: str 
        country: str 
        born: str 
        died: str 

Chessplayer = namedtuple('Chessplayer', 'lname fname full_name country born died')




