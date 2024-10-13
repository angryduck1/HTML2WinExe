from bs4 import BeautifulSoup

class EditHtmlElements:
    def __init__(self, html_content):
        self.html_content = html_content
        
    def delete_elements(self):
        soup = BeautifulSoup(self.html_content, "html.parser")
        soup.title.decompose()
        return str(soup)