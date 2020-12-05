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

# Solution to part two
def different_paths_on_same_slope(tree_map):
    tree_count = traverse_map(map=tree_map, right_increment=1, down_increment=1)
    tree_count *= traverse_map(map=tree_map, right_increment=3, down_increment=1)
    tree_count *= traverse_map(map=tree_map, right_increment=5, down_increment=1)
    tree_count *= traverse_map(map=tree_map, right_increment=7, down_increment=1)
    tree_count *= traverse_map(map=tree_map, right_increment=1, down_increment=2)

    return tree_count



def main():
    tree_map = parse_input()
    tree_count = traverse_map(map=tree_map, right_increment=3, down_increment=1)
    print(f"There are {tree_count} trees in the way!")
    second_solution = different_paths_on_same_slope(tree_map)
    print(f"The product of all the trees in the path is : {second_solution}")

if __name__ == "__main__":
    main()