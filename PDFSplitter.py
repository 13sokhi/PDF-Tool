from PDFReader import PDFReader
from PDFWriter import PDFWriter
import os

class PDFSplitter:
    def __init__(self):
        self.pages = list([])

    def read_pdf(self, path: str):
        reader = PDFReader()
        reader.read_pdf(path)
        self.pages = reader.get_pages()

    def split_by_range(self, output_path: str, file_name: str, first_page: int, last_page: int):
        if first_page<1 or last_page<1:
            raise Exception("Invalid range selection!")
        elif first_page>last_page:
            raise Exception("Bad Range selection!")
        elif last_page>len(self.pages):
            raise Exception(f"PDF has only {len(self.pages)} pages!")

        self.pages = self.pages[first_page - 1 : last_page] # index of stored page is 1 less than requested page
        writer = PDFWriter()
        writer.add_pages(self.pages)
        writer.write_pdf(output_path=output_path, file_name=file_name)

    # make a new PDF having specified pages in specified order
    # pages: list = hold order of pages to be added in new PDF
    def split_by_pages(self, output_path: str, file_name: str, pages: list):
        if min(pages) < 1:
            raise Exception(f"Page {min(pages)} is invalid!")
        if max(pages) > len(self.pages):
            raise Exception(f"Page {max(pages)} does NOT exist in PDF!")

        temp: list = list([])
        for page_num in pages:
            temp.append(self.pages[page_num - 1])
        writer = PDFWriter()
        writer.add_pages(temp)
        writer.write_pdf(output_path=output_path, file_name=file_name)