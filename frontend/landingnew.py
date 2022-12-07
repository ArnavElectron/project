import customtkinter
import tkinter.messagebox
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inventory Management System")
        self.geometry(f"{600}x{500}")
        self.entry = customtkinter.CTkEntry(self, placeholder_text="username")
        self.entry.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="password",show="*")
        self.entry2.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        self.submitbutton = customtkinter.CTkButton(self,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Submit",
                                 command=self.submitbutton_event)
        self.submitbutton.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        
        #photo = tk.PhotoImage(file="C:\\Users\\Student\\Desktop\\show-password-icon-18.jpg")
        self.photo= customtkinter.CTkImage(Image.open("frontend/images/password_show-removebg-preview.png"),size=(20, 20))
        self.c_v1=0
        self.showbutton = customtkinter.CTkButton(self,
                                 width=20,
                                 height=20,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 image=self.photo,
                                 fg_color="transparent",variable=self.c_v1,
	                             onvalue=1,offvalue=0,
                                 command=self.show).place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)
    def submitbutton_event(self):
        print("button pressed")
        username=self.entry.get()
        password=self.entry2.get()
        print("Username : ",username ,"\nPassword : ",password)
    def show(self):
        if(self.c_v1.get()==1):
            self.entry2.config(show='')
        else:
            self.entry2.config(show='*')     

app = App()
app.mainloop()
