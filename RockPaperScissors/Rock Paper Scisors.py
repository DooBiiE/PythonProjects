from random import randint
#from tkinter import *
import tkinter as tk
import time
from PIL import ImageTk,Image

# Variables
def endGame():
    print("Quiting game. goodbye!")
    time.sleep(3)
    exit()

#def startGame():
    #print("Lets begin" + userName + ', good luck!')

#userName.variable = tk.StringVar()
#userName.set("")
#userNameIP.get()

# setting up tkinter
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("275x250")
window.configure(background="black")
window.iconbitmap("RPS.ico")

# image file
path = "RockPaperScissors100x90.png"

# tkinter widgets
# separated into 2 sections top/middle/bottom
top_frame = tk.Frame(window, bg="black", width =300, height = 50)
middle_frame = tk.Frame(window, bg="white", width = 500 )
bottom_frame = tk.Frame(window, bg="black", width =300, height = 100)

# top frame items
labelGameName = tk.Label(top_frame, text="Lets play - Rock Paper Scissors", pady = "1", bg="black", fg="white")

# middle frame items
gameImage = ImageTk.PhotoImage(Image.open(path))
imagePanel = tk.Label(middle_frame, image = gameImage)
userNameLabel = tk.Label(middle_frame, text= "Please enter your name : ", bg="white", fg="black")
userNameIP = tk.Entry(middle_frame, justify = "center",) #textvariable=userName)

# bottom frame items
buttonStart = tk.Button(bottom_frame, text="Start Game", pady = "5", padx = "5")
buttonQuit = tk.Button(bottom_frame, text="Exit", command= endGame,)


# Packing widgets into tk window
labelGameName.pack(side = "top", pady = "5")
imagePanel.pack(fill = "both", expand = "yes", pady = "5" )

buttonQuit.pack(side = "left")
buttonStart.pack(side = "bottom")
userNameLabel.pack()
userNameIP.pack(side = "bottom", pady = "10",)

top_frame.pack(side = "top")
middle_frame.pack()
bottom_frame.pack(side = "bottom")


# Start the window GUI
window.mainloop()

while True:

    print("Lets play Rock, Paper, Scissors ... \n")
    time.sleep(1)
    # Get input from player to make a selection
    print("Please select from the below ... \n")
    time.sleep(1)
    player = input("Rock (r), Paper (p), or Scissors (s)? \n")
    time.sleep(.3)
    print("\n")
    print("Computing your selection ... \n")
    time.sleep(1)
    #print the output of the selection
    time.sleep(0.3)
    print("Player choses: ", player, "vs", end=" ")


    #chosen is a variable and a random int is assigned against (random number between 1 & 3)
    chosen = randint(1,3)

    #defining of what each number relates to in ref to r/p/s
    if chosen == 1:
        computer = "r"

    elif chosen == 2:
        computer = "p"

    else:
        computer = "s"

    #Printing the computer output against the player input
    print("Computer choses: " + computer)
    print("\n")

    #Cheking the 2 inputs and defining who wins
    if player == computer:
        print("Draw! \n")

    #Player chosing rock
    elif player == "r" and computer == "s":
        print("Player wins! \n")

    elif player == "r" and computer == "p":
        print("Computer wins! \n")

    #player chosing paper
    elif player == "p" and computer == "r":
        print("Player wins! \n")

    elif player == "p" and computer == "s":
        print("Computer wins! \n")

    #player chosing scissors
    elif player == "s" and computer == "p":
        print("Player wins! \n")

    elif player == "s" and computer == "r":
        print("Computer wins! \n ")

    answer = input("Would you like to play again? (y/n) \n")
    time.sleep(2)
    print("\n")

    if answer not in ("y", "n"):
        print("Invalid Input")
        break

    if answer == "y":
        continue

    else:
        input("\n Press the enter key to exit")
        break