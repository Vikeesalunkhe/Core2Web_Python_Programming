#break statement 

#serching system using for_loop and brak statement


playerlist = ["Rohit","Mahi","Virat","KLRahul","Shubman"]

PlayerName = input("Enter player name : ")

for i in playerlist:

    if (i == PlayerName):

        print(PlayerName, "is present is list")
        break

else :

    print(PlayerName, "is not present in list")


