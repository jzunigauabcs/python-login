import tkinter as tk

class RegisterView(tk.Toplevel):
    def __init__(self, user_controller):
        super().__init__()
        self.user_controller = user_controller
        self.title("Registro de usuario")
        self.geometry("400x230")
        self.resizable(width=False, height=False)