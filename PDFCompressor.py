from PDFReader import PDFReader
from PDFWriter import PDFWriter

class PDFCompressor:
    def __init__(self):
        self.actual_pages: list = list([])
        self.compressed_pages: list = list([])

    def add_pdf(self, path: str):
        reader = PDFReader()
        reader.read_pdf(path)
        self.actual_pages = reader.get_pages()

    def compress_pdf(self):
        self.compressed_pages = list([])
        for page in self.actual_pages:
            page.compress_content_streams()
            self.compressed_pages.append(page)

    def create_compressed_pdf(self, output_path: str, file_name: str):
        writer = PDFWriter()
        writer.add_pages(self.compressed_pages)
        writer.write_pdf(output_path=output_path, file_name=file_name)

    def clear_pages(self):
        self.actual_pages = list([])
        self.compressed_pages = list([])