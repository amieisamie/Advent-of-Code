from typing import List


def read_file(filename: str):
    with open(filename) as f:
        return f.read().splitlines()


def map_int(input_list: List[str]):
    return list(map(int, input_list))
