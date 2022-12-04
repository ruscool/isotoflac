import os
from engine.links import sacd

path_sacd = f'/home/rusdev'


def yes():
    return 'sacd installed'


def finding(path):
    os.chdir(path)
    folders = os.listdir('.')
    # print(os.system('ls -alth'))
    if 'sacd' in folders:
        yes()
    else:
        os.system(f'git clone {sacd}')
        os.system(f'cd sacd && sudo -S make install')
        yes()


if __name__ == '__main__':
    finding(path_sacd)
