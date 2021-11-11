#Resolution: 1366x768
from tkinter import Tk, Canvas
import random

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
        newGame()
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

def newGame():
    global window, canvas, snake, snakeSize, score, scoreText, direction
    window = setWindowDimensions(width, height)
    canvas = Canvas(window, bg="black", width=width, height=height)

    snake = []
    snakeSize = 30
    snake.append(canvas.create_rectangle(snakeSize,snakeSize, snakeSize * 2, snakeSize * 2, fill="white"))
    score = 0
    txt = "Score: " + str(score)
    scoreText = canvas.create_text( width/2 , 15 , fill="white" , font="Times 20 italic bold", text=txt)

    canvas.bind("<Left>", leftKey) #binds the left arrow key to the "leftKey" function
    canvas.bind("<Right>", rightKey) #binds the right arrow key to the "rightKey" function
    canvas.bind("<Up>", upKey) #binds the up arrow key to the "upKey" function
    canvas.bind("<Down>", downKey) #binds the down arrow key to the "downKey" function
    canvas.focus_set()

    direction = "right"

    placeFood()
    moveSnake()

    window.mainloop() #updates the window screen

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

def placeFood(): #This function places "food" on the canvas
    global food, foodX, foodY #allows us to make changes to global variables "food", "foodX" and "foodY"
    food = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="steel blue" )
    foodX = random.randint(0, width - snakeSize) #generates a random x coordinate where the food will be placed
    foodY = random.randint(0, height - snakeSize) #generates a random y coordinate where the food will be placed
    canvas.move(food, foodX, foodY) #places the food on the canvas in the coordinates that were generated

def leftKey(event): #This function is called when the user presses the key associated with moving left
    global direction #allows us to make changes to global variable "direction"
    direction = "left" #sets the direction of the snake to "left"

def rightKey(event): #This function is called when the user presses the key associated with moving right
    global direction #allows us to make changes to global variable "direction"
    direction = "right" #sets the direction of the snake to "right"

def upKey(event): #This function is called when the user presses the key associated with moving up
    global direction #allows us to make changes to global variable "direction"
    direction = "up" #sets the direction of the snake to "up"

def downKey(event): #This function is called when the user presses the key associated with moving down
    global direction #allows us to make changes to global variable "direction"
    direction = "down" #sets the direction of the snake to "down"

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
    snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#FDF3F3")) #adds a new square to the snake
    if direction == "left":
        canvas.coords(snake[lastElement+1], lastElementPos[0]+snakeSize, lastElementPos[1], lastElementPos[2]+snakeSize, lastElementPos[3])
    elif (direction == "right"):
        canvas.coords(snake[lastElement+1], lastElementPos[0]-snakeSize, lastElementPos[1], lastElementPos[2]-snakeSize, lastElementPos[3])
    elif (direction == "up"):
        canvas.coords(snake[lastElement+1], lastElementPos[0], lastElementPos[1]+snakeSize, lastElementPos[2], lastElementPos[3]+snakeSize)
    else:
        canvas.coords(snake[lastElement+1], lastElementPos[0], lastElementPos[1]-snakeSize, lastElementPos[2], lastElementPos[3]-snakeSize)
#These selection statements move the snake on the canvas when different directions have been selected
    global score #allows us to make changes to global variable "score"
    score += 10
    txt = "Score: " + str(score)
    canvas.itemconfigure(scoreText, text=txt) #updates the text on the canvas

def moveFood(): #This function moves "food" after the snake "eats" one
    global food, foodX, foodY
    canvas.move(food, (foodX*(-1)), (foodY*(-1))) #clears the "food" that is currently on the canvas
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)
#Works in a similar way to the "placeFood" function

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
    foodPos = canvas.coords(food)
    if overlapping(snakeHeadPos, foodPos): #checks if the snake has collided with a food object
        moveFood()
        growSnake()
    for i in range(1,len(snake)):
        if overlapping(snakeHeadPos, canvas. coords(snake[i])): #checks if the snake has collided with itself
            gameOver = True
            canvas.create_text(width/2,height/2,fill="white",font="TImes 20 italic bold", text="Game Over!")
#gameOver is set to true and a message is outputted to the screen telling the user "Game Over!"
    for i in range(1,len(snake)):
        positions.append(canvas.coords(snake[i]))
    for i in range(len(snake) - 1):
        canvas.coords(snake[i+1],positions[i][0],positions[i][1],positions[i][2],positions[i][3])
    if 'gameOver' not in locals():
        window.after(90, moveSnake)
#Calls the moveSnake function every 90 milliseconds within the main loop

width = 1366
height = 768

while True:
    playerScores = fileReader()
    mainMenu()
#This block of code will ensure that the program loops until the user decides to exit
