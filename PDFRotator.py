from PDFReader import PDFReader
from PDFWriter import PDFWriter


class PDFRotator:
    def __init__(self):
        self.pages: list = list([])

    def read_pdf(self, path: str):
        reader = PDFReader()
        reader.read_pdf(path)
        self.pages = reader.get_pages()

    def rotate_page(self, page_num: int, rotation: int):
        if rotation % 90 != 0:
            raise Exception("Rotate only by a factor of 90!")
        elif page_num < 0:
            raise Exception("Invalid page number!")
        elif page_num > len(self.pages):
            raise Exception(f"Page {page_num} not in PDF!")

        self.pages[page_num - 1].rotate(rotation)

    def rotate_pdf(self, rotation: int):
        for i in range(len(self.pages)):
            self.rotate_page(i+1, rotation)

        # if rotation % 90 != 0:
        #     raise Exception("Rotate only by a factor of 90!")
        # for i in range(len(self.pages)):
        #     self.pages[i].rotate(90)

    def create_modified_pdf(self, output_path: str, file_name: str):
        writer = PDFWriter()
        writer.add_pages(self.pages)
        writer.write_pdf(output_path=output_path, file_name=file_name)