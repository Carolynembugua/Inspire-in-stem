from tkinter import *

window = Tk()
window.title("Welcome to my App")
window.configure(bg = 'pastelpurple')
#window.geometry(400 x 400) #fix window size
u_name = Label(window,text = "user name" , font = ("Arial",20))
f_name = Label(window,text = "first name" , font = ("Arial",20))
s_name = Label(window,text = "second name ", font = ("Arial",20))
p_name = Label(window,text = "type password", font = ("Arial",20))

u_name.grid(column = 100, row = 120)
f_name.grid(column = 100,row  = 120)
s_name.grid(column = 100, row = 120)
p_name.grid(column = 100, row = 120)

btn = Button(window,text = "click here",bg = 'blue',fg = 'red', command = open)

btn.grid(column = 120,row = 150)
f_name = Entry(window,width = 20)
s_name = Entry(window,width = 20)

f_name.grid(column = 100, row = 120)
s_name.grid(column = 100 , row = 120)

def open_popup() :
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("pop up window")
    top.configure(bg = 'white')
    msg = Label(top , text = "Welcome to the pop up")