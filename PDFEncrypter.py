from PDFReader import PDFReader
from PDFWriter import PDFWriter


class PDFEncrypter:
    def __init__(self):
        self.pages: list = list([])

    def read_pdf(self, path: str):
        reader = PDFReader()
        reader.read_pdf(path)
        self.pages = reader.get_pages()

    def create_encrypted_pdf(self, output_path: str, file_name: str, password: str):
        writer = PDFWriter()
        writer.add_pages(self.pages)
        writer.write_pdf(output_path=output_path, file_name=file_name, protected=True, password=password)