def find_max(puzzle_input):
    max = 0
    cur = 0
    for line in puzzle_input:
        if line == "":
            if cur > max:
                max = cur
            cur = 0
        else:
            cur += int(line)
    return max


def find_top_x_sum(puzzle_input, size):
    # create empty list of size size
    top_x = [0] * size
    cur = 0
    for line in puzzle_input:
        if line == "":
            if cur > min(top_x):
                top_x[top_x.index(min(top_x))] = cur
            cur = 0
        else:
            cur += int(line)
    return sum(top_x)



def main():
    max = 0
    cur = 0
    # get puzzle input
    with open("in.txt") as f:
        puzzle_input = f.read().splitlines()
    print(find_max(puzzle_input))
    print(find_top_x_sum(puzzle_input, 3))
    

if __name__ == "__main__":
    main()