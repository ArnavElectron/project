import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Brain error")

label = customtkinter.CTkLabel(master=app,
                               text="error 404 Brain not found",
                               width=120,
                               height=25,
                               
                               corner_radius=8)
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
app.mainloop()