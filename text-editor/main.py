from tkinter import Tk, Text, filedialog, Menu
import tkinter as tk


class TextEditor:
    def __init__(self):
        self.current_file_path = ""
        self.root = Tk()
        self.root.title("Untitled - Text Editor")

        self.text = Text(self.root, wrap="word")
        self.text.pack(expand=True, fill="both")

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open...", command=self.__open)
        self.filemenu.add_command(label="Save", command=self.__save)
        self.filemenu.add_command(label="Save as", command=self.__save_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)

        self.formatmenu = Menu(self.menu)
        self.menu.add_cascade(label="Format", menu=self.formatmenu)
        self.font = Menu(self.formatmenu)
        self.formatmenu.add_cascade(label="Font", menu=self.font)
        self.font.add_command(label="Courier", command=self.__font_courier)
        self.font.add_command(label="Helvetica", command=self.__font_helvetica)

    def run(self):
        self.root.mainloop()

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

        path = filedialog.asksaveasfile(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if path:
            path.write(self.text.get(1.0, tk.END))
            path.close()
            self.__update_title(path)
            self.current_file_path = path

        else:
            self.__save_as()

        return

    def __font_courier(self):
        self.text.config(font="Courier")

    def __font_helvetica(self):
        self.text.config(font="Helvetica")
    
if __name__ == "__main__":
    text_editor = TextEditor()
    text_editor.run()
