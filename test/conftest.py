import pytest
import os
import zipfile
import shutil

from script_os import ARCH_DIR, ZIP_DIR, FILE_DIR


@pytest.fixture(scope="session")
def create_archive():
    if not os.path.exists(ARCH_DIR):  # проверяем существует ли папка
        os.mkdir(ARCH_DIR)  # создаем папку если её нет
    with zipfile.ZipFile(ZIP_DIR, 'w') as zf:  # создаем архив
        for file in os.listdir(FILE_DIR): # добавляем файлы в архив
            add_file = os.path.join(FILE_DIR, file)  # склеиваем путь к файлам которые добавляют в архив
            zf.write(add_file, os.path.basename(add_file))  # добавляем файл в архив

    yield
    shutil.rmtree(ARCH_DIR)  # удаляем папку со всеми файлами и подпапками

