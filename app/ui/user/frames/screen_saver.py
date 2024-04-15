from typing import Any, Tuple
import customtkinter as ctk
class ScreenSaver(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.screen_wairt=ctk.CTkLabel(self,text="waiting for admin to\n start the next round",font=('times new roman',80))
    def show(self):
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.screen_wairt.grid(row=0,column=0,padx=300,pady=20,sticky='we')
        self.grid(row=0,column=0,padx=20,pady=20,sticky='nswe')
        
    def hide(self):
        self.grid_forget()