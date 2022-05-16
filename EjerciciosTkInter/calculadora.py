from tkinter import *
from tkmacosx import Button

root = Tk()
root.configure(background="#333")
root.title("Calculadora")
root.geometry("386x168")

equation=StringVar()

def press(num):
    equation.set(equation.get()+str(num))
    print(equation.get())

def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set("ERROR")

def clear():
    equation.set("")
expression_entry = Entry(root, textvariable=equation)
expression_entry.grid(row=0,columnspan=4, sticky='nsew')

btn7= Button(root, text="7", fg="white", bg="#666", command=lambda:press(7))
btn7.grid(row=1, column=0, sticky='nsew')

btn8= Button(root, text="8", fg="white", bg="#666", command=lambda:press(8))
btn8.grid(row=1, column=1, sticky='nsew')

btn9= Button(root, text="9", fg="white", bg="#666", command=lambda:press(9))
btn9.grid(row=1, column=2, sticky='nsew')


btn4= Button(root, text="4", fg="white", bg="#666", command=lambda:press(4))
btn4.grid(row=2, column=0, sticky='nsew')

btn5= Button(root, text="5", fg="white", bg="#666", command=lambda:press(5))
btn5.grid(row=2, column=1, sticky='nsew')

btn6= Button(root, text="6", fg="white", bg="#666", command=lambda:press(6))
btn6.grid(row=2, column=2, sticky='nsew')


btn1= Button(root, text="1", fg="white", bg="#666", command=lambda:press(1))
btn1.grid(row=3, column=0, sticky='nsew')

btn2= Button(root, text="2", fg="white", bg="#666", command=lambda:press(2))
btn2.grid(row=3, column=1, sticky='nsew')

btn3= Button(root, text="3", fg="white", bg="#666", command=lambda:press(3))
btn3.grid(row=3, column=2, sticky='nsew')

btn0= Button(root, text="0", fg="white", bg="#666", command=lambda:press(0))
btn0.grid(row=4, column=0, sticky='nsew', columnspan=2)

btnDecimal= Button(root, text=" . ", fg="white", bg="#666", command=lambda:press("."))
btnDecimal.grid(row=4, column=2, sticky='nsew')



btnSuma= Button(root, text=" + ", fg="white", bg="#fe9727", command=lambda:press("+"))
btnSuma.grid(row=1, column=3, sticky='nsew')

btnMenos= Button(root, text=" - ", fg="white", bg="#fe9727", command=lambda:press("-"))
btnMenos.grid(row=2, column=3, sticky='nsew')


btnMultiplicacion= Button(root, text=" * ", fg="white", bg="#fe9727", command=lambda:press("*"))
btnMultiplicacion.grid(row=3, column=3, sticky='nsew')


btnDivision= Button(root, text=" / ", fg="white", bg="#fe9727", command=lambda:press("/"))
btnDivision.grid(row=4, column=3, sticky='nsew')

btnEqual= Button(root, text=" = ", fg="white", bg="#fe9727", command=equalpress)
btnEqual.grid(row=5, column=3, sticky='nsew')

btnClear= Button(root, text="CLEAR", fg="white", bg="#999", command=clear)
btnClear.grid(row=5, column=2, sticky='nsew')


root.mainloop()