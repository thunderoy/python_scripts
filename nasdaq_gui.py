#!/usr/bin/env python3

import requests
from tkinter import *

class window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()
        
    def init_window(self):
      # self.master.title("GUI")
      
        self.gobutton = Button(self, text="Go", command=self.nasdaq)
        self.gobutton.grid(row=6, column=2, sticky=W)
        
        self.quitbutton = Button(self, text="cancel", command=self.Exit)
        self.quitbutton.grid(row=6, column=0, sticky=E)
        
        self.label1 = Label(self, text="Enter Nasdaq Symbol of any Company:")
        self.label1.grid(row=0, column=0, columnspan=2, sticky=W)
        
        self.label2 = Label(self, text="Nasdaq Value is:")
        self.label2.grid(row=3, column=0, columnspan=2, sticky=W)
        
        self.entry = Entry(self)
        self.entry.grid(row=1, column=1, rowspan=2, sticky=W)
        
        self.txt = Text(self, width=40, height=3)
        self.txt.grid(row=4, column=1, columnspan=2, rowspan=2, sticky=W)
        
    def nasdaq(self):
        try:
            self.nasdaq_value()
        except requests.exceptions.ConnectionError:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "No internet connection :(")
        
    def nasdaq_value(self):
        self.n_s = self.entry.get()
        payload = {'s': self.n_s, 'f': 'l1'}
        res = requests.get('http://download.finance.yahoo.com/d/quotes.csv', params=payload)
        # print(res.raise_for_status())

        if res.text == 'N/A\n':
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, 'Wrong Nasdaq Symbol. Please Try Again.')
        else:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, res.text.strip())

        
    def Exit(self):
        exit()
        
        
root = Tk()
root.geometry("1000x500")
root.title("Nasdaq Value")
app = window(root)
root.mainloop()
