import os
import glob

def find(path, extension):
    if not os.path.exists(path):
        return print('Каталог не найден')
    files = glob.glob(path + '**/*.' + extension, recursive=True)
    return print(files)

path1 = input('Введите путь: ')
extension1 = input('Введите расширение: ')
find(path1, extension1)
