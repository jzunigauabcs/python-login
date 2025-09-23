from views.login_view import LoginView
from views.register_view import RegisterView


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