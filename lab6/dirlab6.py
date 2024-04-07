"""#1
import os
path = "C:\\Users\\Пк\\Documents\\lab6_example"
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])"""

"""#2

import os
print('Exist:', os.access('C:\\Users\\Пк\\Documents\\lab6_example', os.F_OK))
print('Readable:', os.access('C:\\Users\\Пк\\Documents\\lab6_example', os.R_OK))
print('Writable:', os.access('C:\\Users\\Пк\\Documents\\lab6_example', os.W_OK))
print('Executable:', os.access('C:\\Users\\Пк\\Documents\\lab6_example', os.X_OK))"""
#3
"""import os
print("Test a path exists or not:")
path = r'C:\\Users\\Пк\\Documents\\lab6_example'
print(os.path.exists(path))
path = r'C:\\Users\\Пк\\Documents\\lab6_example'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))"""
"""#4
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("text_file_with_strings.txt"))
#5
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())"""
#6
"""import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)"""
#7
"""from shutil import copyfile
copyfile('test.txt', 'abc.txt')"""
"""#8
import os

def delete_file(path):
    # Проверяем существование файла
    if not os.path.exists(path):
        print(f"Файл {path} не существует.")
        return

    # Проверяем доступ к файлу для записи
    if not os.access(path, os.W_OK):
        print(f"Нет доступа к записи в файл {path}.")
        return

    # Удаляем файл
    try:
        os.remove(path)
        print(f"Файл {path} успешно удален.")
    except Exception as e:
        print(f"Произошла ошибка при удалении файла {path}: {e}")

# Указываем путь к файлу, который нужно удалить
specified_path = "/path/to/your/file"

# Удаляем файл по указанному пути
delete_file(specified_path)"""

