from Item import Item
import os

MAX_FOLDER_DL_SIZE_BYTES = os.environ.get('MAX_FOLDER_DL_GB', 2) * 1000 * 1000 * 1000 # GB to Bytes

ROOT_PATHS = []
_ROOT_PATHS = os.environ.get('ROOT_PATHS')
if _ROOT_PATHS:
    for path in _ROOT_PATHS.split(';'):
        path, name = path.split(':')
        ROOT_PATHS.append(Item(path, name))

IGNORE_FILES = os.environ.get('IGNORE_FILES_RE', r'(^\..*$|^lost\+found$|^Temporary Items$|^Network Trash Folder$)')
