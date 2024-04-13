import customtkinter as ctk

window = ctk.CTk()

window.geometry("800x600")

f2 = ctk.CTkFrame(window, fg_color="green")
f1 = ctk.CTkFrame(window, fg_color="red")

f1.grid(row=0, column=0, )
f2.grid(row=0, column=0, )

f2.tkraise()

window.mainloop()