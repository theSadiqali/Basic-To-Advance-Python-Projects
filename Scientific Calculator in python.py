                        #=========================#
                        #  Scientific Calculator  #
                        #-------------------------#
                        #        YOUTUBE          #
                        #   thesadiqali channel   #
                        #   PYTHON PROJECT        #
                        #   BASIC TO ADVANCE      #
                        #=========================#

https://www.youtube.com/@Thesadiqali11
#first of all,
#lets import packages
from tkinter import Tk
from tkinter import StringVar, Entry, Button
from math import pi, e, sin, tan, log, log10, ceil, degrees,radians, exp, asin, acos, floor
from tkinter import *
import numpy as np

#run that
#zero errors. if it showing you error, then you have to install all of the library in cmd

#let me give you the list. how you can install them
# pip install tk
# pip install numpy
# cmd prompt

class calculator(Tk):
    def __init__(self):
        super().__init__()

        self.title(' Scientific Calculator ')
        self.geometry('450x450')
        self.configure(background="white")
        self.string = StringVar()
        entry = Entry(self, textvariable=self.string, font=('Arial', 16), width=30)  
        entry.grid(row=0, column=0, columnspan=10)
        entry.configure(background="white")
        self.btn_bg_color = 'gold'
        entry.focus()
        
        #values in calculator style. make sure
        values = ["7", "8", "9", "/", "%", "clear", "AC",
                  "4", "5", "6", "*", "(", ")", "**",
                  "1", "2", "3", "-", "=", ",", "0", ".", "min", "+", "sin", "asin", "cos", "acos", "tan()",
                  "pow", "log10", "max", "abs", "floor", "pi", "e", "log", "ceil", "degrees", "radians"]
        text = 1
        i = 0
        row = 1
        col = 0
        button_paramas = {'bd':3, 'fg':'#000000', 'bg':'#FFFFFF', 'font':('Arial', 10, 'bold')}
        
        for txt in values:
            padx = 10
            pady = 10
            if (i == 7):
                row = 2
                col = 0
            if (i == 14):
                row = 3
                col = 0
            if (i == 19):
                row = 4
                col = 0
            if (i == 26):
                row = 5
                col = 0
            if (i == 33):
                row = 6
                col = 0
            if (txt == '='):
                btn = Button(self, button_paramas, height=2, width=4, padx=70, pady=pady, text=txt,
                             command=lambda txt=txt: self.equals())
                btn.grid(row=row, column=col, columnspan=3, padx=2, pady=2)
                btn.configure(background="cyan")

            elif (txt == 'clear'):
                btn = Button(self, button_paramas, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.delete())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="dark red")
            elif (txt == 'AC'):
                btn = Button(self, button_paramas, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.clearall())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="dark red")
            else:
                btn = Button(self, button_paramas, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.addChar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background=self.btn_bg_color)
            col = col + 1
            i= i + 1
        Menue_1 = Menu(self)
        
        self.mainloop()

    def clearall(self):
        self.string.set("")

    def equals(self):
        result = ""

        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "ERROR"
        self.string.set(result)

    def addChar(self, char):
        self.string.set(self.string.get() + (str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])


calculator()

#lets chaeck 
#right now we have zero errors
    
