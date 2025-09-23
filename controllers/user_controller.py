from pyexpat.errors import messages

from views.login_view import LoginView
from views.register_view import RegisterView


class UserController:
    def __init__(self, model):
        self.model = model
        self.login_view = None
        self.register_view = None

    def start(self):
        self.login_view = LoginView(self)
        self.login_view.mainloop()

    def show_register_window(self):
        if self.register_view is None or not self.register_view.winfo_exists():
            self.register_view = RegisterView(self)
        self.register_view.lift()

    def handle_register(self, username, password, firstname, lastname, window):
        if not all([username, password, firstname, lastname]):
            print("Campos Vacíos", "Todos los campos son obligatorios.")
            return

        if self.model.create_user(username, password, firstname, lastname):
            print("Éxito", "Usuario registrado correctamente. Ahora puedes iniciar sesión.")
            window.destroy()