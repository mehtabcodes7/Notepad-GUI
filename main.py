#Mehtab Codes Presents
#Notepad Using Python Tkinter

import tkinter as tk
from tkinter import filedialog, font, messagebox

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize the main window
        self.title("Mehtab's Notepad")
        self.geometry("600x400")
        self.config(bg="white")

        # Text area
        self.text_area = tk.Text(self, wrap='word', font=("Arial", 12), bg="white", fg="black")
        self.text_area.pack(expand=True, fill='both')

        # Font size variable
        self.font_size = tk.IntVar(value=12)

        # Create a menu
        self.create_menu()

        # Theme variable
        self.is_dark_theme = False

    def create_menu(self):
        menu_bar = tk.Menu(self)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Increase Font Size", command=self.increase_font_size)
        edit_menu.add_command(label="Decrease Font Size", command=self.decrease_font_size)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Theme menu
        theme_menu = tk.Menu(menu_bar, tearoff=0)
        theme_menu.add_command(label="Toggle Theme", command=self.toggle_theme)
        menu_bar.add_cascade(label="Theme", menu=theme_menu)

        self.config(menu=menu_bar)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get("1.0", tk.END))
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def increase_font_size(self):
        current_size = self.font_size.get()
        self.font_size.set(current_size + 2)
        new_font = font.Font(size=self.font_size.get())
        self.text_area.configure(font=new_font)

    def decrease_font_size(self):
        current_size = self.font_size.get()
        if current_size > 6:  # Set a minimum font size
            self.font_size.set(current_size - 2)
            new_font = font.Font(size=self.font_size.get())
            self.text_area.configure(font=new_font)

    def toggle_theme(self):
        if self.is_dark_theme:
            self.config(bg="white")
            self.text_area.config(bg="white", fg="black")
            self.is_dark_theme = False
        else:
            self.config(bg="black")
            self.text_area.config(bg="black", fg="white")
            self.is_dark_theme = True

if __name__ == "__main__":
    notepad = Notepad()
    notepad.mainloop()
