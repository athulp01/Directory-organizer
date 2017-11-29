#!/usr/bin/python3

import argparse
import os


def path():
    parse = argparse.ArgumentParser(
        add_help=True, description="Organize your files to different directories according to their type")
    parse.add_argument('directory_path', type=str, default='./',
                       help="The absolute path to the directory")
    return parse.parse_args().directory_path


documents = ['.txt', '.doc', '.docx', '.md', '.pdf']
picture = ['.png', '.jpg', 'jpeg', '.bmp']
music = ['.mp3', '.wav']
compressed = ['.zip', '.rar', '.tar', '.gz', '.bz2', '.xz']

directories = [path() + '/Compressed', path() + '/Documents',
               path() + '/Pictures', path() + '/Music']

print("This will organize your files to different directories according to their type!!")
print("Are you sure you want to continue? (y/n)")
flag = input('>>>')
if flag.lower() == 'y':
    try:
        for d in directories:
            os.mkdir(d)
    except FileExistsError:
        pass

    for files in os.listdir(path()):
        dot = (files.rfind('.'))
        if dot is not 0 and dot is not -1:
            if files[dot:].lower() in music:
                os.rename(path() + '/' + files, path() + '/Music/' + files)
            if files[dot:].lower() in picture:
                os.rename(path() + '/' + files, path() + '/Pictures/' + files)
            if files[dot:].lower() in documents:
                os.rename(path() + '/' + files, path() + '/Documents/' + files)
            if files[dot:].lower() in compressed:
                os.rename(path() + '/' + files, path() +
                          '/Compressed/' + files)

    for d in directories:
        if os.listdir(d) is None:
            os.removedirs(d)
else:
    print("Exiting")
    os.sys.exit(0)
