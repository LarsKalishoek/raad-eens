import random

print("Welkom bij raad het getal.")
winamout = 0
gamenum = 0
roundnum = 1
continueG = "y" 

while gamenum <= 20 and continueG == "y":
    gamenum = gamenum + 1
    print("Dit is game nummer " + str(gamenum))

    geheim = random.randint(1, 1000)
    answer = 0


    while int(answer) != geheim and roundnum <= 10:
        print("Round " + str(roundnum))
        roundnum += 1
        answer = int(input("Raad het getal : "))
        difference = geheim - answer
        if answer == geheim:
            print("U heeft het geraden.")
            winamout += 1
        elif difference <= 20 and difference >= -20:
            print("U zit heel warm.")
            if answer < geheim:
                print("Nog een klein beetje hoger.")
            else:
                print("Nog een klein beetje lager.")
        elif difference <= 50 and difference >= -50:
            print("U zit warm")
            if answer < geheim:
                print("Nog wat hoger")
            else:
                print("Nog wat lager")
        elif answer < geheim:
            print("Hoger")
        elif answer > geheim:
            print("Lager")
    continueG = input("Wilt u nog een ronde spelen?  Y/N : ").lower()
print("-------------------------------------------------------------------")
print("U heeft " + str(winamout) + "x gewonnen")