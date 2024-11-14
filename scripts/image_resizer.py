# Resize image to 640 width


import os
import cv2
import numpy as np
from pathlib import Path
from argparse import ArgumentParser
import shutil

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--root', type=str, default='docs/2. Hardware')
    parser.add_argument('--input_markdown', type=str, default='Ground Control Points (GCPs).md')
    parser.add_argument('--width', type=int, default=640)
    parser.add_argument('--delete_unused', type=bool, default=True)
    parser.add_argument('--img_folder', type=str, default='attachment')
    args = parser.parse_args()

    # Read the markdown file and get the image paths
    with open(os.path.join(args.root, args.input_markdown), 'r') as f:
        lines = f.readlines()
        image_file_names = [line.split('](')[1].split(')')[0] for line in lines if '![' in line]

        # Remove '|' from the image paths
        image_file_names = [image_path.split('|')[0] for image_path in image_file_names]

    # Get the list of image if delete_unused is True
    if args.delete_unused:
        # Create trash folder in the root
        trash_folder = 'trash'
        if not os.path.exists(trash_folder):
            os.makedirs(trash_folder)

        image_paths_all = os.listdir(os.path.join(args.root, args.img_folder))
        # Add root to the image paths
        image_paths_all = [os.path.join(args.img_folder, image_path) for image_path in image_paths_all]

        # Delete the unused images
        unused_images = [image_path for image_path in image_paths_all if image_path not in image_file_names]
        for unused_image in unused_images:
            if 0:
                os.remove(os.path.join(args.root, unused_image))
                print(f'Removed {unused_image}')
            else:
                # Get abs path from relative path os.path.join(args.root, unused_image)
                absolute_path_src = os.path.abspath(os.path.join(args.root, unused_image))
                absolute_path_dsc = os.path.abspath(os.path.join(trash_folder, unused_image.split('/')[-1]))
                # Move the file to trash folder using shutil
                shutil.move(absolute_path_src, absolute_path_dsc)

                

    for image_file_name in image_file_names:
        if image_file_name.split('.')[-1] == 'gif':
            # Compress gif image under 10mb  using gifsicle
            absolute_path_src = os.path.abspath(os.path.join(args.root, image_file_name))
            absolute_path_dsc = os.path.abspath(os.path.join(trash_folder, image_file_name.split('/')[-1]))
            shutil.copy(absolute_path_src, absolute_path_dsc)
            os.system(f'gifsicle -O3 --use-col=web --lossy=80 --scale 0.4 "{absolute_path_src}" -o "{absolute_path_src}"')
            continue

        image = cv2.imread(str(os.path.join(args.root,image_file_name)))
        
        # Get file extension usng library
        file_extension = Path(image_file_name).suffix

        # Check if the image is already smaller than 640
        if image.shape[1] <= args.width and file_extension != '.png':
            continue

        # Resize the width to 640
        ratio = args.width / image.shape[1]
        image = cv2.resize(image, (args.width, int(image.shape[0] * ratio)))

        # change the file extension to jpg
        image_file_name_jpg = image_file_name.replace(file_extension, '.jpg')

        # Change the space to underscore
        image_file_name_jpg = image_file_name_jpg.replace(' ', '_')
        
        cv2.imwrite(str(os.path.join(args.root,image_file_name_jpg)), image)


        # Change the markdown file
        with open(os.path.join(args.root, args.input_markdown), 'r') as f:
            filedata = f.read()
        # Replace the target string
        filedata = filedata.replace(image_file_name, image_file_name_jpg)
        # Write the file out again
        with open(os.path.join(args.root, args.input_markdown), 'w') as f:
            f.write(filedata)

        if 1:
            # Remove the original image
            os.remove(str(os.path.join(args.root,image_file_name)))
        else:
            # Move the original image to trash folder
            absolute_path_src = os.path.abspath(os.path.join(args.root, image_file_name))
            absolute_path_dsc = os.path.abspath(os.path.join(trash_folder, image_file_name.split('/')[-1]))
            shutil.move(absolute_path_src, absolute_path_dsc)

