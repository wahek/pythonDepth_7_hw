from os import mkdir, listdir
from random import choice
from .gen_files import generate_files

__all__ = ['gen']


def gen(extension: list[str], name_dir: str = None, count_of_file: int = 1):
    """Создайте новую функцию которая генерирует файлы с разными расширениями.
    ✔ Расширения и количество файлов функция принимает в качестве параметров.
    ✔ Количество переданных расширений может быть любым.
    ✔ Количество файлов для каждого расширения различно.
    ✔ Внутри используйте вызов функции из прошлой задачи"""
    if name_dir:
        if name_dir not in listdir():
            mkdir(name_dir)
    else:
        name_dir = 'default_dir'
    for _ in range(count_of_file):
        generate_files(choice(extension), name_dir + '\\', count_file=1)
