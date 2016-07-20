#!/usr/bin/python
#ARFUMI.py
from tkinter import *
from PIL import ImageTk, Image
import sys
import socket
import datetime

#---------------------------------------------------#
#---------INITIALIZE CONNECTION VARIABLES-----------#
#---------------------------------------------------#
WindowTitle = 'ARFUMI'
HOST = ''
PORT = 60700
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#---------------------------------------------------#
#-----------------Functions-------------------------#
#---------------------------------------------------#
def Submit_Popup():
    #returns true if yes is selected, false otherwise
    return messagebox.askyesno("Verification", "Would you like to continue?") 

def Accept_Popup():
    #returns true if yes is selected, false otherwise
    return messagebox.askyesno("Verification", "Is the laser on the object?")

def Acceptable_Popup():
    #returns true if yes is selected, false otherwise
    return messagebox.askyesno("Verification", "Is this photo acceptable?")
    
#---------------------------------------------------#
#-----------------GRAPHICS MANAGEMENT---------------#
#---------------------------------------------------#

#Create Top Window
top = Tk()
top.title(WindowTitle)
top.geometry("1000x900")
top.resizable(width= False, height = True)

#Create Menu BAR
Menu_Bar = Menu(top)
top.config(menu = Menu_Bar)
#Create Menu List
File_Menu = Menu(Menu_Bar, tearoff = 0)
File_Menu.add_command(label ="New")
File_Menu.add_separator()
File_Menu.add_command(label ="Exit")
Menu_Bar.add_cascade(label = "File", menu = File_Menu)

#Create Help List
Help_Menu = Menu(Menu_Bar, tearoff = 0)
Help_Menu.add_command(label = "Tutorial")
Help_Menu.add_command(label = "About ARFUMI")

Menu_Bar.add_cascade(label = "Help", menu = Help_Menu)

#Create Status Bar
New_Status = StringVar()
Status = Label(top, textvariable = New_Status, relief = SUNKEN, bd = 1, anchor = W)
Status.pack(side = BOTTOM, fill = X)
New_Status.set("********")

#Create Input Frame to the left
Input_Frame = Frame(top, bg = "#cc99ff")
Input_Frame.pack(side = LEFT, expand = True, fill = BOTH)

#Create Label for Horizontal
Horizontal_Label = Label(Input_Frame, text = "HORIZONTAL [0 - 24]", bg = "#cc99ff")
Horizontal_Label.grid(column = 0, row = 0, ipady = 110)

#Create EntryBox for Horizontal
Horizontal_Var = StringVar()
Horizontal = Entry(Input_Frame, textvariable = Horizontal_Var, bd = 6)
Horizontal.grid(column = 1, row = 0)

#Create Label for Vertical
Vertical_Label = Label(Input_Frame, text = "VERTICAL [0 - 24]", bg = "#cc99ff")
Vertical_Label.grid(column = 0, row = 1, sticky = E)

#Create EntryBox for Vertical
Vertical_Var = StringVar()
Vertical = Entry(Input_Frame, textvariable = Vertical_Var, bd = 6)
Vertical.grid(column = 1, row = 1)

#Create Submit Button for Horizontal and Vertical Components                   
submit = Button(Input_Frame, text = "SUBMIT", command = Submit_Popup, bg = "#ffe066", activeforeground = "#b800e6", activebackground = "white")
submit.grid(column = 1, row = 2, ipady = 5, ipadx = 5, pady = 20)

#Create label for Distance
Distance_Label = Label(Input_Frame, text = "DISTANCE [FT]", bg = "#cc99ff")
Distance_Label.grid(column = 0, row = 3, ipady = 70, sticky = E)

#Create label box to display Distance
Distance = StringVar()
Distance_Display = Label(Input_Frame, textvariable = Distance, relief = SUNKEN, bd = 6 )
Distance.set("*******")
Distance_Display.grid(column = 1, row = 3, ipadx = 45)

#Create Output Frame to the right
Output_Frame = Frame(top, bg = "#cc99ff")
Output_Frame.pack(side = RIGHT, expand = True, fill = BOTH)

#Create Image in Output Frame
image = Image.open("test.jpg")
tk_image = ImageTk.PhotoImage(image)
picture = Label(Output_Frame, image = tk_image, relief = RAISED)
picture.grid(padx = 55, pady = 100)

#Create Accept Button for Image in Output Frame
Accept_Button = Button(Output_Frame, text = "ACCEPT", command = Accept_Popup, bg = "#ffe066", activeforeground = "#b800e6", activebackground = "white")
Accept_Button.grid(ipady = 5, ipadx = 5)



top.mainloop()
