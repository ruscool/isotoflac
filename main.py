# main

import sys
import argparse
import os
import pathlib
from pathlib import Path


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', nargs='?', default='.')
    return parser


def work_convert():
    """Get folder and  convert iso to wav"""
    parser = createParser()
    # namespace = '/home/rusdev/Music/Giuliano\ Carmignola'
    namespace = parser.parse_args()
    # print(os.listdir(namespace.folder))  # list files in folder
    # print(os.getcwd())
    path = Path(namespace.folder)
    # path = Path(namespace)
    # print(path)
    return path


def zamena(new_file):
    print(f'in: {new_file}')
    perebor = new_file
    zamena = ['(', ')', ':', '-', '&', "'", ' ']
    # file=new_file.replace(' ','\ ')
    count = len(zamena)
    file = []
    for m in range(count):
        for i in zamena[0]:
            if i in perebor:
                perebor = perebor.replace(i, f'\{i}')
                # file.append(perebor.replace(i, f'm{i}'))
                # print(f'zamena: {perebor}')
            del zamena[0]
    return perebor


def find_iso(path_dir):
    iso_files = []
    for i in os.listdir(path_dir):
        if i.endswith('iso'):
            iso_files.append(i)
            print(f'Find iso: {i}')
    if len(iso_files) > 0:
        return iso_files
    else:
        return 0


def convert_to_wav(path_dir, iso_file):
    os.chdir('/home/rusdev/Projects/sacd/')
    # print(f'folder: {os.getcwd()}')
    # print(f'path: {path_dir}')
    convert_file = f'{path_dir}/{iso_file}'
    file = zamena(convert_file)
    print(f'new path: {file}')
    cmd = f'./sacd -i {file} -r 192000'
    os.system(cmd)
    print("Convert to wav finished")


def covert_to_flac(path_dir):
    """Converter to flac"""
    files = []
    for i in os.listdir(path_dir):
        if i.endswith('wav'):
            files.append(i)
    convert_file = f'{path_dir}/{files[0]}'
    # new_file = convert_file.replace(' ', '\ ')
    os.chdir(path_dir)
    # zamena = [' ', '(', ')', ':', '-', '&']
    # print('111', os.getcwd())
    for file in files:
        file = zamena(file)
        # for i in zamena:
        #     if i in file:
        #         file = file.replace(i, f'\{i}')
        cmd = f'ffmpeg -i {file} {file[:-4]}.flac'
        os.system(cmd)
    # cmd = f'for i in \*.wav; do ffmpeg -i "$i" "$i".flac; done'
    # print(cmd)
    # os.system(cmd)


def delete_file_wav(path_dir):
    """Delete all files in folder"""
    files = []
    os.chdir(path_dir)
    for i in os.listdir(path_dir):
        if i.endswith('wav'):
            files.append(i)
    for count in range(len(files)):
        print(f'Delete: {files[count]}')
        print(os.getcwd())
        os.remove(files[count])
    # print(os.listdir(path_dir))
    print(f'*' * 30)
    print(f'All ready')


if __name__ == '__main__':
    os.chdir('/home/rusdev/Music/Giuliano Carmignola')

    path_folder = work_convert()

    iso_file = find_iso(path_folder)

    convert_to_wav(path_folder, iso_file[0])
    covert_to_flac(path_folder)
    delete_file_wav(path_folder)
