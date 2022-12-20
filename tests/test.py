import tkinter
import customtkinter

check_var = tkinter.StringVar("on")

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

checkbox = customtkinter.CTkCheckBox(master=root_tk, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(padx=20, pady=10)