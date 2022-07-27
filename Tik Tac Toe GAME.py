game = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
count = 0
while True:
    place = int(input("place 1--9 First one will be (X) and then (O): "))
    place -= 1
    if place < 9 and count < 9:
        if (count % 2) == 0:
            game[place] = "X"
            print(f"{game[6]} | {game[7]} | {game[8]}")
            print(f"{game[3]} | {game[4]} | {game[5]}")
            print(f"{game[0]} | {game[1]} | {game[2]}")
            count += 1
        elif (count % 2) == 1:
            game[place] = "O"
            print(f"{game[6]} | {game[7]} | {game[8]}")
            print(f"{game[3]} | {game[4]} | {game[5]}")
            print(f"{game[0]} | {game[1]} | {game[2]}")
            count += 1
    elif place >= 9:
        print("fuk you!! repeat")
    elif count > 10:
        print("Game Ends")
