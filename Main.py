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
        root.geometry("240x150")
        root.title('Sounding Application')
        root.resizable(0, 0)

        #Configure Application Grid
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)

        #Range Label & Entry
        range_label = tk.Label(root, text="Enter Range:")
        range_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        range_entry = tk.Entry(root)
        range_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        #Depth Label & Entry
        depth_label = tk.Label(root, text="Enter Depth:")
        depth_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        depth_entry = tk.Entry(root)
        depth_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        
        #Find Function & Button
        def find():
            #Ensure Entrys are valid numbers
            try:
                query_range = float(range_entry.get())
                query_depth = float(depth_entry.get())
                answer.set(f"Answer: {self.sounding.findData(query_range,query_depth)}")
            
            #Raise Error otherwise
            except:
                tk.messagebox.showinfo("Error",  "Please enter valid numbers.")

        find_button = tk.Button(root, text="Accept",command=find)
        find_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        #Answer Label
        answer = tk.StringVar()
        answer.set("Answer Printed Here")
        answer_label = tk.Label(root, textvariable=answer,bg='white')
        answer_label.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

        root.mainloop()



#----------------------------------------------------------------------------------
#                                  MAIN LOOP
#----------------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sounding Applicaiton")
    parser.add_argument("-file", help="Data file to read.",default="./Data.txt")
    args   = parser.parse_args()

    