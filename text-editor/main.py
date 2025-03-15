from tkinter import (
    Tk,
    Text,
    filedialog,
    Menu,
)
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

        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.__new)
        self.filemenu.add_command(label="Open...", command=self.__open)
        self.filemenu.add_command(label="Save", command=self.__save)
        self.filemenu.add_command(label="Save as", command=self.__save_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)

        self.formatmenu = Menu(self.menu)
        self.menu.add_cascade(label="Format", menu=self.formatmenu)
        self.font = Menu(self.formatmenu)
        self.formatmenu.add_cascade(label="Font", menu=self.font)
        self.font_size = Menu(self.formatmenu)
        self.formatmenu.add_cascade(label="Font Size", menu=self.font_size)
        

        for font in self.fonts:
            self.font.add_command(label=font, command=partial(self.__font, font))
        for size in self.font_sizes:
            self.font_size.add_command(
                label=str(size), command=partial(self.__font_size, size)
            )

    def run(self):
        self.root.mainloop()

    def __new(self):
        self.text.delete(1.0, tk.END)
        self.current_file_path = ""
        self.root.title("Untitled - Text Editor")

    def __update_title(self, new_title):
        self.root.title(f"{new_title.split('/')[-1].split('.')[0]} - Text Editor")

    def __save(self):
        if self.current_file_path:
            with open(self.current_file_path, "w") as file:
                file.write(self.text.get(1.0, tk.END))
        else:
            self.__save_as()

    def __open(self):
        path = filedialog.askopenfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        with open(path, "r") as file:
            content = file.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.INSERT, content)
            self.__update_title(path)
            self.current_file_path = path

    def __save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if path:
            with open(path, "w") as file:
                file.write(self.text.get(1.0, tk.END))
                self.__update_title(path)
                self.current_file_path = path

    def __font(self, font):
        self.text.config(font=(font, self.current_font_size))
        self.current_font = font

    def __font_size(self, size):
        self.text.config(font=(self.current_font, size))
        self.current_font_size = size


if __name__ == "__main__":
    text_editor = TextEditor()
    text_editor.run()
