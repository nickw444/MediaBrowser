from Item import Item

MAX_FOLDER_DL_SIZE_BYTES = 2 * 1000 * 1000 * 1000 # GB to Bytes
ROOT_PATHS = [
    Item('/', 'Macintosh HD'),
    Item('/Volumes/iData/', 'iData')
]
IGNORE_FILES = r'^\..*$'