import tkinter as tk

class LoginView(tk.Tk):
    def __init__(self, user_controller):
        super().__init__()
        self.user_controller = user_controller
        self.title("Iniciar sesión")
        self.geometry("400x230")
        self.resizable(width=False, height=False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.username_label = tk.Label(self, text="Usuario:")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Iniciar sesión",command=self.login_button_clicked)
        self.register_button = tk.Button(self, text="Registrar usuario", command=self.register_button_clicked)

        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.login_button.grid(row=2, column=0, columnspan=2, pady=5)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=5)

    def login_button_clicked(self):
        print("Iniciar sesión")

    def register_button_clicked(self):
        self.user_controller.show_register_window()