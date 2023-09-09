from tkinter import *
import random
 
root = Tk()
 
root.geometry("300x300")
 
root.title("OPEN OX'S R P S Game")

computer_value = {  #computer values
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}
 
def reset_game():  #reset game
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player              ")
    l3.config(text="Computer")
    l4.config(text="")
 
def button_disable():  #button disable
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
 
def isrock(): # If player selected rock
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "खेल बराबरी "
    elif c_v == "Scissor":
        match_result = "खेलाडीले जित्यो "
    else:
        match_result = "कम्प्युटरले जित्यो "
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=c_v)
    button_disable()

def ispaper(): # If player selected paper
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "खेल बराबरी"
    elif c_v == "Scissor":
        match_result = "कम्प्युटरले जित्यो"
    else:
        match_result = "खेलाडीले जित्यो"
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=c_v)
    button_disable()
 
def isscissor():   # If player selected scissor
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "कम्प्युटरले जित्यो"
    elif c_v == "Scissor":
        match_result = "खेल बराबरी"
    else:
        match_result = "खेलाडीले जित्यो"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=c_v)
    button_disable()
 
# Add Labels, Frames and Button
Label(root,
      text="-कैची कागज ढुंगा-",
      font="normal 30 bold",
      fg="blue").pack(pady=20)
 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text="खेलाडी        ",
           font= "normal 14 bold")
 
l2 = Label(frame,
           text="VS       ",
           font="normal 20 bold")
 
l3 = Label(frame, text="कम्पुटर", font="normal 14 bold")
 
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
 
l4 = Label(root,
           text="",
           font="normal 20 bold",
           bg="red",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text="ढुंगा",
            font=16, width=7,
            command=isrock)
 
b2 = Button(frame1, text="कागज ",
            font=16, width=7,
            command=ispaper)
 
b3 = Button(frame1, text="कैची ",
            font=16, width=7,
            command=isscissor)
 
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)
 
Button(root, text="Reset Game",
       font=10, fg="black",
       bg="blue", command=reset_game).pack(pady=20)
 
root.mainloop()