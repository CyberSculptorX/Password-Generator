import tkinter as tk
import secrets
import string
import os

class PasswordGeneratorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Secrets Password Generator | Cyber Sculptor X")
        self.root.configure(bg='#000000')  # Black background
        self.root.geometry("600x300+50+50")  # Set window size and position
        self.root.overrideredirect(True)  # Remove window frame
        self.root.minsize(600, 300)
        self.root.resizable(True, True)

        # Bind the Esc key to close the application
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Font settings
        font_medium = ('Arial', 12)
        font_small = ('Arial', 10)

        # Initialize variables
        self.password_length = tk.IntVar()
        self.password_length.set(16)  # Default password length

        # Create UI elements with custom styling
        self.label_length = tk.Label(self.root, text="Password Length:", fg='#00FF00', bg='#000000', font=font_medium)
        self.label_length.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.label_length_value = tk.Label(self.root, textvariable=self.password_length, fg='#00FF00', bg='#000000', font=font_medium, width=5, justify="center")
        self.label_length_value.grid(row=0, column=1, padx=5, pady=5)
        
        # Increase/Decrease buttons
        self.frame_arrows = tk.Frame(self.root, bg='#000000')
        self.frame_arrows.grid(row=0, column=2, padx=5, pady=5)
        
        self.btn_up = tk.Button(self.frame_arrows, text="▲", command=self.increase_length, fg='#000000', bg='#00FF00', font=font_small)
        self.btn_up.grid(row=0, column=0, padx=5)
        
        self.btn_down = tk.Button(self.frame_arrows, text="▼", command=self.decrease_length, fg='#000000', bg='#00FF00', font=font_small)
        self.btn_down.grid(row=0, column=1, padx=5)

        self.btn_generate = tk.Button(self.root, text="Generate Password", command=self.generate_password, fg='#000000', bg='#00FF00', font=font_medium)
        self.btn_generate.grid(row=1, columnspan=3, pady=5)
        
        self.label_generated_password = tk.Label(self.root, text="Generated Password:", fg='#00FF00', bg='#000000', font=font_medium)
        self.label_generated_password.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.generated_password = tk.Text(self.root, height=3, width=40, wrap="word", fg='#00FF00', bg='#000000', state='disabled', font=font_medium)
        self.generated_password.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
        self.generated_password.tag_configure("center", justify='center')
        
        self.btn_clear = tk.Button(self.root, text="Clear", command=self.clear_screen, fg='#000000', bg='#00FF00', font=font_medium)
        self.btn_clear.grid(row=3, column=0, pady=5)
        
        self.btn_copy = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, fg='#000000', bg='#00FF00', font=font_medium)
        self.btn_copy.grid(row=3, column=1, pady=5)
        
        self.btn_download = tk.Button(self.root, text="Download", command=self.download_password, fg='#000000', bg='#00FF00', font=font_medium)
        self.btn_download.grid(row=3, column=2, pady=5)
        
        self.message_label = tk.Label(self.root, text="", fg='#00FF00', bg='#000000', font=font_medium)
        self.message_label.grid(row=4, columnspan=3, pady=5)

        # Set weights to make the grid cells expand
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

    def increase_length(self):
        current_length = self.password_length.get()
        self.password_length.set(current_length + 1)

    def decrease_length(self):
        current_length = self.password_length.get()
        if current_length > 16:
            self.password_length.set(current_length - 1)

    def generate_password(self):
        try:
            length = self.password_length.get()
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for _ in range(length))
            self.generated_password.config(state='normal')
            self.generated_password.delete(1.0, tk.END)  # Clear previous content
            self.generated_password.insert(tk.END, password)
            self.generated_password.tag_add("center", "1.0", "end")
            self.generated_password.config(state='disabled')
        except ValueError:
            self.show_message("Error: Please enter a valid integer for password length.")

    def clear_screen(self):
        self.generated_password.config(state='normal')
        self.generated_password.delete(1.0, tk.END)
        self.generated_password.config(state='disabled')
        self.show_message("Screen cleared.")

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.generated_password.get(1.0, tk.END).strip())
        self.show_message("Password copied to clipboard.")

    def download_password(self):
        download_path = os.path.join(os.path.expanduser("~"), "Downloads", "weather_report.txt")
        with open(download_path, 'w') as file:
            file.write(self.generated_password.get(1.0, tk.END).strip())
        self.show_message("Password saved successfully in the Downloads folder.")

    def show_message(self, message):
        self.message_label.config(text=message)
        self.root.after(4000, self.clear_message)

    def clear_message(self):
        self.message_label.config(text="")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.run()
