from pdf2image import convert_from_path
import os


class PDFToImage:
    def convert_to_images(self, path: str, output_path: str, dpi: int = 300):
        if not os.path.exists(path):
            raise Exception(f"{path} does NOT exists!")
        elif not os.path.isdir(output_path):
            raise Exception("Output path can ONLY be a directory!")

        pages = convert_from_path(pdf_path=path, dpi=dpi)

        for i, page in enumerate(pages):
            img_save_path = os.path.join(output_path, f' ({i + 1}).png')
            page.save(img_save_path, 'png')
