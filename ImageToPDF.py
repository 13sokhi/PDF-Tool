import os
from PIL import Image

class ImageToPDF:
    def __init__(self):
        self.image_paths: list = list([])

    def add_image(self, path: str):
        if not os.path.isfile(path):
            raise Exception("Only select Image files!")
        elif not path.endswith('.png') or not path.endswith('.jpg') or not path.endswith('.jpeg'):
            raise Exception("Only select .png/.jpg/.jpeg files!")

        self.image_paths.append(path)

    def add_all_directory_images(self, path: str):
        for pdf_path in path:
            self.add_image(pdf_path)

    def create_pdf(self, output_path: str, file_name: str):
        save_path = os.path.join(output_path, f"{file_name}.pdf")
        if not os.path.isdir(output_path):
            raise Exception("Output path can only be a directory!")
        elif os.path.exists(save_path):
            raise Exception(f"{save_path} already exists!")

        first_image = Image.open(self.image_paths[0]).convert('RGB')
        remaining_images = list([])
        for img_path in self.image_paths[1:]:
            remaining_images.append(Image.open(img_path).convert('RGB'))

        first_image.save(save_path, save_all=True, append=remaining_images)

    def clear_images(self):
        self.image_paths = list([])