from tkinter import *
import tkinter as tk
from tkinter import ttk
from random import randint

#### Algorithm for setting the window (of the program) in the center, slightly in the north position of the screen/desktop ####
def centerWindow(width, height):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    x = (screenWidth/2) - (width/2)
    y = (screenHeight/2.5) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


#### Upping the scoreboard ####
def scoreChange():
    global scoreCounter
    global scoreLabel
    scoreCounter += 1
    scoreLabel.config(text=("Score", scoreCounter))


#### Setting the score, after win-combo break, to 0 ####
def scoreChangeLose():
    global scoreCounter
    global scoreLabel
    scoreCounter = 0
    scoreLabel.config(text=("Score", scoreCounter))


#### Logic for highscore ####
def highScoreChange():
    global highScore
    global highLabel
    if highScore < scoreCounter:
        highScore = scoreCounter
    highLabel.config(text=("High-Score", highScore))


#### Logic for randomization when user chooses rock ####
def spinRock():
    number = randint(0, 2)
    imageLabel.config(image=imageList[number])
    imageLabel2.config(image=imageList[0])

    if number == 0:
        winLose.config(text="Draw!")
        '''highScoreChange()
        scoreChangeLose()'''
    elif number == 1:
        winLose.config(text="You Lost!")
        highScoreChange()
        scoreChangeLose()
    elif number == 2:
        winLose.config(text="You Won!")
        scoreChange()

        
#### Logic for randomization when user chooses paper ####
def spinPaper():
    number = randint(0, 2)
    imageLabel.config(image=imageList[number])
    imageLabel2.config(image=imageList[1])

    if number == 0:
        winLose.config(text="You Won!")
        scoreChange()
    elif number == 1:
        winLose.config(text="Draw!")
    elif number == 2:
        winLose.config(text="You Lost!")
        highScoreChange()
        scoreChangeLose()


#### Logic for randomization when user chooses scissors ####
def spinscissors():
    number = randint(0, 2)
    imageLabel.config(image=imageList[number])
    imageLabel2.config(image=imageList[2])

    if number == 0:
        winLose.config(text="You Lost!")
        highScoreChange()
        scoreChangeLose()
    elif number == 1:
        winLose.config(text="You Won!")
        scoreChange()
    elif number == 2:
        winLose.config(text="Draw!")


#### Main window ####
root = tk.Tk()
root.title('Emin Hodzic <> Rock Paper Scissors')
root.iconbitmap('C:/Python Project/RockPS/Assets//e.ico')


#### Puts the window in the center, slightly in the north position of the screen ####
centerWindow(1000, 500)
#### Locks resizing of the window ####
root.resizable(False, False)
#root.config(bg="black")

frame = ttk.Frame(root)
frame.pack()


#### Slike ####
rock = PhotoImage(file='Assets/rock.png')
paper = PhotoImage(file='Assets/paper.png')
scissors = PhotoImage(file='Assets/scissors.png')


#### Add images to list ####
imageList = [rock, paper, scissors]


#### Random number 0-2 ####
number = randint(0, 2)


#### Score ####
scoreCounter = 0
highScore = 0

scoreLabel = Label(frame, text=("Score", scoreCounter), font=("Helvetica", 15))
scoreLabel.grid(row=0, column=3, pady=10, sticky="ew")

highLabel = Label(frame, text=("High-Score", scoreCounter), font=("Helvetica", 15))
highLabel.grid(row=0, column=5, pady=10, sticky="ew")

cpuLabel = Label(frame, text=("CPU"), font=("Helvetica", 10))
cpuLabel.grid(row=0, column=1, pady=(20, 0), sticky="ew")

userLabel = Label(frame, text=("YOU"), font=("Helvetica", 10))
userLabel.grid(row=0, column=6, pady=(20, 0), sticky="ew")


#### Throw an image when the program starts ####
imageLabel = Label(frame, image=imageList[number], width=290, height=300, bd=0)
imageLabel.grid(row=1, column=0, columnspan=3, pady=30, sticky="ew")

imageLabel2 = Label(frame, image=imageList[number], width=290, height=300, bd=0)
imageLabel2.grid(row=1, column=6, pady=30, sticky="ew")

#### Buttons for user input ####
rockButton = ttk.Button(frame, text="ROCK", command=spinRock)
rockButton.grid(row=2, column=3, padx=5, sticky="ew")

paperButton = ttk.Button(frame, text="PAPER", command=spinPaper)
paperButton.grid(row=2, column=4, padx=5, sticky="ew")

scissorsButton = ttk.Button(frame, text="SCISSORS", command=spinscissors)
scissorsButton.grid(row=2, column=5, padx=5, sticky="ew")


#### Win_Lose Result ####
winLose = Label(frame, text="", font=("Helvetica", 15))
winLose.grid(row=3, column=3,columnspan=3, padx=5, pady=20, sticky="ew")



root.mainloop()

#Meme
'''def spinscissors():
    number = randint(0, 2)
    imageLabel.config(image=imageList[number])

    if number == 0:
        winLose.config(text="You Lost to a Computer, schelcht Ojda cc; Play again!")
        scoreChangeLose()
    elif number == 1:
        winLose.config(text="You Won, Good Job Human, Better Score? Play again!")
        scoreChange()
    elif number == 2:
        winLose.config(text="Draw... really Human?! You can do better; Play Again!")
        scoreChangeLose()'''