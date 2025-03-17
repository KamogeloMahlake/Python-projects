from tkinter import Tk, Text, filedialog, Menu
import tkinter as tk
from functools import partial


class TextEditor:
    fonts = ["Arial", "Courier", "Times New Roman", "Roman", "Comic Sans"]
    font_sizes = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

    def __init__(self):
        self.current_file_path = ""
        self.current_font = "Arial"
        self.current_font_size = 12

        self.root = Tk()
        self.root.title("Untitled - Text Editor")

        self.text = Text(self.root, wrap="word")
        self.text.pack(expand=True, fill="both")

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.create_file_menu()
        self.create_format_menu()

    def run(self):
        self.root.mainloop()

    def create_file_menu(self):
        filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open...", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save as", command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)

    def create_format_menu(self):
        formatmenu = Menu(self.menu)
        self.menu.add_cascade(label="Format", menu=formatmenu)
        font_menu = Menu(formatmenu)
        formatmenu.add_cascade(label="Font", menu=font_menu)
        font_size_menu = Menu(formatmenu)
        formatmenu.add_cascade(label="Font Size", menu=font_size_menu)

        for font in self.fonts:
            font_menu.add_command(label=font, command=partial(self.set_font, font))
        for size in self.font_sizes:
            font_size_menu.add_command(
                label=str(size), command=partial(self.set_font_size, size)
            )

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.current_file_path = ""
        self.root.title("Untitled - Text Editor")

    def update_title(self, new_title):
        self.root.title(f"{new_title.split('/')[-1].split('.')[0]} - Text Editor")

    def save_file(self):
        if self.current_file_path:
            try:
                with open(self.current_file_path, "w") as file:
                    file.write(self.text.get(1.0, tk.END))
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            self.save_file_as()

    def open_file(self):
        path = filedialog.askopenfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if path:
            try:
                with open(path, "r") as file:
                    content = file.read()
                    self.text.delete(1.0, tk.END)
                    self.text.insert(tk.INSERT, content)
                    self.update_title(path)
                    self.current_file_path = path
            except Exception as e:
                print(f"Error opening file: {e}")

    def save_file_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if path:
            try:
                with open(path, "w") as file:
                    file.write(self.text.get(1.0, tk.END))
                    self.update_title(path)
                    self.current_file_path = path
            except Exception as e:
                print(f"Error saving file as: {e}")

    def set_font(self, font):
        self.text.config(font=(font, self.current_font_size))
        self.current_font = font

    def set_font_size(self, size):
        self.text.config(font=(self.current_font, size))
        self.current_font_size = size


if __name__ == "__main__":
    text_editor = TextEditor()
    text_editor.run()