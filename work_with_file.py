from work_with_files import gen_file_with_extension, sorted_files

LIST_VIDEO = ['AVI', 'mp4']
LIST_TEXT = ['doc', 'docx', 'txt']
LIST_PICT = ['jpg', 'png']
LIST_MUSIC = ['vaf', 'mp3']


# def ex_1(name: str, count: int):
#     with open(name, 'a', encoding='utf-8') as f:
#         for _ in range(count):
#             f.write(f'{random.randint(-1000, 1000)} | {random.random() * random.randint(-1000, 1000)}\n')
#
#
# def give_name():
#     name = ''
#     for _ in range(random.randint(4, 7)):
#         name += chr(random.randint(98, 122))
#     return name.capitalize()
#
#
# def fill_name(name: str, count: int):
#     with open(name, 'a', encoding='utf-8') as f:
#         for _ in range(count):
#             f.write(f'{give_name()}\n')

gen_file_with_extension.gen(['.txt', '.doc', '.docx', '.jpg', '.png', '.mp3', '.mp4', '.AVI'], 'my_dir', 20)
sorted_files.sort()
sorted_files.renamed('csv', 'txt', 'replace_file')
