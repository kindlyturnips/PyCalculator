#----------------------------------------------------------------------------------
#                                PyCalc.py                
# Simple Calculator Application
#
#10/09/2023
#Created by Christopher Turnipseed
#
#----------------------------------------------------------------------------------

import argparse
import numpy as np
import tkinter as tk
import tkinter.messagebox
import lib.CONFIG as config
import lib.FUNCT as funct

   
#----------------------------------------------------------------------------------
#                                  GUI OBJECT
#----------------------------------------------------------------------------------
class Application(object):
    def __init__(self,object):
        #Pass Operations object
        self.calc = object

    #Main Window
    def MainWindow(self):
        #Root window
        root = tk.Tk()
        root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        root.title(config.NAME)
        root.resizable(0, 0)

        #Num Buttons & Placement  
        #Num 0
        num_button = tk.Button(root, text="0", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH, 
                        command= lambda i="0": (self.calc.setNum(i),diag.set(self.calc.getEq()),))
        num_button.grid(column=1, row=6, sticky=tk.E)

        #Num 1 - 9
        nb_row = 5
        nb_col = 0
        for i in range(1,10):
            num_button = tk.Button(root, text=f"{i}", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                                command= lambda i=f"{i}": (self.calc.setNum(i),diag.set(self.calc.getEq()),))
            num_button.grid(column=nb_col, row=nb_row, sticky=tk.E)
            if nb_col == 2:
                nb_col=0
                nb_row-=1
            else:
                nb_col+=1

        #Operations Button & Placement
        ob_row = 5
        ob_col = 3
        for item in ["+","-","×","÷"]:
            oper_button = tk.Button(root, text=item, height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                                command=lambda i=item: (self.calc.setOper(i),diag.set(self.calc.getEq()),))
            oper_button.grid(column=ob_col, row=ob_row, sticky=tk.E)
            ob_row-=1

        #Bot Row
        #Decimal Button
        bot_row = 6
        dec_button = tk.Button(root, text=".", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH, 
                            command=lambda: (self.calc.setDec(),diag.set(self.calc.getEq()),))
        dec_button.grid(column=2, row=bot_row, sticky=tk.E)
        #Pos/Neg Button
        pn_button = tk.Button(root, text="⁻/₊", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.setPosNeg(),diag.set(self.calc.getEq()),))
        pn_button.grid(column=0, row=bot_row, sticky=tk.E)
        #Equal Button
        eq_button = tk.Button(root, text="=", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.solve(),diag.set(self.calc.getEq()),))
        eq_button.grid(column=3, row=bot_row, sticky=tk.E)

        #Top Row
        #% Button
        top_row = 1
        per_button = tk.Button(root, text="%", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.setPer(),diag.set(self.calc.getEq()),))
        per_button.grid(column=0, row=top_row, sticky=tk.E)
        #CE Button, clears current num
        ce_button = tk.Button(root, text="CE", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.numClear(),diag.set(self.calc.getEq()),))
        ce_button.grid(column=1, row=top_row, sticky=tk.E)
        #C Button, clears all
        c_button = tk.Button(root, text="C", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.fullClear(),diag.set(self.calc.getEq()),))
        c_button.grid(column=2, row=top_row, sticky=tk.E)
        #Bcsp Button, ⌫
        bcsp_button = tk.Button(root, text="⌫", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.delChar(),diag.set(self.calc.getEq()),))
        bcsp_button.grid(column=3, row=top_row, sticky=tk.E)

        #2nd Row
        #Inverse Button
        inv_button = tk.Button(root, text="1/x", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.invNum(),diag.set(self.calc.getEq()),))
        inv_button.grid(column=0, row=top_row+1, sticky=tk.E)
        #Squared Button
        sq_button = tk.Button(root, text="x²", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.sqNum(),diag.set(self.calc.getEq()),))
        sq_button.grid(column=1, row=top_row+1, sticky=tk.E)
        #Square Root Button
        sqrt_button = tk.Button(root, text="√(x)", height = config.BUTTON_HEIGHT, width  = config.BUTTON_WIDTH,
                              command=lambda: (self.calc.sqrtNum(),diag.set(self.calc.getEq()),))
        sqrt_button.grid(column=2, row=top_row+1, sticky=tk.E)

        #Display
        #Answer Label & Position
        diag = tk.StringVar()
        diag.set(self.calc.getEq())
        diag_label = tk.Label(root, textvariable=diag,bg='white')
        diag_label.grid(column=0, row=0, columnspan=4, sticky="ew")
        root.mainloop()


#----------------------------------------------------------------------------------
#                                  MAIN LOOP
#----------------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simply Python Calcultaor")
    #parser.add_argument("-file", help="Data file to read.",default="./Data.txt")
    args   = parser.parse_args()
    maths = funct.Operations()
    Application(maths).MainWindow()
    