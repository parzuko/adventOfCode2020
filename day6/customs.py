def get_data():
    with open("input.txt", "r+") as file:
        data = file.read().strip().split("\n\n")
    return data

def get_distinct_answers(raw_data):
    groups = [set(each.replace("\n", "")) for each in raw_data]
    total = sum([len(group) for group in groups])
    return total

def main():
    raw_data = get_data()
    part_one = get_distinct_answers(raw_data)
    print(f"The first answer is: {part_one}")


if __name__ == "__main__":
    main()