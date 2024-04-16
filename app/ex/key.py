import customtkinter

def on_key_press(event):
  # Get the pressed key details from the event object
  key = event.keysym  # Use event.char for printable characters

  # Check for specific keys or perform actions based on the key
  if key == "Escape":
    print("Escape key pressed!")
  else:
    print("You pressed:", key)

# Create a CustomTkinter app
app = customtkinter.CTk()

# Create a CTkEntry widget (or any other CustomTkinter widget)
entry = customtkinter.CTkEntry(master=app)

# Bind any key press to the on_key_press function
entry.bind("<KeyPress>", on_key_press)

# Add the entry widget to the app
entry.pack(pady=20, padx=20)

# Start the main event loop
app.mainloop()
