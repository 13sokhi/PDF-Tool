from PDFReader import PDFReader
from PDFWriter import PDFWriter
import os

class PDFMerger:
    def __init__(self):
        self.pages = list([])

    def add_pdf(self, path):
        reader = PDFReader()
        reader.read_pdf(path)
        self.pages.extend(reader.get_pages())

    def merge_pdfs(self, output_path: str, file_name: str):
        writer = PDFWriter()
        writer.add_pages(self.pages)
        writer.write_pdf(output_path=output_path, file_name=file_name)

    def clear_pdf_paths(self):
        self.pdf_paths = list([])