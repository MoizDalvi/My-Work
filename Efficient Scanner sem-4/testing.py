from tkinter import *
from tkinter import ttk
#Creating main window
root = Tk()

def Input_Box():
    # creating a top window
    master_2 = Toplevel(root)

    #Textboxes
    user_name = Entry(master_2)
    user_name.grid(row = 1, column = 2)


    label_un = ttk.Label(master_2, text = "Enter File Name")
    label_un.grid(row = 1, column = 1)


    get_button = Button(master_2, text = "Confirm", command = lambda: getname(user_name))
    get_button.grid(row=1, column = 3)
    master_2.mainloop() 

def getname(user_name):
    
    input = user_name.get()
    print(input)


call_button = Button(root, text='Enter Usrnm and pwd', command = Input_Box)
call_button.pack()
root.mainloop()