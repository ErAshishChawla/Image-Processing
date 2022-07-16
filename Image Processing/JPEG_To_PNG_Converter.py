import sys
import os
import re

from PIL import Image


class ParentFolderNotPresent(Exception):
    pass


class StorageFolderCreationFailed(Exception):
    pass


class NoJpgImageInParentFolder(Exception):
    pass


# function to check if parent folder exists in current directory
def check_path(folder):
    folder_path = f'.\\{folder}'
    is_dir = os.path.isdir(folder_path)
    return is_dir


def create_folder(storage_folder, parent_folder):
    try:
        parent_path = f'.\\{parent_folder}'
        path = os.path.join(parent_path, storage_folder)
        os.mkdir(path)
    except:
        return False


if __name__ == '__main__':
    regex = r"[a-zA-z\d]+[\.][j]{1}[p]{1}[e]{,1}[g]$"
    pattern = re.compile(regex)
    try:
        directory_folder = sys.argv[1]
        storage_folder = sys.argv[2]
        print(storage_folder)
        if not (check_path(directory_folder)):
            raise ParentFolderNotPresent
        if not (check_path(directory_folder + storage_folder)):
            status = create_folder(storage_folder, directory_folder)
            if not status:
                raise StorageFolderCreationFailed
        # converting images
        directory_folder_path = f'.\\{directory_folder}'

        only_jpgs = [f for f in os.listdir(directory_folder_path) if
                     os.path.isfile(os.path.join(directory_folder_path, f)) and pattern.fullmatch(f)]
        jpg_count = len(only_jpgs)

        if jpg_count == 0:
            raise NoJpgImageInParentFolder

        for image in only_jpgs:
            image_name = image.split('.')
            img = Image.open(os.path.join(directory_folder_path, image))
            img.save(os.path.join(directory_folder_path, storage_folder, f'{image_name[0]}_png.png'), 'png')

    except ParentFolderNotPresent:
        print(f'''
        {directory_folder} is not present in the current directory.
        Please specify the correct path of the folder containing the images and rerun the program
        ''')
    except StorageFolderCreationFailed:
        print('Error occurred during creation of storage folder')

    except NoJpgImageInParentFolder:
        print(f'There is no jpg image in {directory_folder}. Please add some images and rerun the program')
