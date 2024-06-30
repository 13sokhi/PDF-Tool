import os
import fitz
from CodeGenerator import CodeGenerator


class PDFToImage:
    def convert_to_images(self, path: str, output_path: str):
        if not os.path.exists(path):
            raise Exception(f"{path} does NOT exists!")
        if not os.path.exists(output_path):
            raise Exception(f'{output_path} does NOT exist!')
        elif not os.path.isdir(output_path):
            raise Exception("Output path can ONLY be a directory!")

        pdf_doc = fitz.open(path)
        for i in range(len(pdf_doc)):
            page = pdf_doc.load_page(i)
            pix = page.get_pixmap()
            code = CodeGenerator.generate_code(5)
            img_save_path = os.path.join(output_path, f'({i + 1})-{code}.png')
            pix.save(img_save_path)