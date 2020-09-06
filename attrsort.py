from read_csv import read_csv
from chess_player import Chessplayer
from operator import attrgetter
from binary_search import find

# setting variable to chess player's attribute
by_lname = attrgetter('lname')

arr = read_csv('chess-players.csv')
arr.sort(key=by_lname)

result = find(arr, value='Šulskis', key=by_lname)

if (result):
        print("Player found in the list")
        print(f'{result}')
    
else: 
    print("Not found Player") 