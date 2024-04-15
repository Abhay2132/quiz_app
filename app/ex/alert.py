import customtkinter as ctkt

def create_alert_dialog(title, message):
  """Creates and displays a custom alert dialog.

  Args:
      title: The title of the dialog window.
      message: The message to display in the dialog body.
  """
  # Create the main window for the alert dialog
  alert_window = ctkt.CTkToplevel()
  alert_window.geometry("400x200")
  alert_window.title(title)

  # Create a frame to hold the message and buttons
  message_frame = ctkt.CTkFrame(master=alert_window,)
  message_frame.pack(pady=20)

  # Display the message
  message_label = ctkt.CTkLabel(master=message_frame, justify=ctkt.LEFT, text=message)
  message_label.pack()

  # Add a button to close the dialog
  button_frame = ctkt.CTkFrame(master=alert_window)
  button_frame.pack(pady=10)

  close_button = ctkt.CTkButton(master=button_frame, text="Close", command=lambda: alert_window.destroy())
  close_button.pack(pady=10)

  # Run the main loop for the alert dialog window
  alert_window.mainloop()

# Example usage
title = "Alert!"
message = "This is a custom alert dialog."
create_alert_dialog(title, message)
