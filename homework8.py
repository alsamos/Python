# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import csv
import json
import pickle
from pathlib import Path


def directory_research(directory_path):
    results = []
    for parent, dirs, files in os.walk(directory_path):
        for name in files:
            full_path = os.path.join(parent, name)
            results.append({"Name": name,
                            "Root_Directory": parent, 
                            "File_or_Directory": 'File',
                            "The_Size": f'{os.path.getsize(full_path)} bytes'
                            })
        for name in dirs:
            full_path = os.path.join(parent, name)
            results.append({"Name": name,
                            "Root_Directory": parent, 
                            "File_or_Directory": 'Directory',
                            "The_Size": f'{the_size(full_path)} bytes'
                            })
    with open("result.json", "w", encoding='utf-8') as json_write:
        json.dump(results, json_write)
    with open("result.csv", "w", encoding='utf-8', newline='') as csv_write:
        headers_list =  list(results[0].keys())
        writer = csv.DictWriter(csv_write, fieldnames=headers_list)
        writer.writeheader()
        writer.writerows(results)
    with open("result.pickle", "wb") as pickle_writebyte:
        pickle.dump(results, pickle_writebyte)


def the_size(path):
    the_size_calc = 0
    for dirs, parent, files in os.walk(path):
        for f in files:
            route = os.path.join(dirs, f)
            the_size_calc += os.path.getsize(route)
    return the_size_calc


if __name__ == '__main__':
    directory_research(Path("C:\\GeekBrains\\Python_Data Engineer\\Homework8_package"))