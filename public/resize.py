import os
from PIL import Image

def resize_images_in_folder(src_folder, dst_folder, new_size):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for subdir, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                img_path = os.path.join(subdir, file)
                img = Image.open(img_path)
                img = img.resize(new_size, Image.ANTIALIAS)

                dst_dir = subdir.replace(src_folder, dst_folder)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)

                img.save(os.path.join(dst_dir, file))

# Usage
resize_images_in_folder('./images', './sm', (800, 600))