from PDFWriter import PDFWriter
from PDFReader import PDFReader
from PDFMerger import PDFMerger


pdf_path = "C:\\Users\\asus\\Desktop\\New folder\\out.pdf"

# Test1 : reading and writing a PDF with different name
# reader = PDFReader()
# reader.read_pdf(pdf_path)
# pages = reader.get_pages()
#
# writer = PDFWriter()
# writer.add_pages(pages)
# writer.write_pdf("C:\\Users\\asus\\Desktop\\New folder", "out2")


# Test2 : Merging 2 PDFs
# pdf_merger = PDFMerger()
# pdf_merger.add_pdf('C:\\Users\\asus\\Desktop\\New folder\\out.pdf')
# pdf_merger.add_pdf('C:\\Users\\asus\\Desktop\\New folder\\sample.pdf')
# pdf_merger.merge_pdfs('C:\\Users\\asus\\Desktop\\New folder', 'mergerd')