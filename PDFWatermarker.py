from PyPDF2 import PageObject
from PDFReader import PDFReader
from PDFWriter import PDFWriter

class PDFWatermarker:
    def __init__(self):
        self.watermark_pdf_path: str = ''
        self.actual_pages: list = list([])
        self.watermarked_pages: list = list([])

    #     This method takes in path of PDF of image to be used as a watermark
    def set_watermark(self, path: str):
        self.watermark_pdf_path = path

    def read_pdf(self, path: str):
        reader = PDFReader()
        reader.read_pdf(path)
        self.actual_pages = reader.get_pages()

    def add_watermark_to_pdf(self):
        for page in self.actual_pages:
            # creating new watermark PageObject each time loop runs
            reader = PDFReader()
            reader.read_pdf(self.watermark_pdf_path)
            temp_page = reader.get_pages()[0]

            # merging and adding page to list
            temp_page.merge_page(page)
            self.watermarked_pages.append(temp_page)

    def create_watermarked_pdf(self, output_path: str, file_name: str):
        writer = PDFWriter()
        writer.add_pages(self.watermarked_pages)
        writer.write_pdf(output_path=output_path, file_name=file_name)