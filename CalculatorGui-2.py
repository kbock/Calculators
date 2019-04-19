from tkinter import*

#ADDED 4/17/19
from functools import partial
#END OF ADDED

import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        if self.op == 'sub':
            self.total -= self.current
        if self.op == 'multi':
            self.total *= self.current
        if self.op == 'divide':
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    #ADDED 4/17/19
    def display2(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
    #===============

    def opPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()
root = Tk()
root.title("Inches to MM Conversion Calculator")
root.resizable(width = False, height = False)
calc = Frame(root)
calc.grid()

#==================================================Row0===================================================

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg = "powder blue", bd=10, width = 18, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=3, pady=1, sticky=W+E+S+N)
txtDisplay.insert(0, "0")

inchlabel = Label(calc, pady=1, bd=4, fg='black', font=('arial', 15), text='inches').grid(row=0, column=3, pady=1, sticky=W+E+S+N)

#==================================================Row1 4/17/19===================================================

#txtDisplay2 = Entry(calc, font=('arial', 20, 'bold'), bg = "powder blue", bd=10, width = 18, justify=RIGHT)
#txtDisplay2.grid(row=1, column=0, columnspan=3, pady=1, sticky=W+E+S+N)
#txtDisplay2.insert(0, "0")

mmlabel = Label(calc, pady=1, bd=4, fg='black', font=('arial', 15), text='mm').grid(row=1, column=3, pady=1, sticky=W+E+S+N)

#==================================================Row2===================================================

btnClearEntry = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
                text='CE', command = added_value.all_Clear_Entry, bg='whitesmoke').grid(row=2, column=0, sticky=W+E+S+N)

btnClear = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
            text='C', command = added_value.Clear_Entry, bg='whitesmoke').grid(row=2, column=1, sticky=W+E+S+N)

btnSqRoot = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
            text='√', command = added_value.squared, bg='whitesmoke').grid(row=2, column=2, sticky=W+E+S+N)

btnAdd = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
            text=chr (43), bg='whitesmoke', command = lambda: added_value.operation('add')).grid(row=2, column=3, sticky=W+E+S+N)

#==================================================Row3===================================================

btn7 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 15, 'bold'), width=6, height=2,
        text='7', bg='powder blue', command = lambda: added_value.numberEnter(7)).grid(row=3, column=0, sticky=W+E+S+N)

btn8 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text='8', bg='powder blue', command = lambda: added_value.numberEnter(8)).grid(row=3, column=1, sticky=W+E+S+N)

btn9 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text='9', bg='powder blue', command = lambda: added_value.numberEnter(9)).grid(row=3, column=2, sticky=W+E+S+N)

btnSub = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
            text='-', bg='whitesmoke', command = lambda: added_value.operation('sub')).grid(row=3, column=3, sticky=W+E+S+N)

#==================================================Row4===================================================

btn4 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text='4', bg='powder blue', command = lambda: added_value.numberEnter(4)).grid(row=4, column=0, sticky=W+E+S+N)

btn5 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text='5', bg='powder blue', command = lambda: added_value.numberEnter(5)).grid(row=4, column=1, sticky=W+E+S+N)

btn6 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text='6', bg='powder blue', command = lambda: added_value.numberEnter(6)).grid(row=4, column=2, sticky=W+E+S+N)

btnDiv = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
            text='/', bg='whitesmoke', command = lambda: added_value.operation('divide')).grid(row=4, column=3, sticky=W+E+S+N)

#==================================================Row5===================================================

btn1 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text='1', bg='powder blue', command = lambda: added_value.numberEnter(1)).grid(row=5, column=0, sticky=W+E+S+N)

btn2 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text='2', bg='powder blue', command = lambda: added_value.numberEnter(2)).grid(row=5, column=1, sticky=W+E+S+N)

btn3 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text='3', bg='powder blue', command = lambda: added_value.numberEnter(3)).grid(row=5, column=2, sticky=W+E+S+N)

btnMult = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
                text='X', bg='whitesmoke', command = lambda: added_value.operation('multi')).grid(row=5, column=3, sticky=W+E+S+N)

#==================================================Row6===================================================

btnPM = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
        text=chr(177), command=added_value.opPM, bg='whitesmoke').grid(row=6, column=0, sticky=W+E+S+N)

btn0 = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
            text='0', bg='powder blue', command = lambda:added_value.numberEnter(0), ).grid(row=6, column=1, sticky=W+E+S+N)

btnDot = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
            text='.', bg='whitesmoke', command = lambda: added_value.numberEnter('.')).grid(row=6, column=2, sticky=W+E+S+N)

btnEquals = Button(calc, pady=1, bd=4, fg='black', font=('arial', 15, 'bold'), width=6, height=2,
                text='=', bg='whitesmoke', command = added_value.sum_of_total).grid(row=6, column=3, sticky=W+E+S+N)

#==============================================Key Bindings================================================



root.mainloop()