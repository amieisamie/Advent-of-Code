from typing import List

from day1_sonarsweep import read_file

def run_day2_solution():
    lines = read_file('DiveInstructions.txt')
    print(loop_through_instructions(lines))

def loop_through_instructions(lines:List[str]):
    horizontal_position, vertical_depth, aim = 0, 0, 0
    for line in lines:
        command, value = line.split()
        value = int(value)
        if command == "forward":
            horizontal_position += value
            vertical_depth += aim*value
        elif command == "down":
            aim += value
        else:
            aim -= value
    return horizontal_position * vertical_depth

