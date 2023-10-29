from tkinter import *
from tkinter import ttk
window = Tk()
frm = ttk.Frame(window, padding=10)
frm.grid()

ttk.Label(frm, text="TIK TAK TOE").grid(column=1, row=0)
btn1 = Button(window, text = "1").grid(column=1, row=1)
btn1 = Button(window, text = "1",font="Arial 50 bold", fg= "blue").grid(column=1, row=1)
btn2 = Button(window, text = "2",font="Arial 50 bold", fg= "blue").grid(column=2, row=1)
btn3 = Button(window, text = "3",font="Arial 50 bold", fg= "blue").grid(column=3, row=1)

btn4 = Button(window, text = "4",font="Arial 50 bold", fg= "blue").grid(column=1, row=2)
btn5 = Button(window, text = "5",font="Arial 50 bold", fg= "blue").grid(column=2, row=2)
btn6 = Button(window, text = "6",font="Arial 50 bold", fg= "blue").grid(column=3, row=2)

btn7 = Button(window, text = "7",font="Arial 50 bold", fg= "blue").grid(column=1, row=3)
btn8 = Button(window, text = "8",font="Arial 50 bold", fg= "blue").grid(column=2, row=3)
btn9 = Button(window, text = "9",font="Arial 50 bold", fg= "blue").grid(column=3, row=3)
window.mainloop()
