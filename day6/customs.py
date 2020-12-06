from collections import Counter

def get_input():
    with open("input.txt", "r+") as file:
        data = file.read().split("\n")
        return data

def total_answered(group):
    distinct_elements = Counter(group)
    return len(distinct_elements)

def get_sum_of_counts(raw_data):
    total_count = 0
    group_data = ""
    i = 0
    for data in raw_data:
        if data != "":
            group_data += data
        if data == "" or i == len(raw_data) -1:
            total_count += total_answered(group_data)
            group_data = ""
        i += 1 
    return total_count

def main():
    raw_data = get_input()
    answers = get_sum_of_counts(raw_data)
    print(f"There are {answers} distinct answers")

if __name__ == "__main__":
    main()