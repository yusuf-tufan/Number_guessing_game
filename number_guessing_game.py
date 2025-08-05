import random
import time
from tkinter import *

window=Tk()
window.minsize(700,700)
window.config(pady=50)

list_num=[]
right_guess=5
def range_num():

    try:
        user_range=int(enter_range.get())
        num = random.randint(0, user_range)
        list_num.clear()
        list_num.append(num)

    except:

        error_lbl=Label(text='Just enter a number!', width=20, height=6, bg='light green', fg='black',font=('Arial', 10, 'bold'))
        error_lbl.place(x=260, y=240)


def guess_num():
    global right_guess

    try:
        user_input=int(enter_num.get())
        if user_input == list_num[0]:
            lbl_num = Label(text=f'True Guess\nNumber was {list_num[0]}\nShuffle the numbers\nto play again.', width=20, height=6, bg='light green', fg='black',font=('Arial', 10, 'bold'))
            lbl_num.place(x=260, y=240)
        else:
            lbl_error = Label(text='Wrong Number\nTry another number.', width=20, height=6, bg='light green', fg='black',font=('Arial', 10, 'bold'))
            lbl_error.place(x=260, y=240)
    except:
        error_lbl=Label(text='Just enter a number!', width=20, height=6, bg='light green', fg='black',font=('Arial', 10, 'bold'))
        error_lbl.place(x=260, y=240)


    if right_guess==0:
        lbl_end=Label(text=f'Your rights are over\nNumber was {list_num[0]}\nShuffle the numbers\nto play again.', width=20, height=6, bg='light green', fg='black',font=('Arial', 10, 'bold'))
        lbl_end.place(x=260, y=240)
        list_num.clear()
    right_guess = right_guess - 1
#lbl enter (0,input)
lbl_numberrange=Label(text='Guess between 0 and the number you write.',font=('Arial',15,'bold'))
lbl_numberrange.place(x=140,y=0)
#enter range
enter_range=Entry(width=10,bg='white',fg='black',font=('Arial',15,'bold'))
enter_range.place(x=260,y=35)

#button range
range_button=Button(text='Shuffle Number.',width=15,bg='light blue',command=range_num)
range_button.place(x=260,y=75)


#lbl enter num
lbl_enter=Label(text='Enter Your Guess',font=('Arial',15,'bold'))
lbl_enter.place(x=230,y=125)
#enter num
enter_num=Entry(width=10,bg='white',fg='black',font=('Arial',15,'bold'))
enter_num.place(x=260,y=150)
#button guess
guess_button=Button(text='Guess',width=15,bg='light blue',command=guess_num)
guess_button.place(x=260,y=190)

window.mainloop()