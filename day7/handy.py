from collections import defaultdict, deque

colors1 = defaultdict(list)
colors2 = defaultdict(list)

def get_input():
    with open("input.txt", "r") as file:
        return [each.strip() for each in file.readlines()]

def populate_hashmap(raw_data):
    for each in raw_data:
        parent_bag, contents  = [data for data in each.split(" bags contain ")]
        contents = contents.replace(".", "").split(", ")
        for content in contents:
            if content != "no other bags":
                number = int(content[0])
                child_bag = content[2:].split(" bag")[0]
                child_bag = child_bag.strip()
                colors1[child_bag].append((number, parent_bag)) # parent colors for each color
                colors2[parent_bag].append((number, child_bag)) # child colors for each color
                


def main():
    data = get_input()
    populate_hashmap(data)
    part_one = first_part("shiny gold")
    print(f"the answer is {part_one}")

def first_part(parent_color):
    final = []
    temp = deque([parent_color])
    while len(temp) > 0:
        for each in filter(lambda y: y == temp[-1], colors1.keys()):
            for color in filter(lambda x: x[1] not in final and x[1] not in temp, colors1[each]):
                temp.appendleft(color[1])
        final.append(temp.pop())
    return len(final) - 1


if __name__ == "__main__":
    main()