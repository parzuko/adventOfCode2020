from collections import defaultdict
#accumulator = 5
operations = []
def get_input():
    with open("input.txt", "r+") as file:
        raw_data = file.readlines()
        return raw_data

def split_input(raw_data):
    for each in raw_data:
        each = each.strip()
        operation, number = each.split(" ")
        operations.append([operation, number])

def get_value_of_accumulator(list_of_operations):
    seen = set()
    accumulator = 0
    iterator = 0
    while True:
        if iterator >= len(list_of_operations):
            return accumulator
        operation = list_of_operations[iterator][0]
        number = int(list_of_operations[iterator][1])
        if iterator in seen:
            return accumulator
        seen.add(iterator)
        if operation == "nop":
            iterator += 1
        if operation == "acc":
            accumulator += number
            iterator += 1
        if operation == "jmp":
            iterator += number
def main():
    raw_data = get_input()
    split_input(raw_data)
    #print(operations[0:10])
    accumulator = get_value_of_accumulator(operations)
    print(accumulator)

if __name__ == "__main__":
    main()