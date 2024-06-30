import os
from PIL import Image

class ImageToPDF:
    def __init__(self):
        self.image_paths: list = list([])

    def add_image(self, path: str):
        if not os.path.isfile(path):
            raise Exception("Only select Image files!")
        elif not path.endswith('.png') and not path.endswith('.jpg') and not path.endswith('.jpeg'):
            raise Exception("Only select .png/.jpg/.jpeg files!")

        self.image_paths.append(path)

    # add all image files from specified directory to image list
    def add_all_directory_images(self, path: str):
        self.clear_images()
        if not os.path.exists(path):
            raise Exception(f'Directory {path} does NOT exist!')
        folder_content = os.listdir(path)
        for item_path in folder_content:
            if item_path.endswith('.png') or item_path.endswith('.jpg') or item_path.endswith('.jpeg'):
                img_path = os.path.join(path, item_path)
                self.image_paths.append(img_path)
        return self.image_paths

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

        first_image.save(save_path, save_all=True, append_images=remaining_images)

    def clear_images(self):
        self.image_paths = list([])