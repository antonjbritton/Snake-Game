from tkinter import Tk, Canvas

def mainMenu():
    print("Please choose one of the following options:")
    print("1.New Game")
    print("2.Load Game")
    print("3.Leaderboard")
    print("4.Quit")
    choice = input("Enter a number between 1 and 4: ")
    if choice == "1":
        print("Option 1")
    elif choice == "2":
        print("Option 2")
    elif choice == "3":
        print("Option 3")
    elif choice == "4":
        exit()
    else:
        print("That is not a valid choice. Try again.")
        mainMenu()

mainMenu()
