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
        #Pass Souding object
        self.sounding = object

    #Main Window
    def MainWindow(self):
        #Root window
        root = tk.Tk()
        root.geometry(f"{config.WINDOW_HEIGHT}x{config.WINDOW_WIDTH}")
        root.title('Simple Python Calculator by Chris')
        root.resizable(0, 0)

        #Configure Application Grid
        """root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)"""

        #Range Label & Entry
        """range_label = tk.Label(root, text="Enter Range:")
        range_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        range_entry = tk.Entry(root)
        range_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5) """
        
        #Depth Label & Entry
        """depth_label = tk.Label(root, text="Enter Depth:")
        depth_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        depth_entry = tk.Entry(root)
        depth_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
         """

        #Num Function
        def num():
            pass

        def oper():
            pass
        
        #Num Buttons & Placement
        num_button = tk.Button(root, text=f"0",command=num,
                               height = config.BUTTON_HEIGHT,
                               width  = config.BUTTON_WIDTH)
        num_button.grid(column=1, row=5, sticky=tk.E)

        nb_row = 4
        nb_col = 0
        for i in range(1,10):
            print(nb_row,nb_col)
            num_button = tk.Button(root, text=f"{i}",command=num,
                               height = config.BUTTON_HEIGHT,
                               width  = config.BUTTON_WIDTH)
            num_button.grid(column=nb_col, row=nb_row, sticky=tk.E)
            if nb_col == 2:
                nb_col=0
                nb_row-=1
            else:
                nb_col+=1

        #Operations Button & Placement
        ob_row = 5
        ob_col = 3
        for item in ["+","-","x","÷"]:
            add_button = tk.Button(root, text=item,command=oper,
                               height = config.BUTTON_HEIGHT,
                               width  = config.BUTTON_WIDTH)
            add_button.grid(column=ob_col, row=ob_row, sticky=tk.E)
            ob_row-=1

        #Answer Label & Position
        answer = tk.StringVar()
        answer.set("Answer ")
        answer_label = tk.Label(root, textvariable=answer,bg='white')
        answer_label.grid(column=0, row=0, columnspan=4, sticky="ew")
        
        root.mainloop()



#----------------------------------------------------------------------------------
#                                  MAIN LOOP
#----------------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simply Python Calcultaor")
    #parser.add_argument("-file", help="Data file to read.",default="./Data.txt")
    args   = parser.parse_args()
    data = funct.Operations()

    Application(data).MainWindow()
    