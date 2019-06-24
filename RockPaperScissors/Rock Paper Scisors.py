from random import randint
import tkinter as tk
import time as time
from tkinter import StringVar
from PIL import ImageTk,Image

# Variables
def endGame():
    print("Quiting game. goodbye!")
    time.sleep(3)
    exit()

def startGame():
    print("Lets begin" + userNameIP.get() + ', good luck!')

def userName():
    userNameIP.entry = StringVar()
    userNameIP.set("")
    userNameIP.get()

def enterUserName():
    enterUserNameButton.pack_forget()
    inputUserNameLabel= tk.Label(middle_frame, text="Welcome " + userNameIP.get() + ", press Start Game to play.", bg="white")
    inputUserNameLabel.pack()
    #userNameLabel.pack()
    userNameLabel.pack_forget()
    userNameIP.pack_forget()


def resetUserName():
    #inputUserNameLabel.pack_forget()
    inputUserNameLabel.destroy()
    userNameLabel.pack()
    enterUserNameButton.pack()
    userNameIP.pack (side = "bottom", pady = "10",)
    inputUserNameLabel.pack_forget()

# setting up tkinter
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x300")
window.configure(background="black")
window.iconbitmap("RPS.ico")

# image file
path = "RockPaperScissors100x90.png"

# tkinter widgets
# separated into 2 sections top/middle/bottom
top_frame = tk.Frame(window, bg="black", width =250, height = 50)
middle_frame = tk.Frame(window, bg="white", width = 250, height = 250)
middleBottom_frame = tk.Frame(window, bg="white", width = 350, height = 5)
bottom_frame = tk.Frame(window, bg="black", width =250, height = 100)

# top frame items
labelGameName = tk.Label(top_frame, text="Lets play - Rock Paper Scissors", pady = "1", bg="black", fg="white")

# middle frame items
gameImage = ImageTk.PhotoImage(Image.open(path))
imagePanel = tk.Label(middle_frame, image = gameImage)
userNameLabel = tk.Label(middle_frame, text= "userNameLabel", bg="white", fg="black") #Please enter your name :
userNameIP = tk.Entry(middle_frame, justify = "center", text=" ")
enterUserNameButton = tk.Button(middle_frame, text = "Enter username", command=enterUserName)
inputUserNameLabel = tk.Label(middle_frame, bg="white", text= "inputUserNameLabel")


# bottom frame items
buttonStart = tk.Button(bottom_frame, text="Start Game", pady = "5", padx = "5")
buttonQuit = tk.Button(bottom_frame, text="Exit", command= endGame,)
buttonReset =tk.Button(bottom_frame, text = "Reset username", command= resetUserName,)

# Packing widgets into tk window
# Top frame pack
labelGameName.pack(side = "top", pady = "5")
imagePanel.pack(fill = "none", expand = "yes", pady = "5" )

# Middle frame pack
enterUserNameButton.pack(side = "bottom", pady = "3")
userNameIP.pack(side = "bottom", pady = "10",)
userNameLabel.pack()
inputUserNameLabel.pack()

# Bottom frame pack
buttonQuit.pack(side = "left")
buttonReset.pack(side = "right")
buttonStart.pack(side = "bottom", ipadx = "30", padx = "5", anchor = "center")

# Frame packing
top_frame.pack(side = "top")
middle_frame.pack()
bottom_frame.pack(side = "bottom", pady = "5")
middleBottom_frame.pack(side = "bottom")

# Start the window GUI
window.mainloop()







##### game code ##### -----------------------------------
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