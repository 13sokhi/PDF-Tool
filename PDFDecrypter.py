from PDFReader import PDFReader
from PDFWriter import PDFWriter


class PDFDecrypter:
    def __init__(self):
        self.pages: list = list([])

    def read_pdf(self, path: str, password: str = ''):
        reader = PDFReader()
        reader.read_pdf(path=path, password=password)
        self.pages = reader.get_pages()

    def create_decrypted_pdf(self, output_path: str, file_name: str):
        writer = PDFWriter()
        writer.add_pages(self.pages)
        writer.write_pdf(output_path=output_path, file_name=file_name)