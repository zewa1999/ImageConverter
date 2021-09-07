import sys
import os
from PIL import Image


# grab first and second argument
def grab_arguments():
    return sys.argv


# check is new/ exists, if not create the folder
def check_folder_exists():
    args = grab_arguments()
    folder = str(args[2])
    if os.path.exists(folder):
        print("File exists!")
    else:
        print("Folder doesn't exists... Attempting to create new folder.")
        create_folder(args[2])
        print("Folder created successfully!")


def create_folder(output_folder):
    os.makedirs(output_folder)


# loop through Pokedex
def get_images(image_folder):
    return os.listdir(image_folder)


# convert images to png
def convert_to_png():
    args = grab_arguments()
    images = get_images(args[1])
    print("Grabbed the images...Attempting to convert to png. ")
    for image in images:
        img = Image.open(f"{args[1]}{image}")
        cleaned_name = os.path.split(image)[0]
        img.save(f"{args[2]}{cleaned_name}.png", 'png')
    print("Files converted successfully!")
