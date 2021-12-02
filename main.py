def get_increasing_count(lines):
    previous_line = lines[0]
    count = 0
    for line in lines:
        if line > previous_line:
            count = count + 1
        previous_line = line
    return count


def sum_of_lines(lines):
    newLines = []
    for i in range (0, len(lines) - 2):
        newLines.append(lines[i] + lines[i+1] + lines[i+2])
    return newLines


with open('SonarSweep2.txt') as f:
    lines = list(map(int, f.read().splitlines()))
    print(sum_of_lines(lines))
    print(get_increasing_count(sum_of_lines(lines)))

