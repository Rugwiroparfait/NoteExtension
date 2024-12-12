from PIL import Image
import os

# Input directory containing your images
input_dir = "/home/kali/Documents/Projects/NoteExtension/Images"
output_dir = os.path.join(input_dir, "resized")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Target sizes
output_sizes = {"icon16.png": (16, 16), "icon48.png": (48, 48), "icon128.png": (128, 128)}

# Iterate through files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".png"):  # Process only PNG files
        input_path = os.path.join(input_dir, file_name)
        img = Image.open(input_path)
        
        for size_name, size in output_sizes.items():
            resized_img = img.resize(size, Image.ANTIALIAS)
            output_file = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_{size_name}")
            resized_img.save(output_file, format="PNG")
            print(f"Saved resized image: {output_file}")

print("All images resized successfully!")
