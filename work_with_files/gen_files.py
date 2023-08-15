from secrets import token_bytes
from random import randint, sample
import string

__all__ = ['generate_files']


def generate_files(extension: str, name_dir: str, name_len_min: int = 6, name_len_max: int = 30,
                   count_of_bytes_min: int = 256,
                   count_of_bytes_max: int = 4096, count_file: int = 42):
    """✔ Создайте функцию, которая создаёт файлы с указанным расширением.
    Функция принимает следующие параметры:
    ✔ расширение
    ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
    ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
    ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
    ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
    ✔ количество файлов, по умолчанию 42
    ✔ Имя файла и его размер должны быть в рамках переданного диапазона."""
    for _ in range(1, count_file + 1):
        gen_len = randint(name_len_min, name_len_max)
        gen_name = string.ascii_letters
        gen_count_bytes = randint(count_of_bytes_min, count_of_bytes_max)
        name_file = ''.join(sample(gen_name, gen_len))
        with open(f'{name_dir + name_file}{extension}', 'w', encoding='utf-8') as data:
            while gen_count_bytes > 0:
                if gen_count_bytes >= 32:
                    data.write(f'{str(token_bytes(32))}\n')
                    gen_count_bytes -= 32
                else:
                    data.write(f'{str(token_bytes(gen_count_bytes))}\n')
                    gen_count_bytes = 0
