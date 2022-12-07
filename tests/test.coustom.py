from tkinter import *
import tkinter as tk
my_w = tk.Tk()
my_w.geometry("350x100") 
font1=('Times',18,'bold')	
sv = tk.StringVar() # connected to 1st Label and Spinbox
        
l1=tk.Label(my_w,text='Password',font=font1)  
l1.grid(row=1,column=1,padx=10,pady=10)
e1_str=tk.StringVar() # string variable   
e1 = tk.Entry(my_w,font=font1,width=15,show='*',textvariable=e1_str)
e1.grid(row=1,column=2,padx=5,pady=5)
c_v1=IntVar(value=0)
def my_show():
    if(c_v1.get()==1):
        e1.config(show='')
    else:
        e1.config(show='*')

c1 = tk.Checkbutton(my_w,text='Show Password',variable=c_v1,
	onvalue=1,offvalue=0,command=my_show)
c1.grid(row=2,column=1)    
my_w.mainloop()  # Keep the window open