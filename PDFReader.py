from PyPDF2 import PdfReader
import os

class PDFReader:
    def __init__(self):
        self.pages = list([])

    def read_pdf(self, path, password=None):
        if not os.path.exists(path):
            raise Exception(f"{path} does NOT exist!")
        elif not os.path.isfile(path):
            raise Exception(f"{path} is not a FILE!")
        elif not str(path).endswith('.pdf'):
            raise Exception(f"{path} is NOT a PDF!")

        reader = PdfReader(path)
        if reader.is_encrypted:
            reader.decrypt(password)
        self.pages = reader.pages

    def get_total_pages(self):
        return len(self.pages)

    def get_pages(self):
        return self.pages

    def clear_pages(self):
        self.pages = list([])
