from PDFReader import PDFReader
from PDFWriter import PDFWriter
import os

class PDFSplitter:
    def __init__(self):
        self.pages = list([])

    def read_pdf(self, path: str):
        reader = PDFReader()
        reader.read_pdf(path)
        self.pages = list([])

    def split_by_range(self, output_path: str, file_name: str, first_page: int, last_page: int):
        self.pages = self.pages[first_page - 1 : last_page] # index of stored page is 1 less than requested page
        writer = PDFWriter()
        writer.add_pages(self.pages)
        writer.write_pdf(output_path=output_path, file_name=file_name)

    def split_by_pages(self, output_path: str, file_name: str, *args: set):
        temp: list = list([])
        for i in range(len(self.pages)):
            if i+1 in args:
                temp.append(self.pages[i]) # adding pages whose index+1 corresponds to requested page
        writer = PDFWriter()
        writer.add_pages(self.pages)
        writer.write_pdf(output_path=output_path, file_name=file_name)