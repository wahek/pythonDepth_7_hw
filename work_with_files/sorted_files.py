from os import walk, getcwd, replace, makedirs, rename

LIST_VIDEO = ['AVI', 'mp4']
LIST_TEXT = ['doc', 'docx', 'txt']
LIST_PICT = ['png', 'jpg']
LIST_MUSIC = ['vaf', 'mp3']

__all__ = ['sort', 'renamed']


def sort():
    for path, directs, files in walk(getcwd()):
        for file in files:
            try:
                temp = file.split('.')[1]
                if temp in LIST_PICT:
                    try:
                        current_path = fr'{getcwd()}\replace_file\PICTURES'
                        makedirs(current_path)
                    except FileExistsError:
                        pass
                    replace(fr'{path}\{file}', fr'{current_path}\{file}')
                if temp in LIST_MUSIC:
                    try:
                        current_path = fr'{getcwd()}\replace_file\MUSIC'
                        makedirs(current_path)
                    except FileExistsError:
                        pass
                    replace(fr'{path}\{file}', fr'{current_path}\{file}')
                if temp in LIST_TEXT:
                    try:
                        current_path = fr'{getcwd()}\replace_file\TEXT'
                        makedirs(current_path)
                    except FileExistsError:
                        pass
                    replace(fr'{path}\{file}', fr'{current_path}\{file}')
                if temp in LIST_VIDEO:
                    try:
                        current_path = fr'{getcwd()}\replace_file\VIDEO'
                        makedirs(current_path)
                    except FileExistsError:
                        pass
                    replace(fr'{path}\{file}', fr'{current_path}\{file}')
            except IndexError:
                pass


def renamed(output_extends: str, input_extends: str, direction: str = getcwd(),
            start: int = 0, stop: int = 3, round_num: int = 3):
    """- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    - принимать параметр количество цифр в порядковом номере.
    - принимать параметр расширение исходного файла.
    Переименование должно работать только для этих файлов внутри каталога.
    - принимать параметр расширение конечного файла.
    - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
    берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
    Далее счётчик файлов и расширение."""
    for path, direct, files in walk(direction):
        for count, file in enumerate(files):
            try:
                if file.split('.')[1] == input_extends:
                    rename(fr'{path}\{file}', fr'{path}\{file[start:stop]}{count:{0}{round_num}}.{output_extends}')
            except IndexError:
                pass
