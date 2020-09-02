from operator import attrgetter
from read_csv import read_csv

players = read_csv('chess-players.csv')
by_full_name = attrgetter('full_name')
players.sort(key=by_full_name)
for x in players:
            # print("Last Name: " + x.lname  + ", " + "First Name: "+ x.fname + "," + x.country)
            print("Full Name: "+ x.full_name + ", " + x.country + ", "+ x.born + ", "+ x.died)  