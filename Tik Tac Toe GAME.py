game = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
allReady = []
count = 0
place = 0
print("\t============================  Tik Tak Toe  ============================ ")
print("\tHey There !\n")
print("\tThe Game Layout is mapped to your Numpad As Shown Down\n")
print("\t\t\t7 | 8 | 9")
print("\t\t\t4 | 5 | 6")
print("\t\t\t1 | 2 | 3\n")

input("\tPress Enter To Continue\n")
while True:
    try:
        if place < 9 and count < 9:
            if (count % 2) == 0:
                x = input("\tPlayer (X): \n").casefold()
                place = int(x)
                place -= 1
                if place not in allReady:
                    allReady.append(place)
                    game[place] = "X"
                    print(f"\t{game[6]} | {game[7]} | {game[8]}")
                    print(f"\t{game[3]} | {game[4]} | {game[5]}")
                    print(f"\t{game[0]} | {game[1]} | {game[2]} \n")
                    count += 1
                    if (game[6] == "X" and game[7] == "X" and game[8] == "X") or (game[6] == "X" and game[3] == "X" and game[0] == "X") or (game[6] == "X" and game[4] == "X" and game[2] == "X") or (game[8] == "X" and game[5] == "X" and game[2] == "X") or (game[0] == "X" and game[1] == "X" and game[2] == "X") or (game[7] == "X" and game[4] == "X" and game[1] == "X") or (game[3] == "X" and game[4] == "X" and game[5] == "X") or (game[0] == "X" and game[4] == "X" and game[8] == "X"):
                        print("Congrate Player (X) won")
                        input()
                        input()
                        break
                    if (game[6] == "O" and game[7] == "O" and game[8] == "O") or (game[6] == "O" and game[3] == "O" and game[0] == "O") or (game[6] == "O" and game[4] == "O" and game[2] == "O") or (game[8] == "O" and game[5] == "O" and game[2] == "O") or (game[0] == "O" and game[1] == "O" and game[2] == "O") or (game[7] == "O" and game[4] == "O" and game[1] == "O") or (game[3] == "O" and game[4] == "O" and game[5] == "O") or (game[0] == "O" and game[4] == "O" and game[8] == "O"):
                        print("Congrate Player (O) won")
                        input()
                        input()
                        break
                else:
                    print("Can't play there !!!")
                    continue
            elif (count % 2) == 1:
                x = input("\tPlayer (O): \n").casefold()
                place = int(x)
                place -= 1
                if place not in allReady:
                    allReady.append(place)
                    game[place] = "O"
                    print(f"\t{game[6]} | {game[7]} | {game[8]}")
                    print(f"\t{game[3]} | {game[4]} | {game[5]}")
                    print(f"\t{game[0]} | {game[1]} | {game[2]} \n")
                    count += 1
                    if (game[6] == "X" and game[7] == "X" and game[8] == "X") or (game[6] == "X" and game[3] == "X" and game[0] == "X") or (game[6] == "X" and game[4] == "X" and game[2] == "X") or (game[8] == "X" and game[5] == "X" and game[2] == "X") or (game[0] == "X" and game[1] == "X" and game[2] == "X") or (game[7] == "X" and game[4] == "X" and game[1] == "X") or (game[3] == "X" and game[4] == "X" and game[5] == "X") or (game[0] == "X" and game[4] == "X" and game[8] == "X"):
                        print("Congrate Player (X) won")
                        input()
                        input()
                        break
                    if (game[6] == "O" and game[7] == "O" and game[8] == "O") or (game[6] == "O" and game[3] == "O" and game[0] == "O") or (game[6] == "O" and game[4] == "O" and game[2] == "O") or (game[8] == "O" and game[5] == "O" and game[2] == "O") or (game[0] == "O" and game[1] == "O" and game[2] == "O") or (game[7] == "O" and game[4] == "O" and game[1] == "O") or (game[3] == "O" and game[4] == "O" and game[5] == "O") or (game[0] == "O" and game[4] == "O" and game[8] == "O"):
                        print("Congrate Player (O) won")
                        input()
                        input()
                        break
                else:
                    print("Can't play there !!!")
                    continue
        elif place >= 9:
            print("Out of range")
            input()
            break
        elif count > 10:
            print("Game Ends")
    except ValueError:
        print("")
    except IndexError:
        print("")
