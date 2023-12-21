
import json
import csv
from pathlib import Path
import pickle
import os


def convert(file: Path) -> None:
    my_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
        my_dict[name.title()] = float(number)
        with open(f'{file.stem}.json', 'w', encoding='utf-8') as f_write:
            json.dump(my_dict, f_write, indent=2, ensure_ascii=False)


def json_to_csv(file: Path) -> None:
    with open(file, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)

        list_rows = []
        for level, id_name_dict in data.items():
            for id, name in id_name_dict.items():
                list_rows.append({'level': int(level), 'id': int(id), 'name': name})

    with open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(list_rows)


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    json_list = []
    with open(csv_file, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
        if i != 0:
            level, id, name = line
            json_dict['level'] = int(level)
            json_dict['id'] = f'{int(id):010}'
            json_dict['name'] = name.title()
            json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
            json_list.append(json_dict)

    with open(json_file, 'w', encoding='utf-8') as f_write:
        json.dump(json_list, f_write, indent=2)


def json_to_pickle(path: Path) -> None:
    for file in path.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
            with open(f'{file.stem}.pickle', 'wb') as f_writebyte:
                pickle.dump(data, f_writebyte)


def pickle_to_csv(file: Path) -> None:
    with (
            open(file, 'rb') as f_read,
            open(f'{file.stem}.csv', 'w', encoding='utf-8', newline='') as f_write
        ):
        data = pickle.load(f_read)
        headers_list = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=headers_list, dialect='excel-tab', quoting = csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


def csv_to_pickle(file: Path) -> None:
    pickle_list = []
    with open(file, 'r', newline='', encoding='utf-8') as f_read:
        csv_file = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_file):
            print(i, line)
        if i == 0:
            pickle_keys = line
        else:
            pickle_dict = {k: v for k, v in zip(pickle_keys, line)}
            pickle_list.append(pickle_dict)
            print(pickle.dumps(pickle_list))


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
    convert(Path('results.txt'))
    json_to_csv(Path('users.json'))
    csv_to_json(Path('users.csv'), Path('new_users.json'))
    json_to_pickle(Path('D:\\Gb\\py_an\\sem8'))
    pickle_to_csv(Path('new_users.pickle'))
    csv_to_pickle(Path('new_users.csv'))
    directory_research(Path("C:\\GeekBrains\\Python_Data Engineer\\Homework8_package"))