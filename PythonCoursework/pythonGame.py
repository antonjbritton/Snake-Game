#Resolution: 1366x768
from tkinter import Tk, Canvas, PhotoImage, Label, Button
from random import randint

def fileReader(textFile): #This function is used to read the player names and scores from a text file
    playerScores = list()
    with open(textFile) as file:
        playerScores = file.readlines()
    playerScores = [line.rstrip("\n") for line in open(textFile)]
    file.close()
    return playerScores
#The file is opened and its contents are stored in the "playerScores" list. The empty lines are then
#discarded from "playerScores". Then the file is closed. This function returns the list "playerScores"

def mainMenu(): #This functions acts as the main menu of my game
    print("\nPlease choose one of the following options:")
    print("1.New Game")
    print("2.Load Game")
    print("3.Leaderboard")
    print("4.Customise Controls")
    print("5.Quit")
    choice = input("Enter a number between 1 and 5: ")
# depending on which number the user inputs (1-5) they will be redirected to another part of my program
    if choice == "1":
        global player
        player = input("\nPlease enter your player name: ")
        while player == "":
            player = input("\nInvalid entry. Please try again: ")
        chooseDifficulty()
    elif choice == "2":
        loadGame()
    elif choice == "3":
        chooseLeaderboard()
    elif choice == "4":
        customiseControls()
    elif choice == "5":
        exit()
    else:
        print("That is not a valid choice. Try again.")
        mainMenu()
#I have validated the user input and made use of recursion to ensure that if the user does not enter a
#valid input, this process will be repeated until they do

def chooseDifficulty(): #This function allows the user to set the difficulty of their game
    print("\nPlease choose one of the following difficulties:")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")
    difficultyChoice = input("Enter a number between 1 and 3: ")
    if difficultyChoice == "1" or difficultyChoice == "2" or difficultyChoice == "3":
        newGame(difficultyChoice)
#Calls the "newGame" function and passes the "difficultyChoice" variable so that the function knows which difficulty the user chose
    else:
        print("That is not a valid choice. Try again.")
        chooseDifficulty()
#I have validated the user input and made use of recursion to ensure that if the user does not enter a
#valid input, this process will be repeated until they do

def loadGame():
    global player
    player = input("\nEnter your username to load your save file: ")
    saveFileData = list()
    with open("saveFile.txt") as file:
        saveFileData = file.readlines()
    saveFileData = [line.rstrip("\n") for line in open("saveFile.txt")]
    file.close()
#stores the contents of the save file in a list
    for index in range(len(saveFileData)): #checks each item in the list
        if saveFileData[index] == player: #if the current item in the list is the name of the player that was entered (i.e. the player exists)
            found = True
            newGame(str(saveFileData[index+1]),int(saveFileData[index+2]),int(saveFileData[index+3]))
#set found to True and create a new game with the details of the player that were saved
    if "found" not in locals():
        print("\nThere does not appear to be a save file for that player")
#if the player can't be found in the list then an appropriate error message is outputted

def newGame(difficulty, savedLength=0, savedScore=0):
    global window, canvas, currentDifficulty, snake, snakeSize, snakeSpeed, score, scoreText, direction, paused, hidden, multiplier
    window = setWindowDimensions(width, height) #sets up the window
    canvas = Canvas(window, bg="black", width=width, height=height) #creates a canvas which we will use for the background and shapes
    paused = False
    hidden = False

    if difficulty == "1": #sets up game mode 1 (easy)
        snakeSize = 100
        snakeSpeed = 150
        background = PhotoImage(file="background1.png")#source: https://pixabay.com/illustrations/forest-trees-fog-silhouette-mist-5855196/
    elif difficulty == "2": #sets up game mode 2 (medium)
        snakeSize = 80
        snakeSpeed = 100
        background = PhotoImage(file="background2.png")#source: https://pixabay.com/vectors/mountains-panorama-forest-mountain-1412683/
    elif difficulty == "3": #sets up game mode 3 (hard)
        snakeSize = 40
        snakeSpeed = 50
        background = PhotoImage(file="background3.png")#source: https://pixabay.com/illustrations/trees-lake-forest-river-sky-beach-6207925/
    currentDifficulty = difficulty

    canvas.create_image(width/2,height/2, image=background) #creates the background
    snake = []
    snake.append(canvas.create_rectangle(snakeSize,snakeSize, snakeSize * 2, snakeSize * 2, fill="green")) #this represents the snake's head
    for i in range(savedLength - 1):
        snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="light green"))
#if the user has loaded a previous game then this code sets the snake to the correct length
    score = savedScore
    txt = "Score: " + str(score)
    scoreText = canvas.create_text( width/2 , 40 , fill="white" , font="Times 40 italic bold", text=txt)

    if "leftChoice" in globals():
        canvas.bind(leftChoice, leftKey)
        canvas.bind(rightChoice, rightKey)
        canvas.bind(upChoice, upKey)
        canvas.bind(downChoice, downKey)
#This block of code checks whether the user has defined custom controls. If they have, then the keys that they
#chose are binded to the corresponding direction function

    canvas.bind("<Left>", leftKey) #binds the left arrow key to the "leftKey" function
    canvas.bind("<Right>", rightKey) #binds the right arrow key to the "rightKey" function
    canvas.bind("<Up>", upKey) #binds the up arrow key to the "upKey" function
    canvas.bind("<Down>", downKey) #binds the down arrow key to the "downKey" function
    canvas.bind("123", shrinkCheat) #binds the key combination "123" to the skrinkCheat function
    canvas.bind("456", growCheat) #binds the key combination "456" to the growCheat function
    canvas.bind("789", doublePointsCheat) #binds the key combination "789" to the doublePointsCheat function
    canvas.bind("<space>", pause) #binds the space bar to the "pause" function
    canvas.bind("<Escape>", bossKey) #binds the escape key to the "bossKey" function
    canvas.focus_set()

    direction = "right"
    multiplier = 1

    placeBlueFood()
    placeRedFood()
    moveSnake()

    window.mainloop() #updates the window screen

def chooseLeaderboard():
    print("\nPlease choose a game mode to view the history of: ")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")
    leaderboardChoice = input("Enter a number between 1 and 3: ")
#Allows the user to choose which game mode they would like to view the leaderboard of
    if leaderboardChoice == "1":
        viewLeaderboard(fileReader("easyScores.txt"))
    elif leaderboardChoice == "2":
        viewLeaderboard(fileReader("mediumScores.txt"))
    elif leaderboardChoice == "3":
        viewLeaderboard(fileReader("hardScores.txt"))
#The selection statement is used to determine which text file will be read from
    else:
        print("That is not a valid choice. Try again.")
        chooseLeaderboard()
#I have made use of recursion so that if the user does not enter a valid choice they will be given the chance to do so again

def viewLeaderboard(playerScores): #This function allows the user to view the leaderboard
    if len(playerScores) > 0:
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
    else:
        print("\nNo player data to display.")
#I have added validation for this option because if the "playerScores" list is empty then the user
#will not be able to view the leaderboard

def updateLeaderboard(): #This function is used to update the leaderboard after the user has played a game
    leaderboardFileData = list()
    if currentDifficulty == "1":
        leaderboardFile = "easyScores.txt"
    elif currentDifficulty == "2":
        leaderboardFile = "mediumScores.txt"
    elif currentDifficulty == "3":
        leaderboardFile = "hardScores.txt"
    with open(leaderboardFile) as file:
        leaderboardFileData = file.readlines()
    leaderboardFileData = [line.rstrip("\n") for line in open(leaderboardFile)]
    file.close()
#opens the specified text file and stores its contents in a list
    for index in range(len(leaderboardFileData)): #checks each item in the list
        if leaderboardFileData[index] == player: #if the player already exists
            if int(leaderboardFileData[index + 1]) < score: #and their new score is greater than their previous score
                leaderboardFileData[index + 1] = score #their score will be updated
            found = True
    if "found" not in locals(): #if the player does not already exist their details will be added to the end of the list
        leaderboardFileData.append(player)
        leaderboardFileData.append(score)
    with open (leaderboardFile, "w") as file: #writes the contents of the list to the relevant text file
        for item in leaderboardFileData:
            file.write("%s\n" % item)

def customiseControls():
    global leftChoice, rightChoice, upChoice, downChoice
    currentChoices = []
    possibleChoices = "abcdefghijklmnopqrstuvwxyz" #these are the characters that the user can choose from
    print("\nThe default controls for this game are the arrow keys")
    print("Please choose a secondary key (letter) for each direction")
    leftChoice = input("Enter the key you will use to turn left: ")
    while (leftChoice in currentChoices) or (len(leftChoice) > 1) or (leftChoice not in possibleChoices):
        leftChoice = input("That is not a valid entry. Please try again: ")
    currentChoices.append(leftChoice)
    rightChoice = input("Enter the key you will use to turn right: ")
    while (rightChoice in currentChoices) or (len(rightChoice) > 1) or (rightChoice not in possibleChoices):
        rightChoice = input("That is not a valid entry. Please try again: ")
    currentChoices.append(rightChoice)
    upChoice = input("Enter the key you will use to go up: ")
    while (upChoice in currentChoices) or (len(upChoice) > 1) or (upChoice not in possibleChoices):
        upChoice = input("That is not a valid entry. Please try again: ")
    currentChoices.append(upChoice)
    downChoice = input("Enter the key you will use to go down: ")
    while (downChoice in currentChoices) or (len(downChoice) > 1) or (downChoice not in possibleChoices):
        downChoice = input("That is not a valid entry. Please try again: ")
#the user will be asked to enter a key for each direction. If they enter a key more than once, or they enter more than
#one key, or they enter a key that is not a letter, then they will be told that this is not a valid entry and they will
#have to enter something else

def placeBlueFood(): #This function places blue "food" on the canvas
    global blueFood, blueFoodX, blueFoodY #allows us to make changes to global variables "blueFood", "blueFoodX" and "blueFoodY"
    blueFood = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="blue")
    blueFoodX = randint(0, width - snakeSize) #generates a random x coordinate where the food will be placed
    blueFoodY = randint(0, height - snakeSize) #generates a random y coordinate where the food will be placed
    canvas.move(blueFood, blueFoodX, blueFoodY) #places the food on the canvas in the coordinates that were generated

def placeRedFood(): #This function places red "food" on the canvas
    global redFood, redFoodX, redFoodY #allows us to make changes to global variables "redFood", "redFoodX" and "redFoodY"
    redFood = canvas.create_oval(0,0, snakeSize, snakeSize, fill="red")
    redFoodX = randint(0, width - snakeSize) #generates a random x coordinate where the food will be placed
    redFoodY = randint(0, height - snakeSize) #generates a random y coordinate where the food will be placed
    canvas.move(redFood, redFoodX, redFoodY) #places the food on the canvas in the coordinates that were generated

def leftKey(event): #This function is called when the user presses the key associated with moving left
    global direction #allows us to make changes to global variable "direction"
    if direction != "right": #ensures that the direction is not equal to "right" so that changing the direction will not cause the snake to collide with itself
        direction = "left" #sets the direction of the snake to "left"

def rightKey(event): #This function is called when the user presses the key associated with moving right
    global direction #allows us to make changes to global variable "direction"
    if direction != "left": #ensures that the direction is not equal to "left" so that changing the direction will not cause the snake to collide with itself
        direction = "right" #sets the direction of the snake to "right"

def upKey(event): #This function is called when the user presses the key associated with moving up
    global direction #allows us to make changes to global variable "direction"
    if direction != "down": #ensures that the direction is not equal to "down" so that changing the direction will not cause the snake to collide with itself
        direction = "up" #sets the direction of the snake to "up"

def downKey(event): #This function is called when the user presses the key associated with moving down
    global direction #allows us to make changes to global variable "direction"
    if direction != "up": #ensures that the direction is not equal to "up" so that changing the direction will not cause the snake to collide with itself
        direction = "down" #sets the direction of the snake to "down"

def shrinkCheat(event): #This function is used to shrink the snake on command
    global snake #allows us to make changes to global variable "snake"
    if len(snake) > 1:
        canvas.delete(snake[len(snake) - 1])
        snake.pop()
        print("\nShrink cheat activated!")
#Shrinks the snake and outputs a relevant message to the command line
    else:
        print("\nThe snake is too small to shrink!")
#The purpose of the selection statement is to ensure that the snake's head is not deleted

def growCheat(event): #This function is used to grow the snake on command
    global snake #allows us to make changes to global variable "snake"
    snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="light green"))
    print("\nGrow cheat activated!")
#Grows the snake and outputs a relevant message to the command line

def doublePointsCheat(event): #This function is used to toggle double points on command
    global multiplier #allows us to make changes to global variable "multiplier"
    if multiplier == 1:
        multiplier = 2
        print("\nDouble points activated!")
#If double points is turned off then it will be turned on and the user will be informed of this via a message outputted to the terminal
    else:
        multiplier = 1
        print("\nDouble points deactivated!")
#If double points is turned on then it will be turned off and the user will be informed of this via a message outputted to the terminal

def pause(event):
    global paused, pauseText #allows us to make changes to global variables "paused" and "pauseText"
    if paused == False:
        paused = True
        pauseText = canvas.create_text(width/2,height/2,fill="white",font="Times 40 italic bold", text="Press space bar to resume the game\nPress enter to save the game\nPress backspace to quit the game")
        canvas.bind("<Return>",save)
        canvas.bind("<BackSpace>",quit)
#This block of code is used to "pause" the game
    else:
        paused = False
        canvas.delete(pauseText)
        canvas.unbind("<Return>")
        canvas.unbind("<BackSpace>")
        moveSnake()
#This block of code is used to "unpause" the game

def save(event):
    saveFileData = list()
    with open("saveFile.txt") as file:
        saveFileData = file.readlines()
    saveFileData = [line.rstrip("\n") for line in open("saveFile.txt")]
    file.close()
#This block of code stores the values in the save file to a list
    for index in range(len(saveFileData)):
        if saveFileData[index] == player:
            saveFileData[index + 1] = currentDifficulty
            saveFileData[index + 2] = len(snake)
            saveFileData[index + 3] = score
            found = True
#This block of code goes through each item in the list and checks them to determine whether the player has
#already saved a game. If the player has saved a game before, then this game is overwritten by the new one
    if "found" not in locals():
        saveFileData.append(player)
        saveFileData.append(currentDifficulty)
        saveFileData.append(len(snake))
        saveFileData.append(score)
#If the player has not saved a game before, then their game details are appended to the list
    with open ("saveFile.txt", "w") as file:
        for item in saveFileData:
            file.write("%s\n" % item)
#The saveFileData list is written to the save file

def quit(event):
    window.destroy()
#This function allows the user to quit the game

def bossKey(event):
    global paused, pauseText, hidden, hideScreen, hideScreenText #allows us to make changes to global variables "paused", "pauseText", "hidden", "hideScreen" and "hideScreenText"
    if hidden == False: #if the boss key screen is not showing
        if paused == False:
            paused = True
            pauseText = canvas.create_text(width/2,height/2,fill="white",font="Times 40 italic bold", text="Press space bar to resume the game\nPress enter to save the game\nPress backspace to quit the game")
            canvas.bind("<Return>",save)
            canvas.bind("<BackSpace>",quit)
#This block of code pauses the game so that it is not running while the boss key screen is obscuring the user's view
        hideScreen = canvas.create_rectangle(0,0,width,height,fill="white") #creates a white screen that covers the game screen
        hideScreenText = canvas.create_text(width/2,height/2,fill="black",font="Times 40 italic bold",text="Loading...") #creates text to give the impression that the user is waiting for a page to load
        window.title("") #changes the title of the window to ""
        hidden = True
        paused = True
    else: #if the boss key screen is showing
        canvas.delete(hideScreen) #the screen block will be deleted
        canvas.delete(hideScreenText) #the loading text will be deleted
        window.title("Snake Game") #the title of the window will be changed to "Snake Game"
        hidden = False



def setWindowDimensions(w,h): #This function sets the dimensions of the window
    window = Tk()
    window.title("Snake Game")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2) #x position on screen
    y = (hs/2) - (h/2) #y position on screen
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
#uses the geometry method to set the dimensions and position of the window
    return window

def growSnake(): #This function is used to grow the snake
    lastElement = len(snake) - 1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="light green")) #adds a new square to the snake
    if direction == "left":
        canvas.coords(snake[lastElement+1], lastElementPos[0]+snakeSize, lastElementPos[1], lastElementPos[2]+snakeSize, lastElementPos[3])
    elif (direction == "right"):
        canvas.coords(snake[lastElement+1], lastElementPos[0]-snakeSize, lastElementPos[1], lastElementPos[2]-snakeSize, lastElementPos[3])
    elif (direction == "up"):
        canvas.coords(snake[lastElement+1], lastElementPos[0], lastElementPos[1]+snakeSize, lastElementPos[2], lastElementPos[3]+snakeSize)
    else:
        canvas.coords(snake[lastElement+1], lastElementPos[0], lastElementPos[1]-snakeSize, lastElementPos[2], lastElementPos[3]-snakeSize)
#These selection statements move the snake on the canvas when different directions have been selected
    global score, points #allows us to make changes to global variables "score" and "points"
    score += (points * multiplier)
    txt = "Score: " + str(score)
    canvas.itemconfigure(scoreText, text=txt) #updates the text on the canvas

def moveBlueFood(): #This function moves blue "food" after the snake "eats" one
    global blueFood, blueFoodX, blueFoodY, points
    if canvas.itemcget(blueFood, "fill") == "blue":
        points = 10
    else:
        points = 30
    canvas.delete(blueFood) #clears the blue "food" that is currently on the canvas
    foodOption = randint(1, 10)
    if foodOption == 1:
        blueFood = canvas.create_arc(0,0, snakeSize*2, snakeSize*2, fill="yellow")
    else:
        blueFood = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="blue")
    blueFoodX = randint(0, width - snakeSize*2)
    blueFoodY = randint(0, height - snakeSize*2)
    canvas.move(blueFood, blueFoodX, blueFoodY)
#Works in a similar way to the "placeBlueFood" function

def moveRedFood(): #This function moves red "food" after the snake "eats" one
    global redFood, redFoodX, redFoodY, points
    if canvas.itemcget(redFood, "fill") == "red":
        points = 20
    else:
        points = 30
    canvas.delete(redFood) #clears the red "food" that is currently on the canvas
    foodOption = randint(1, 5)
    if foodOption == 1:
        redFood = canvas.create_arc(0,0, snakeSize*2, snakeSize*2, fill="yellow")
        newPoints = 30
    else:
        redFood = canvas.create_oval(0,0, snakeSize, snakeSize, fill="red")
        newPoints = 20
    redFoodX = randint(0, width - snakeSize*2)
    redFoodY = randint(0, height - snakeSize*2)
    canvas.move(redFood, redFoodX, redFoodY)
#Works in a similar way to the "placeRedFood" function

def overlapping(a,b): #This function is used to check if the snake is overlapping with something
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False
#If the snake is overlapping with something the function returns true. If not, the function returns False

def moveSnake(): #This function is used to move the snake
    canvas.pack()
    positions = []
    positions.append(canvas.coords(snake[0]))
    if positions[0][0] < 0:
        canvas.coords(snake[0],width,positions[0][1],width-snakeSize,positions[0][3])
    elif positions[0][2] > width:
        canvas.coords(snake[0],0-snakeSize,positions[0][1],0,positions[0][3])
    elif positions[0][3] > height:
        canvas.coords(snake[0],positions[0][0],0-snakeSize,positions[0][2],0)
    elif positions[0][1] < 0:
        canvas.coords(snake[0],positions[0][0],height,positions[0][2],height-snakeSize)
#These selection statements are used to ensure that if the snake disappears off one side of the screen
#it will reapper on the other side of the screen
    positions.clear()
    positions.append(canvas.coords(snake[0]))
    if direction == "left":
        canvas.move(snake[0], - snakeSize, 0) #moves the snake left
    elif direction == "right":
        canvas.move(snake[0], snakeSize, 0) #moves the snake right
    elif direction == "up":
        canvas.move(snake[0], 0, -snakeSize) #moves the snake up
    elif direction == "down":
        canvas.move(snake[0], 0, snakeSize) #moves the snake down
    snakeHeadPos = canvas.coords(snake[0])
    blueFoodPos = canvas.coords(blueFood)
    redFoodPos = canvas.coords(redFood)
    if overlapping(snakeHeadPos, blueFoodPos): #checks if the snake has collided with a blue food object
        moveBlueFood()
        growSnake()
    if overlapping(snakeHeadPos, redFoodPos): #checks if the snake has collided with a red food object
        moveRedFood()
        growSnake()
    for i in range(1,len(snake)):
        if overlapping(snakeHeadPos, canvas. coords(snake[i])): #checks if the snake has collided with itself
            gameOver = True
            updateLeaderboard()
            canvas.create_text(width/2,height/2,fill="white",font="Times 40 italic bold", text="Game Over! Press backspace to quit.")
            canvas.bind("<BackSpace>",quit)
            canvas.unbind("<space>")
#gameOver is set to true and a message is outputted to the screen telling the user "Game Over!"
#the leaderboard is updated and the relevant keys are binded/unbinded
    for i in range(1,len(snake)):
        positions.append(canvas.coords(snake[i]))
    for i in range(len(snake) - 1):
        canvas.coords(snake[i+1],positions[i][0],positions[i][1],positions[i][2],positions[i][3])
    if 'gameOver' not in locals() and paused == False:
        window.after(snakeSpeed, moveSnake)
#Calls the moveSnake function within the main loop

width = 1366
height = 768

while True:
    mainMenu()
#This block of code will ensure that the program loops until the user decides to exit
