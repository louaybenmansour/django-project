import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")
        
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=10)
        
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)
        
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=10)
        
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)
        
        self.btn_login = tk.Button(root, text="Login", command=self.check_credentials)
        self.btn_login.pack(pady=20)

    def check_credentials(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username == "louay" and password == "louay123":
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()  # Close the login window
            import main  # Import the main application
            main.run()  # Call the run function in main.py
        else:
            messagebox.showerror("Error", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()