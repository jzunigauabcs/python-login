from _curses import window

from views.login_view import LoginView
from views.register_view import RegisterView
from tkinter import messagebox


class UserController:
    def __init__(self, user_model):
        self.user_model = user_model
        self.login_view = None
        self.register_view = None

    def run(self):
        self.login_view = LoginView(self)
        self.login_view.mainloop()

    def show_register_window(self):
        if self.register_view is None or not self.register_view.winfo_exists():
            self.register_view = RegisterView(self)
        self.register_view.lift()

    def handle_register(self, username, password, firstname, lastname, window):
        if not all([username, password, firstname, lastname]):
            messagebox.showerror("Error", "Todos los campos obligatorios")
            return

        if self.user_model.create_user(username, password, firstname, lastname):
            messagebox.showinfo("Success", "Usuario creado exitosamente")
            window.destroy()