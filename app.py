from tkinter import *
from tkinter import messagebox


def setText(btn):
    global displayText
    temp = displayText.get() + str(btn)
    displayText.set(temp)

def calculate():
    global displayText
    try:
        result = eval(displayText.get())
        displayText.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Cannot divide by zero')
    except:
        messagebox.showerror('Error', 'Error occurred')


def clearText():
    global displayText
    displayText.set('')

root = Tk()
root.title('Calculator')
root.geometry('500x450')

displayText = StringVar()

label = Label(root, font=('Arial', 30), bg='lightgrey', width=20, pady=10, textvariable=displayText)
label.pack()

frame = Frame(root)
frame.pack()

num1 = Button(frame, text='1', width=3, font=('Arial',20), command=lambda: setText(1))
num1.grid(row=0, column=0)
num2 = Button(frame, text='2', width=3, font=('Arial',20), command=lambda: setText(2))
num2.grid(row=0, column=1)
num3 = Button(frame, text='3', width=3, font=('Arial',20), command=lambda: setText(3))
num3.grid(row=0, column=2)
num4 = Button(frame, text='4', width=3, font=('Arial',20), command=lambda: setText(4))
num4.grid(row=1, column=0)
num5 = Button(frame, text='5', width=3, font=('Arial',20), command=lambda: setText(5))
num5.grid(row=1, column=1)
num6 = Button(frame, text='6', width=3, font=('Arial',20), command=lambda: setText(6))
num6.grid(row=1, column=2)
num7 = Button(frame, text='7', width=3, font=('Arial',20), command=lambda: setText(7))
num7.grid(row=2, column=0)
num8 = Button(frame, text='8', width=3, font=('Arial',20), command=lambda: setText(8))
num8.grid(row=2, column=1)
num9 = Button(frame, text='9', width=3, font=('Arial',20), command=lambda: setText(9))
num9.grid(row=2, column=2)
num0 = Button(frame, text='0', width=3, font=('Arial',20), command=lambda: setText(0))
num0.grid(row=3, column=0)

period = Button(frame, text='.', width=3, font=('Arial',20), command=lambda: setText('.'))
period.grid(row=3, column=1)

plus = Button(frame, text='+', width=3, font=('Arial',20), command=lambda: setText('+'))
plus.grid(row=0, column=3)
minus = Button(frame, text='-', width=3, font=('Arial',20), command=lambda: setText('-'))
minus.grid(row=1, column=3)
multiply = Button(frame, text='x', width=3, font=('Arial',20), command=lambda: setText('*'))
multiply.grid(row=2, column=3)
divide = Button(frame, text='/', width=3, font=('Arial',20), command=lambda: setText('/'))
divide.grid(row=3, column=3)
equal = Button(frame, text='=', width=3, font=('Arial',20), command=lambda: calculate())
equal.grid(row=3, column=2)
clearbtn = Button(root, text='Clear', font=('Arial',20), command=lambda: clearText())
clearbtn.pack()


root.mainloop()
