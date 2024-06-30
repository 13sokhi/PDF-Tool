from PDFWriter import PDFWriter
from PDFReader import PDFReader
from PDFMerger import PDFMerger
from PDFSplitter import PDFSplitter
from PDFWatermarker import PDFWatermarker
from PDFCompressor import PDFCompressor
from PDFEncrypter import PDFEncrypter
from PDFDecrypter import PDFDecrypter
from PDFToImage import PDFToImage
from ImageToPDF import ImageToPDF
from PDFRotator import PDFRotator


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


# Test3: Splitting PDF by Range
# pdf_splitter = PDFSplitter()
# pdf_splitter.read_pdf('C:\\Users\\asus\\Desktop\\New folder\\out.pdf')
# pdf_splitter.split_by_range(first_page=1, last_page=1, output_path='C:\\Users\\asus\\Desktop\\New folder', file_name='split2')


# Test4: Splitting PDF by pages
# pdf_splitter = PDFSplitter()
# pdf_splitter.read_pdf('C:\\Users\\asus\\Desktop\\New folder\\out.pdf')
# pdf_splitter.split_by_pages('C:\\Users\\asus\\Desktop\\New folder', 'split3', 1, 4, 5)


# Test5: Watermarking a PDF
# pdf_watermarker = PDFWatermarker()
# pdf_watermarker.set_watermark('C:\\Users\\asus\\Desktop\\New folder\\watermark.pdf')
# pdf_watermarker.read_pdf('C:\\Users\\asus\\Desktop\\New folder\\split3.pdf')
# pdf_watermarker.add_watermark_to_pdf()
# pdf_watermarker.create_watermarked_pdf(output_path='C:\\Users\\asus\\Desktop\\New folder', file_name='watermarked')


# Test6: compressing a PDF
# pdf_compressor = PDFCompressor()
# pdf_compressor.add_pdf('C:\\Users\\asus\\Desktop\\New folder\\img.pdf')
# pdf_compressor.compress_pdf()
# pdf_compressor.create_compressed_pdf(output_path='C:\\Users\\asus\\Desktop\\New folder', file_name='img compressed')


# Test7: Encrypting a PDF
# pdf_encrypter = PDFEncrypter()
# pdf_encrypter.read_pdf('C:\\Users\\asus\\Desktop\\New folder\\compressed.pdf')
# pdf_encrypter.create_encrypted_pdf(output_path='C:\\Users\\asus\\Desktop\\New folder', file_name='encrypted', password='1234')


# Test8: Decrypting a PDF
# implement handling for: FileNotDecryptedError in actual program
# pdf_decrypter = PDFDecrypter()
# pdf_decrypter.read_pdf('C:\\Users\\asus\\Desktop\\New folder\\encrypted.pdf', password='1234')
# pdf_decrypter.create_decrypted_pdf(output_path='C:\\Users\\asus\\Desktop\\New folder', file_name='decrypted2')


# Test9: converting PDF to images
# image_maker = PDFToImage()
# image_maker.convert_to_images(path='C:\\Users\\asus\\Desktop\\New folder\\sample.pdf', output_path='C:\\Users\\asus\\Desktop\\New folder\\images 2')


# Test10: converting images to PDF
# img_to_pdf = ImageToPDF()
# img_to_pdf.add_all_directory_images(path='C:\\Users\\asus\\Desktop\\New folder\\images')
# img_to_pdf.create_pdf(output_path='C:\\Users\\asus\\Desktop\\New folder', file_name='img2')


# Test11: rotate a PDF (rotate all pages)
# pdf_rotator = PDFRotator()
# pdf_rotator.read_pdf('C:\\Users\\asus\\Desktop\\New folder\\out.pdf')
# pdf_rotator.rotate_pdf(90)
# pdf_rotator.create_modified_pdf(output_path='C:\\Users\\asus\\Desktop\\New folder', file_name='rot')


# Test12: rotate specific PDF pages
pdf_rotator = PDFRotator()
pdf_rotator.read_pdf('C:\\Users\\asus\\Desktop\\New folder\\out.pdf')
pdf_rotator.rotate_page(4, 90)
pdf_rotator.create_modified_pdf(output_path='C:\\Users\\asus\\Desktop\\New folder', file_name='rot')