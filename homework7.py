# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании 
#     в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно 
#     работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона 
#     [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется 
#     желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def group_rename(to_name, nums, from_extension, to_extension, range_initial_name, path=str):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(from_extension):
            old_name = os.path.splitext(filename)[0] 
            if range_initial_name:
                old_name_str = old_name[range_initial_name[0]:range_initial_name[1]]  
            else:
                ""
            new_filename = f"{old_name_str}{to_name}{str(counter).zfill(nums)}{to_extension}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            counter += 1

if __name__ == '__main__':
    group_rename('012345_', 3, '.csv', '.txt', [0, 6], './')