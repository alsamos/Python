# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from homework7 import *
from random import randint, uniform, choice, choices
from pathlib import Path
from typing import TextIO
from string import ascii_lowercase, digits
from os import chdir

MIN_NUMBER = -1000
MAX_NUMBER = 1000
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def fill_num(filename: str | Path, count: int) -> None:
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(count):
            num_int = randint(MIN_NUMBER, MAX_NUMBER)
            num_float = uniform(MIN_NUMBER, MAX_NUMBER)
        f.write(f'{num_int}|{num_float}\n')


def random_names(filename: str | Path, count: int) -> None:
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(count):
            name = ''
            cur_vowel = choice([-1, 1])
        for _ in range(randint(MIN_LEN, MAX_LEN)):
            if cur_vowel < 0:
                name += choice(VOWELS)
            else:
                name += choice(CONSONANTS)
        cur_vowel *= -1
    print(name.title(), file=f)


def read_line_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.rstrip()


def convert_lines(names: str | Path, numbers: str | Path, results: str | Path) -> None:
    with (
        open('names.txt', 'r', encoding='utf-8') as f_names,
        open('numbers.txt', 'r', encoding='utf-8') as f_numbers,
        open('results.txt', 'a', encoding='utf-8') as f_results,
        ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        max_len = max(len_numbers, len_names)

        for _ in range(max_len):
            name = read_line_or_begin(f_names)
            nums_str = read_line_or_begin(f_numbers)
            num_i, num_f = map(float, nums_str.split('|'))
            multiply = num_i * num_f
            if multiply < 0:
                f_results.write(f'{name.lower()} {-multiply}\n')
            elif multiply > 0:
                f_results.write(f'{name.upper()} {int(multiply)}\n')


# def create_file(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096,
#                 count: int = 42) -> None:
#     for _ in range(count):
#         file_name = ''.join(choices(ascii_lowercase+digits+'_', k=randint(min_len, max_len))) + extension
#         data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
#         with open(file_name, 'wb') as f:
#             f.write(data)


# def generate_file(**kwargs) -> None:
#     for extension, amount in kwargs.items():
#     create_file(extension, count=amount)


def create_file(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096,
                count: int = 42) -> None:
    for _ in range(count):
        print(Path.cwd())
    while True:
        file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len))) + '.' + extension
        if not Path(file_name).is_file():
            break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(file_name, 'wb') as f:
            f.write(data)


def generate_file(filepath: str|Path, **kwargs) -> None:
        if isinstance(filepath, str):
            filepath = Path(filepath)
        if not filepath.is_dir():
            filepath.mkdir(parents=True)
            chdir(filepath)
        for extension, amount in kwargs.items():
            create_file(extension, count=amount)


if __name__ == '__main__':
    generate_file('new', txt=1, bin=2)
    fill_num(Path('numbers.txt'), 256)
    random_names(Path('names.txt'), 120)
    convert_lines(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))
    create_file('.txt', count=2)
    # generate_file(bin=2, jpg=1, txt=3)
    group_rename('012345_', 3, '.csv', '.txt', [0, 6], './')