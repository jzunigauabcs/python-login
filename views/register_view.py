import tkinter as tk

class RegisterView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Crear cuenta")
        self.geometry("400x400")
        self.resizable(False, False)

        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)
        self.firstname_label = tk.Label(self, text="First Name:")
        self.firstname_entry = tk.Entry(self)
        self.lastname_label = tk.Label(self, text="Last Name:")
        self.lastname_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Registrar", command=self.register_button_clicked)

        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.firstname_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.firstname_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.lastname_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.login_button.grid(row=4, column=0, columnspan=2, pady=10)

    def register_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        self.controller.handle_register(username, password, firstname, lastname, self)