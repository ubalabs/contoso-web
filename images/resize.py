# This code was written by Copilot in response to a prompt request
# for a function that would 
# 1. Take 3 arguments: input_folder, output_folder, size
# 2. Resize all images in the input_folder to the given size
# 3. Save the resized images in the output_folder
# 4. Preserve the folder structure of the input_folder in the output_folder
# 5. Create the output_folder if it doesn't exist
# 6. Overwrite any existing files in the output_folder
# ----------------------------------------------------------------------
# The code was used to resize images from the `public.images/` folder
# to a `sm` folder that was then manually copied over into `public/images`
# for use in the static web app.

import os
from PIL import Image
import os
from PIL import Image

def resize_images_in_folder(input_folder, output_folder, size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            # Get the relative path of the file
            relative_path = os.path.relpath(root, input_folder)
            # Create the corresponding subfolder in the output folder
            output_subfolder = os.path.join(output_folder, relative_path)
            os.makedirs(output_subfolder, exist_ok=True)

            # Resize the image
            image = Image.open(os.path.join(root, filename))
            image.thumbnail(size)
            output_path = os.path.join(output_subfolder, filename)
            image.save(output_path)

        
# Usage
resize_images_in_folder('./images', './sm', (400, 400))