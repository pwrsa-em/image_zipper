import os
import fnmatch
import zipfile

def find_images(directory):
    """Finds all image files in a directory and its subdirectories."""
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.tif']
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for extension in image_extensions:
            for filename in fnmatch.filter(filenames, extension):
                matches.append(os.path.join(root, filename))
  
    return matches

def zip_images(images, output_zip):
    """Zips all found images into a single zip file."""
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for image in images:
            zipf.write(image, os.path.relpath(image, os.path.dirname(images[0])))
            

def main():
    # Setting the directory to root of the C: drive on Windows or / on Linux/Mac
    directory = '/'
    output_zip = 'backup.zip'
    
    print(f"Searching for images in {directory}...")
    print("This operation may take time, please wait...")
    images = find_images(directory)
    
    if images:
        zip_images(images, output_zip)
        print(f"Successfully saved {len(images)} images to {output_zip}.")
    else:
        print("No images found in the specified directory.")

if __name__ == "__main__":
    main()
