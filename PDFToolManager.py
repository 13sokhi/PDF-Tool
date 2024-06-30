from PDFMerger import PDFMerger
from PDFSplitter import PDFSplitter
from PDFWatermarker import PDFWatermarker
from PDFCompressor import PDFCompressor
from PDFEncrypter import PDFEncrypter
from PDFDecrypter import PDFDecrypter
from PDFToImage import PDFToImage
from ImageToPDF import ImageToPDF
from PDFRotator import PDFRotator
import os
from PyPDF2.errors import FileNotDecryptedError


def merge_pdfs():
    pdf_merger = PDFMerger()
    i = 1
    pdf_paths: list = list([])
    while True:
        path = input("\033[0m" + f'PDF {i} path (0 to cancel, 1 to Merge): ')
        if path == '0': # to cancel merging PDFs
            return
        elif path == '1' and i == 1: # when user selects to MERGE PDFs but no PDFs are selected
            print("\033[31m" + 'No PDF selected to Merge!\n')
        elif path == '1': # to merge selected PDFs
            output_path = input("Path to save merged PDF (folder): ")
            file_name = input('PDF name (without ".pdf"): ')
            pdf_merger.merge_pdfs(output_path=output_path, file_name=file_name)

            print("\n\033[32m" + f'{i - 1} PDF:')
            for pdf_path in pdf_paths:
                print("\033[32m" + pdf_path)
            print("\033[32m" + f'merged at {os.path.join(output_path, f"{file_name}.pdf")}')
            return
        else:
            pdf_merger.add_pdf(path)
            pdf_paths.append(path)
            i += 1


def split_pdf():
    while True:
        print("\n\033[0m" + 'Press 0 to Exit')
        print('Press 1 to split by Range')
        print('Press 2 to split by pages')
        method = int(input('Selection: '))
        match method:
            case 0:
                break
            case 1:
                split_pdf_by_range()
                return
            case 2:
                split_pdf_by_pages()
                return
            case _:
                print("\033[31m" + 'Invalid Selection!')

def split_pdf_by_range():
    pdf_splitter = PDFSplitter()
    pdf_path = input('Path of PDF to split: ')
    pdf_splitter.read_pdf(pdf_path)

    first_page = int(input('Start page number: '))
    last_page = int(input('Last page number: '))
    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')
    pdf_splitter.split_by_range(output_path=output_path, file_name=file_name, first_page=first_page, last_page=last_page)
    print("\n\033[32m" + f'Splitted PDF created at: {os.path.join(output_path, f"{file_name}.pdf")}')

def split_pdf_by_pages():
    pdf_splitter = PDFSplitter()
    pdf_path = input('Path of PDF to split: ')
    pdf_splitter.read_pdf(pdf_path)

    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')
    pages: list = list([])
    i = 1
    while True:
        page_num = int(input("\033[0m" + f'Enter page {i} to add (-1 to Cancel, 0 to Split): '))
        if page_num == -1:
            return
        elif page_num == 0 and i == 1:
            print("\n\033[31m" + 'No pages selected!\n')
        elif page_num == 0:
            pdf_splitter.split_by_pages(output_path=output_path, file_name=file_name, pages=pages)
            print("\n\033[32m" + f'Split PDF created at: {os.path.join(output_path, f"{file_name}.pdf")}')
            return
        else:
            pages.append(page_num)
            i += 1

def watermark_pdf():
    watermark_path = input('Path to watermark (ONLY PDF): ')
    pdf_path = input('Path to PDF to watermark: ')
    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')

    pdf_watermarker = PDFWatermarker()
    pdf_watermarker.set_watermark(watermark_path)
    pdf_watermarker.read_pdf(pdf_path)
    pdf_watermarker.add_watermark_to_pdf()
    pdf_watermarker.create_watermarked_pdf(output_path=output_path, file_name=file_name)

    print("\n\033[32m" + f'Watermarked PDF created at: {os.path.join(output_path, f"{file_name}.pdf")}')

def compress_pdf():
    pdf_path = input('Path to PDF to compress: ')
    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')

    pdf_compressor = PDFCompressor()
    pdf_compressor.add_pdf(pdf_path)
    pdf_compressor.compress_pdf()
    pdf_compressor.create_compressed_pdf(output_path=output_path, file_name=file_name)

    print("\n\033[32m" + f'Compressed PDF created at: {os.path.join(output_path, f"{file_name}.pdf")}')

def encrypt_pdf():
    pdf_path = input('Path to PDF to encrypt: ')
    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')
    password = input('PDF password to set: ')

    pdf_encrypter = PDFEncrypter()
    pdf_encrypter.read_pdf(pdf_path)
    pdf_encrypter.create_encrypted_pdf(output_path=output_path, file_name=file_name, password=password)

    print("\n\033[32m" + f'Encrypted PDF created at: {os.path.join(output_path, f"{file_name}.pdf")}')

def decrypt_pdf():
    pdf_path = input('Path to PDF to decrypt: ')
    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')
    password = input('Current PDF password : ')

    pdf_decrypter = PDFDecrypter()
    pdf_decrypter.read_pdf(path=pdf_path, password=password)
    pdf_decrypter.create_decrypted_pdf(output_path=output_path, file_name=file_name)

    print("\n\033[32m" + f'Decrypted PDF created at: {os.path.join(output_path, f"{file_name}.pdf")}')

def convert_pdf_to_images():
    pdf_path = input('Path to PDF to convert to images: ')
    output_path = input('Path to save (folder): ')

    converter = PDFToImage()
    converter.convert_to_images(path=pdf_path, output_path=output_path)

    print("\n\033[32m" + f'PDF {pdf_path} converted to images at: {output_path}')

def convert_images_to_pdf():
    while True:
        print("\n\033[0m" + 'Press 0 to Exit')
        print('Press 1 to select all images in a directory: ')
        print('Press 2 to select individual images: ')

        method = int(input())
        match method:
            case 0:
                break
            case 1:
                convert_all_directory_images_to_pdf()
                break
            case 2:
                convert_specific_images_to_pdf()
                break
            case _:
                print("\033[31m" + 'Invalid Selection!')

def convert_all_directory_images_to_pdf():
    folder_path = input('Path of folder with images: ')
    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')
    converter = ImageToPDF()
    images = converter.add_all_directory_images(folder_path)
    converter.create_pdf(output_path=output_path, file_name=file_name)

    print("\n\033[32m" + f'{len(images)} Images:')
    for img in images:
        print('\t' + img)
    print(f'combined as PDF at: {os.path.join(output_path, f"{file_name}.pdf")}')

def convert_specific_images_to_pdf():
    converter = ImageToPDF()
    img_list: list = list([])
    i = 1
    while True:
        img_path = input("\033[0m" + f'Path of Image {i} to add (0 to cancel, 1 to Combine): ')
        if img_path == '0':
            return
        elif img_path == '1' and i == 1:
            print("\n\033[31m" + 'No images selected to combine\n')
        elif img_path == '1':
            output_path = input('Path to save (folder): ')
            file_name = input('PDF name (without ".pdf"): ')
            converter.create_pdf(output_path=output_path, file_name=file_name)

            print("\n\033[32m" + f' {i - 1} Images:')
            for img in img_list:
                print('\t' + img)
            print(f'combined as PDF at: {os.path.join(output_path, f"{file_name}.pdf")}')
            return
        else:
            converter.add_image(img_path)
            img_list.append(img_path)
            i += 1


def rotate_pdf():
    while True:
        print("\n\033[0m" + 'Press 0 to Exit')
        print('Press 1 to Rotate all PDF pages')
        print('Press 2 to Rotate selected pages')
        method = int(input('Selection: '))
        match method:
            case 0:
                break
            case 1:
                rotate_all_pages()
                return
            case 2:
                rotate_selected_pages()
                return
            case _:
                print("\033[31m" + 'Invalid input!')

def rotate_all_pages():
    pdf_path = input('Path of PDF to rotate: ')
    rotation = int(input('Rotation (90, 180, 270): '))
    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')

    pdf_rotator = PDFRotator()
    pdf_rotator.read_pdf(pdf_path)
    pdf_rotator.rotate_pdf(rotation=rotation)
    pdf_rotator.create_modified_pdf(output_path=output_path, file_name=file_name)

    print("\n\033[32m" + f'PDF {pdf_path} rotated by {90} deg at: {os.path.join(output_path, f"{file_name}.pdf")}')

def rotate_selected_pages():
    pdf_path = input('Path of PDF to rotate: ')
    pdf_rotator = PDFRotator()
    pdf_rotator.read_pdf(pdf_path)
    while True:
        print("\n\033[0m" + 'Press 0 to Stop')
        print('Press 1 to select page to rotate')
        inp = int(input('Selection: '))
        match inp:
            case 0:
                break
            case 1:
                page_num = int(input('Enter page number to rotate: '))
                rotation = int(input('Enter rotation (90, 180, 270): '))
                pdf_rotator.rotate_page(page_num=page_num, rotation=rotation)
            case _:
                print("\033[31m" + 'Invalid Input!')
    output_path = input('Path to save (folder): ')
    file_name = input('PDF name (without ".pdf"): ')
    pdf_rotator.create_modified_pdf(output_path=output_path, file_name=file_name)

    print("\n\033[32m" + f'Rotated PDF created at: {os.path.join(output_path, f"{file_name}.pdf")}')

def main():
    while True:
        print("\n\033[0m" + "-"*50)
        print('-> Press 0 to Exit')
        print('-> Press 1 to Merge PDFs')
        print('-> Press 2 to Split PDF')
        print('-> Press 3 to Watermark a PDF')
        print('-> Press 4 to Compress PDF')
        print('-> Press 5 to Encrypt PDF')
        print('-> Press 6 to Decrypt PDF')
        print('-> Press 7 to convert PDF into Images')
        print('-> Press 8 to convert Images into PDF')
        print('-> Press 9 to Rotate a PDF')

        feature = int(input('\nSelection: '))
        print('')

        try:
            match feature:
                case 0:
                    print("\033[36m" + '\nProgram Ends...')
                    break
                case 1:
                    merge_pdfs()
                case 2:
                    split_pdf()
                case 3:
                    watermark_pdf()
                case 4:
                    compress_pdf()
                case 5:
                    encrypt_pdf()
                case 6:
                    decrypt_pdf()
                case 7:
                    convert_pdf_to_images()
                case 8:
                    convert_images_to_pdf()
                case 9:
                    rotate_pdf()
                case _:
                    print("\n\033[31m" + 'Invalid Selection!')
        except ValueError:
            print("\n\033[31m" + "Invalid Selection\n")
        except FileNotDecryptedError:
            print("\n\033[31m" + 'Wrong Password!')
        except Exception as e:
            print("\n\033[31m" + str(e) + '\n')

if __name__ == "__main__":
    main()