#!/usr/bin/env python
from os.path import join, dirname, exists, isdir
from os import makedirs
from shutil import move
import yaml, argparse

def setup_rename(old_path, new_path):
    if isdir(old_path):
        print('Will not rename a whole directory')
        return

    if exists(new_path):
        print('Will not overwrite', new_path)
        return
    
    if not exists(dirname(new_path)):
        makedirs(dirname(new_path))
    
    move(old_path, new_path)

parser = argparse.ArgumentParser(description='Prepare some renames.')
parser.add_argument('config', help='Configuration file path')

if __name__ == '__main__':
    args = parser.parse_args()
    
    with open(args.config) as input:
        config = yaml.safe_load(input)
        site_dir = config.get('docs_dir')
        
        for (old_name, new_name) in config.get('mz:renames', {}).items():
            print(old_name, '-->', new_name)
            old_path = join(site_dir, old_name)
            new_path = join(site_dir, new_name)
            print(old_path, '==>', new_path)
            setup_rename(old_path, new_path)
