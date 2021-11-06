from tkinter import Tk, Canvas

def fileReader(): #This function is used to read the player names and scores from a text file
    playerScores = list()
    with open("scores.txt") as file:
        playerScores = file.readlines()
    playerScores = [line.rstrip("\n") for line in open("scores.txt")]
    file.close()
    return playerScores
#The file is opened and its contents are stored in the "playerScores" list. The empty lines are then
#discarded from "playerScores". Then the file is closed. This function returns the list "playerScores"

def mainMenu(): #This functions acts as the main menu of my game
    print("\nPlease choose one of the following options:")
    print("1.New Game")
    print("2.Load Game")
    print("3.Leaderboard")
    print("4.Quit")
    choice = input("Enter a number between 1 and 4: ")
# depending on which number the user inputs (1-4) they will be redirected to another part of my program
    if choice == "1":
        print("Option 1")
    elif choice == "2":
        print("Option 2")
    elif choice == "3":
        if len(playerScores) > 0:
            viewLeaderboard()
        else:
            print("\nNo player data to display.")
#I have added validation for this option because if the "playerScores" list is empty then the user
#will not be able to view the leaderboard
    elif choice == "4":
        exit()
    else:
        print("That is not a valid choice. Try again.")
        mainMenu()
#I have validated the user input and made use of recursion to ensure that if the user does not enter a
#valid input, this process will be repeated until they do

def viewLeaderboard(): #This function allows the user to view the leaderboard
    for i in range(0, len(playerScores), 2):
        for j in range(0, len(playerScores) - 2, 2):
            if playerScores[j + 1] < playerScores[j + 3]:
                swapUsername = playerScores[j]
                playerScores[j] = playerScores[j + 2]
                playerScores[j + 2] = swapUsername
                swapScore = playerScores[j + 1]
                playerScores[j + 1] = playerScores[j + 3]
                playerScores[j + 3] = swapScore
#I have utilised a bubble sort in order to sort the player data so that it can be represented in a leaderboard
    print("\nLeaderboard:")
    count = 1
    for i in range(0, len(playerScores), 2):
        print(str(count) + "." + playerScores[i] + " - " + playerScores[i + 1] + "points")
        count += 1
#I have used a for loop to display the data of each user in a leaderboard structure

while True:
    playerScores = fileReader()
    mainMenu()
#This block of code will ensure that the program loops until the user decides to exit
