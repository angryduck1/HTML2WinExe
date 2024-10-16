from bs4 import BeautifulSoup

class EditHtmlElements:
    def __init__(self, html_content):
        self.html_content = html_content
        
    def delete_elements(self):
        soup = BeautifulSoup(self.html_content, "html.parser")
        soup.title.decompose()
        return str(soup)
    
    def get_background_color(self):
        soup = BeautifulSoup(self.html_content, "html.parser")
        body = soup.find('body')
        if body and 'style' in body.attrs:
            style = body['style']
            if 'background-color' in style:
                color_value = style.split("background-color:")[1].strip().rstrip(";")
                return color_value
        else:
            print("Background color is not found")
