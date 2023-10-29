from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('Tik Tak Toe')
frm = ttk.Frame(window, padding=10)
frm.grid()

playerX = True


def winnerInfo():
    if playerX == True:
            messagebox.showinfo('The winner is...', 'The winner is... Player O')
    elif playerX == False:
            messagebox.showinfo('The winner is...', 'The winner is... Player X')



def winnerIs():
    if btn1["text"] != "?" and btn1["text"] == btn2["text"] and btn1["text"] == btn3["text"]:
        btn1.config(fg = "green")
        btn2.config(fg = "green")
        btn3.config(fg = "green")
        btn4.config(state = DISABLED)
        btn5.config(state = DISABLED)
        btn6.config(state = DISABLED)
        btn7.config(state = DISABLED)
        btn8.config(state = DISABLED)
        btn9.config(state = DISABLED)
        winnerInfo()

    if btn4["text"] != "?" and btn4["text"] == btn5["text"] and btn4["text"] == btn6["text"]:
        btn4.config(fg = "green")
        btn5.config(fg = "green")
        btn6.config(fg = "green")
        btn1.config(state = DISABLED)
        btn2.config(state = DISABLED)
        btn3.config(state = DISABLED)
        btn7.config(state = DISABLED)
        btn8.config(state = DISABLED)
        btn9.config(state = DISABLED)
        winnerInfo()

    if btn7["text"] != "?" and btn7["text"] == btn8["text"] and btn7["text"] == btn9["text"]:
        btn7.config(fg = "green")
        btn8.config(fg = "green")
        btn9.config(fg = "green")
        btn1.config(state = DISABLED)
        btn2.config(state = DISABLED)
        btn3.config(state = DISABLED)
        btn4.config(state = DISABLED)
        btn5.config(state = DISABLED)
        btn6.config(state = DISABLED)
        winnerInfo()

    if btn1["text"] != "?" and btn1["text"] == btn4["text"] and btn1["text"] == btn7["text"]:
        btn1.config(fg = "green")
        btn4.config(fg = "green")
        btn7.config(fg = "green")
        btn5.config(state = DISABLED)
        btn2.config(state = DISABLED)
        btn3.config(state = DISABLED)
        btn6.config(state = DISABLED)
        btn8.config(state = DISABLED)
        btn9.config(state = DISABLED)
        winnerInfo()

    if btn2["text"] != "?" and btn2["text"] == btn5["text"] and btn2["text"] == btn8["text"]:
        btn2.config(fg = "green")
        btn5.config(fg = "green")
        btn8.config(fg = "green")
        btn1.config(state = DISABLED)
        btn4.config(state = DISABLED)
        btn3.config(state = DISABLED)
        btn7.config(state = DISABLED)
        btn6.config(state = DISABLED)
        btn9.config(state = DISABLED)
        winnerInfo()

    if btn3["text"] != "?" and btn3["text"] == btn6["text"] and btn3["text"] == btn9["text"]:
        btn3.config(fg = "green")
        btn9.config(fg = "green")
        btn6.config(fg = "green")
        btn1.config(state = DISABLED)
        btn2.config(state = DISABLED)
        btn4.config(state = DISABLED)
        btn7.config(state = DISABLED)
        btn8.config(state = DISABLED)
        btn5.config(state = DISABLED)
        winnerInfo()

    if btn1["text"] != "?" and btn1["text"] == btn5["text"] and btn1["text"] == btn9["text"]:
        btn1.config(fg = "green")
        btn5.config(fg = "green")
        btn9.config(fg = "green")
        btn6.config(state = DISABLED)
        btn2.config(state = DISABLED)
        btn3.config(state = DISABLED)
        btn7.config(state = DISABLED)
        btn8.config(state = DISABLED)
        btn4.config(state = DISABLED)
        winnerInfo()

    if btn3["text"] != "?" and btn3["text"] == btn5["text"] and btn3["text"] == btn7["text"]:
        btn3.config(fg = "green")
        btn5.config(fg = "green")
        btn7.config(fg = "green")
        btn1.config(state = DISABLED)
        btn2.config(state = DISABLED)
        btn4.config(state = DISABLED)
        btn6.config(state = DISABLED)
        btn8.config(state = DISABLED)
        btn9.config(state = DISABLED)
        winnerInfo()


def xOro(btn):
    global playerX
    if btn["text"] == "?" and playerX == True:
        btn["text"] = "X"
        playerX = False
        winnerIs()
    elif btn["text"] == "?" and playerX == False:
        btn["text"] = "O"
        playerX = True
        winnerIs()


btn1 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn1))
btn1.grid(column=1, row=1)
btn2 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn2))
btn2.grid(column=2, row=1)
btn3 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn3))
btn3.grid(column=3, row=1)

btn4 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn4))
btn4.grid(column=1, row=2)
btn5 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn5))
btn5.grid(column=2, row=2)
btn6 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn6))
btn6.grid(column=3, row=2)

btn7 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn7))
btn7.grid(column=1, row=3)
btn8 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn8))
btn8.grid(column=2, row=3)
btn9 = Button(window, text = "?",font="Arial 50 bold", fg= "blue", command = lambda:xOro(btn9))
btn9.grid(column=3, row=3)
window.mainloop()