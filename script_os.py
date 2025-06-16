import os.path

CURRENT_FILE = os.path.abspath(__file__) # получение абсолютного пути
CURRENT_DIR = os.path.dirname(CURRENT_FILE) # получение абсолютного пути директории
FILE_DIR: str = os.path.join(CURRENT_DIR, 'file') # склеивание пути и папки file
ARCH_DIR = os.path.join(FILE_DIR, 'resourses') # склеивание пути и папки resourses
ZIP_DIR = os.path.join(ARCH_DIR, 'zip_arch.zip') # склеивание пути и файла 'zip_arch.zip'

