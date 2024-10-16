from tkinter import *
from tkhtmlview import HTMLLabel
from tkinter import messagebox
from bs4 import BeautifulSoup
from Utilites.EditHtmlElements import EditHtmlElements

class HTML:
    def __init__(self):
        self.html_content = ""

    def read_html(self):
        try:
            with open("your_file.html", "r", encoding="utf-8") as file:
                self.html_content = file.read()
        except FileNotFoundError:
            messagebox.showerror("Error", "File is not Found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_title(self):
        soup = BeautifulSoup(self.html_content, "html.parser")
        title = soup.title.string
        return title
    
    def display_html(self):
        self.read_html()
        modified_html = EditHtmlElements(self.html_content).delete_elements()

        root = Tk()
        root.title(self.get_title())
        root.geometry("400x400")

        html_tk = HTMLLabel(root, html=modified_html, background=EditHtmlElements(self.html_content).get_background_color())
        html_tk.pack(padx=0, pady=0, expand=True, fill=BOTH)

        root.mainloop()