import customtkinter
import tkinter.messagebox
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inventory Management System")
        self.geometry(f"{1000}x{700}")
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
                                 fg_color="white",
                                 hover_color='#bcbcbc',
                                 text_color="black",
                                 command=self.submitbutton_event)
        self.submitbutton.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        self.photo1= customtkinter.CTkImage(Image.open("frontend/images/showpassnew.png"),size=(10, 10))
        self.showbutton = customtkinter.CTkButton(self,
                                 width=20,
                                 height=20,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 image=self.photo1,
                                 fg_color="white",
                                 hover_color='#bcbcbc',
                                 command=self.show,
                                 ).place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    def submitbutton_event(self):
        print("button pressed")
        username=self.entry.get()
        password=self.entry2.get()
        print("Username : ",username ,"\nPassword : ",password)
    def show(self):
        if(c==1):
            self.entry2.configure(show="")
            c=+1
        if(c!=1):
            self.entry2.configure(show="")
            c=1
        print(c)

        
app = App()
app.mainloop()
