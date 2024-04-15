import customtkinter as ctk


app = ctk.CTk()

button = ctk.CTkButton(app, text="CLICK", command=print)
button.pack()

app.mainloop()