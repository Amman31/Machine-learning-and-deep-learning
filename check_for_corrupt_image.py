from PIL import Image
import os

def check_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Add other extensions as needed
            try:
                img = Image.open(os.path.join(directory, filename)) 
                img.verify()  # Verify that it is a valid image
            except (IOError, SyntaxError) as e:
                print(f"Corrupt image file: {filename}")

# Check your training dataset
check_images('Images_Validation/cat')
