import tkinter as tk

class RegisterView(tk.Toplevel):
    def __init__(self, user_controller):
        super().__init__()
        self.user_controller = user_controller
        self.title("Registro de usuario")
        self.geometry("400x400")
        self.resizable(width=False, height=False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.username_label = tk.Label(self, text="Usuario:")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password")
        self.password_entry = tk.Entry(self, show="*")
        self.firstname_label = tk.Label(self, text="First Name:")
        self.firstname_entry = tk.Entry(self)
        self.lastname_label = tk.Label(self, text="Last Name:")
        self.lastname_entry = tk.Entry(self)
        self.register_button = tk.Button(self, text="Registrar usuario", command=self.register_button_clicked)

        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.firstname_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.firstname_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.lastname_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.register_button.grid(row=4, column=0, columnspan=2, pady=5)

    def register_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        self.user_controller.handle_register(username, password, firstname, lastname, self)