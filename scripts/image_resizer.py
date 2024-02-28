# Resize image to 640 width


import os
import cv2
import numpy as np
from tqdm import tqdm
from pathlib import Path
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--root', type=str, default='docs/1. Setup')
    parser.add_argument('--input_markdown', type=str, default='DAS.md')
    parser.add_argument('--width', type=int, default=1440)
    parser.add_argument('--delete_unused', action='store_false')
    parser.add_argument('--img_folder', type=str, default='imgs')
    args = parser.parse_args()

    # Read the markdown file and get the image paths
    with open(os.path.join(args.root, args.input_markdown), 'r') as f:
        lines = f.readlines()
        image_paths = [line.split('](')[1].split(')')[0] for line in lines if '![' in line]

    # Get the list of image if delete_unused is True
    if args.delete_unused:
        image_paths_all = os.listdir(os.path.join(args.root, args.img_folder))
        # Add root to the image paths
        image_paths_all = [os.path.join(args.img_folder, image_path) for image_path in image_paths_all]

        # Delete the unused images
        unused_images = [image_path for image_path in image_paths_all if image_path not in image_paths]
        for unused_image in unused_images:
            os.remove(os.path.join(args.root, unused_image))
            print(f'Removed {unused_image}')

    for image_path in tqdm(image_paths):
        image = cv2.imread(str(os.path.join(args.root,image_path)))
        
        # Check if the image is already smaller than 640
        if image.shape[1] < args.width:
            continue

        # Resize the width to 640
        ratio = args.width / image.shape[1]
        image = cv2.resize(image, (args.width, int(image.shape[0] * ratio)))
        cv2.imwrite(str(os.path.join(args.root,image_path)), image)