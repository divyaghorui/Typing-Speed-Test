from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()
window.geometry('450x200')

x = 0

def game():
    global x
    if x==0:
        window.destroy()
        x = x+1

    def check_result():
        if entry.get() == words[word]:
            end = timer()
            print("Your time was {} seconds".format(end-start))
        else:
            print("Wrong spelling!!")

    words = ['programming', 'coding', 'samosa', 'tea', 'blahblah', 'youtube', 'python', 'college']
    word = random.randint(0, (len(words) - 1))
    start = timer()
    windows = Tk()
    windows.geometry('450x200')
    x2 = Label(windows, text=words[word], font="times 20")
    x2.place(x=70, y=50)
    x3 = Label(windows, text="Let's see how fast you can type....", font="times 20")
    x3.place(x=10, y=10)
    entry = Entry(windows)
    entry.place(x=280, y=55)
    b2 = Button(windows, text='SUBMIT', command=check_result, width=12, bg='gray')
    b2.place(x=150, y=100)
    b3 = Button(windows, text='TRY AGAIN', command=game, width=12, bg='gray')
    b3.place(x=250, y=100)
    windows.mainloop()

x1 = Label(window, text = "Let's start this game ... ", font = "times")
x1.place(x=10, y=10)

b1 = Button(window, text = 'START', command = game, width = 12, bg = 'gray')
b1.place(x = 150, y = 100)

window.mainloop()
