import csv
from operator import attrgetter
from chess_player import Chessplayer


by_lname = attrgetter('lname')
by_fname = attrgetter('fname')
by_full_name = attrgetter('full_name')
# open csv file read file csv_reader
# parameter delimiter
# count line
# print

def read_csv(file):
    data = []
    # with open ('chess-players.csv', encoding = "utf-8")as csv_file:
    with open (file, encoding = "utf-8", mode='r')as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1 
            else:
                line_count +=1
                lname = row[0].strip()
                fname = row[1].strip()
                full_name = row[2].strip()
                country = row[3].strip()
                born = row[4].strip()
                died = row[5].strip()
                player = Chessplayer(lname,fname,full_name,country,born,died)
                data.append(player)
                #sort player's last name
                # data.sort(key=by_full_name)
        # print('processed lines :',line_count)
        # for x in data:
            # print("Last Name: " + x.lname  + ", " + "First Name: "+ x.fname + "," + x.country + x.born + ", "+ x.died)
        # print("Total of chess players are : ", str(len(data)))
        return data

    





