import os
import cv2
import numpy as np
from pathlib import Path
from argparse import ArgumentParser
import shutil

def resize_image(image_path, width):
    image = cv2.imread(image_path)
    if image.shape[1] <= width:
        return image_path  # No need to resize

    ratio = width / image.shape[1]
    resized_image = cv2.resize(image, (width, int(image.shape[0] * ratio)))

    new_image_path = image_path.replace(Path(image_path).suffix, '.jpg')
    cv2.imwrite(new_image_path, resized_image)
    return new_image_path

def process_markdown(markdown_path, width, delete_unused):
    with open(markdown_path, 'r') as f:
        lines = f.readlines()
        image_file_names = [line.split('](')[1].split(')')[0] for line in lines if '![' in line]
        image_file_names = [image_path.split('|')[0] for image_path in image_file_names]
    
    # Filtering out web addresses such as https
    image_file_names = [image_path for image_path in image_file_names if not image_path.startswith('http')]

    # Add markdown parent path
    pardir = os.path.dirname(markdown_path)
    image_file_names = [os.path.join(pardir,image_path) for image_path in image_file_names]
    

    if delete_unused:
        trash_folder = 'trash'
        os.makedirs(trash_folder, exist_ok=True)

        all_images = [line.split('](')[1].split(')')[0] for line in lines if '![' in line]
        unused_images = [img for img in all_images if img not in image_file_names]
        for unused_image in unused_images:
            shutil.move(unused_image, os.path.join(trash_folder, Path(unused_image).name))

    for image_file_name in image_file_names:
        if image_file_name.lower().endswith('.gif'):
            absolute_path_src = os.path.abspath(image_file_name)
            os.system(f'gifsicle -O3 --use-col=web --lossy=80 --scale 0.4 "{absolute_path_src}" -o "{absolute_path_src}"')
            continue

        new_image_path = resize_image(image_file_name, width)
        if new_image_path != image_file_name:
            with open(markdown_path, 'r') as f:
                filedata = f.read()
            image_file_name_only = image_file_name.split("/")[-1]
            new_image_path_only = new_image_path.split("/")[-1]
            filedata = filedata.replace(image_file_name_only, new_image_path_only)
            with open(markdown_path, 'w') as f:
                f.write(filedata)
            os.remove(image_file_name)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_markdown', type=str, default="docs/2. Hardware/Drone/1 - 2024-11-18 Assembling propellers.md")
    parser.add_argument('--width', type=int, default=640)
    parser.add_argument('--delete_unused', type=bool, default=False)
    args = parser.parse_args()

    process_markdown(args.input_markdown, args.width, args.delete_unused)