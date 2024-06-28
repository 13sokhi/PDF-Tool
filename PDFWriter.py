from PyPDF2 import PdfWriter
import os

class PDFWriter:
    def __init__(self):
        self.pages = list([])

    def add_pages(self, pages: list):
        self.pages.extend(pages)

    def write_pdf(self, output_path: str, file_name: str, protected=False, password=None):
        save_path = os.path.join(output_path, f"{file_name}.pdf")
        print(save_path)
        if not os.path.exists(output_path):
            raise Exception(f"{output_path} does NOT exist!")
        elif not os.path.isdir(output_path):
            raise Exception(f"{output_path} is not a DIRECTORY!")
        elif os.path.exists(save_path):
            raise Exception(f"{save_path} already exists!")

        writer = PdfWriter()
        for page in self.pages:
            writer.add_page(page)
        if protected:
            writer.encrypt(password)
        writer.write(save_path)

    def clear_pages(self):
        self.pages = list([])