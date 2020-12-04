length_of_row = 32

def parse_input():
    map = []
    with open("input.txt", "r+") as file:
        reader = file.readlines()
    for each in reader:
        map.append(each.rstrip() * 1000)
    return map


def traverse_map(map, right_increment, down_increment):
    row = 0
    col = 0
    count = 0

    while True:
        try:
            if map[col][row] == "#":
                count += 1
        except Exception:
            break
        row += right_increment
        col += down_increment 

    return count

def main():
    tree_map = parse_input()
    tree_count = traverse_map(map=tree_map, right_increment=3, down_increment=1)
    print(f"There are {tree_count} trees in the way!")

if __name__ == "__main__":
    main()