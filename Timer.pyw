#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Timer.pyw
Author tatsuyanttr
2018/06/26

'''
import datetime as dt
import sys
import tkinter as Tk


class Timer(Tk.Frame):
    
    def say(self, text, cr=True):
        def x():
            self.message(text, cr)
        return x

    def count(self, event):
        txt = self.EditBox.get()
        ap = self.now.strftime("%H:%M:%S") +" " + txt
        self.message(ap)
        self.EditBox.delete(0, Tk.END)
        
    def message(self, text, cr=True):
        if cr :
            self.Txa.insert(Tk.END,text + "\n")
        else :
            self.Txa.insert(Tk.END,text)
        self.Txa.see(Tk.END)

    def update(self):
        self.now = dt.datetime.now()
        self.btext.set(self.now.strftime("%H:%M:%S"))
        #self.message(time.strftime("%H%M%S"))
        if(self.now.strftime("%M%S") == "0000"):
            self.message(self.now.strftime("%H") + u"時になりました")
        elif (self.now.strftime("%M%S") == "5000"):
            self.message(u"少し休みませんか？")
        self.after(1000,self.update)

    def __init__(self, master=None):
        
        self.now = dt.datetime.now()
        Tk.Frame.__init__(self, master)
        self.master.title('Timer')
    
        self.btext = Tk.StringVar(self)
        self.btext.set('1')

        self.Label = Tk.Label(self, textvariable=self.btext)
        self.Label.pack()

        self.Txa= Tk.Text(self)
        self.Txa.pack(fill = Tk.BOTH, expand=1)
         
        self.EditBox = Tk.Entry(self)
        self.EditBox.bind('<Return>', self.count)
        self.EditBox.pack(side = Tk.BOTTOM, fill =Tk.X)

        self.Button = Tk.Button(self, text=u'☀', fg='orange', command=self.say(u'☀',cr=False))
        self.Button.pack()
        self.Button2 = Tk.Button(self, text=u'☁', fg='cyan', command=self.say(u"☁",cr=False))
        self.Button2.pack()
        self.Button3 = Tk.Button(self, text=u'☂', fg='blue', command=self.say(u"☂",cr=False))
        self.Button3.pack()







root = Tk.Tk()
app = Timer(master=root)
app.EditBox.focus_set()
app.pack(fill = Tk.BOTH, expand=1)
app.update()
app.mainloop()
    
