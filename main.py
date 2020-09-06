from binary_search import binary_search 
from sort import bubble_sort
from read_csv import read_csv
from chess_player import Chessplayer


arr = read_csv('chess-players.csv')
sub_players = read_csv('players.csv')


# sort players using bubble sort algarithm
bubble_sort(arr)


#find player 
for player in sub_players:
    print('****** Searching in progress.... *****')
    result = binary_search(arr,player)

    if (result):
            print("Player found in the list")
            print(f'First Name: {arr[result].fname}, Last Name: {arr[result].lname}, Country: {arr[result].country}, Born: {arr[result].born}, Died: {arr[result].died}')
        
    else: 
        print("Not found Player") 