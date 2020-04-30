import os
import shutil

from glob import glob
from datetime import datetime


# I didn't want to have to write this function, but listdir and glob are both
# somewhat underpowered.
# DFS assume no cycles
def get_all_files(dir_path, file_paths):
    paths = os.listdir(dir_path)
    paths = [os.path.join(dir_path, p) for p in paths]

    for path in paths:
        if os.path.isfile(path):
            file_paths.add(path)
        elif os.path.isdir(path):
            get_all_files(path, file_paths)
        else:
            raise Exception('The following file is not a normal file nor directory: {}'
                .format(path))


def back_up_and_symlink(local_filepaths):
    usr_dir = os.path.expanduser('~/')
    timestamp_string = '.bak-' + datetime.now().strftime('%Y-%m-%d-%H:%M')
    skipped = []
    backed_up = []
    symlinked = []

    for p in local_filepaths:
        dest_file = ''.join([usr_dir] + p.split('./files/'))
        dest_dir = os.path.dirname(dest_file)

        print('looking for {}'.format(dest_file))
        if not os.path.exists(dest_dir):
            print('This directory does not exist. Skipping')
            skipped.append(dest_file)
            continue
        if os.path.exists(dest_file):
            if os.path.islink(dest_file):
                print('{} already a symlink. skipping'.format(dest_file))
                continue
            new_name = dest_file + timestamp_string
            print('Moving {}->{}'.format(dest_file, new_name))
            backed_up.append(dest_file)
        # Do symlinking
        print('Symlinking {}->{}'.format(dest_file, p))
        symlinked.append(dest_file)

    return skipped, backed_up, symlinked

def print_list_info(headline, items):
    print('{} {}{}'.format(headline, len(items), '=' * 40))
    for x in items:
        print(x)

if __name__ == '__main__':
    local_filepaths = set()
    base_dir = os.getcwd()
    get_all_files('./files', local_filepaths)

    print('These are the local repo filepaths')
    for p in local_filepaths:
        print(p)
    
    skipped, backed_up, symlinked = back_up_and_symlink(local_filepaths)

    print('')
    print_list_info('Skipped', skipped)
    print_list_info('Backed up', backed_up)
    print_list_info('Symlinked', symlinked)
