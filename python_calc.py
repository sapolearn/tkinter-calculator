from tkinter import*

# define window
root = Tk()
root.title("python calculator")
root.configure(bg = "black")
# root.geometry("400x450")

#define click function
def click(num):
    return

def clear():
    e.delete(0,END)


# create textbox
e = Entry(root,bd = 5,width = 80)
e.grid(row= 0, column = 0,padx = 20, pady = 15)


#create buttons
num_1 = Button(root,text = "1",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_2 = Button(root,text = "2",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_3 = Button(root,text = "3",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_4 = Button(root,text = "4",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_5 = Button(root,text = "5",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_6 = Button(root,text = "6",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_7 = Button(root,text = "7",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_8 = Button(root,text = "8",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_9 = Button(root,text = "9",bd = 4, padx = 20, pady = 15, command = lambda:click(1))

num_0 = Button(root,text = "0",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_dot = Button(root,text = ".",bd = 4, padx = 20, pady = 15, command = lambda:click(1))

num_add = Button(root,text = "+",bd = 4, padx = 20, pady = 35, command = lambda:click(1))
num_subtract = Button(root,text = "-",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_multiply = Button(root,text = "*",bd = 4, padx = 20, pady = 15, command = lambda:click(1))
num_divide = Button(root,text = "/",bd = 4, padx = 20, pady = 15, command = lambda:click(1))

num_equal = Button(root,text = "=",bd = 4, padx = 50, pady = 15, command = lambda:click(1))
num_clear = Button(root,text = "clear",bd = 4, padx = 20, pady = 15, command = clear)





#place buttons
num_1.grid(row = 3,column= 0)
num_2.grid(row = 3,column= 1)
num_3.grid(row = 3,column= 2)

num_4.grid(row = 2,column= 0)
num_5.grid(row = 2,column= 1)
num_6.grid(row = 2,column= 2)

num_7.grid(row = 1,column= 0)
num_8.grid(row = 1,column= 1)
num_9.grid(row = 1,column= 2)

num_dot.grid(row = 4,column= 0)
num_0.grid(row = 4,column= 1)
num_clear.grid(row = 4,column= 2)

num_add.grid(row = 1,column= 3)
num_subtract.grid(row = 2,column= 3)
num_multiply.grid(row = 3,column= 3)
num_divide.grid(row = 4,column= 3)

num_equal.grid(row = 5,column= 0)



root.mainloop()