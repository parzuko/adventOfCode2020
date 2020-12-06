def get_data():
    with open("input.txt", "r+") as file:
        data = file.read().strip().split("\n\n")
    return data

def get_distinct_answers(raw_data):
    groups = [set(each.replace("\n", "")) for each in raw_data]
    total = sum([len(group) for group in groups])
    return total

def get_common_answers(raw_data):
    total = 0
    for each in raw_data:
        answers = each.split("\n")
        answer_one = set(answers[0])
        for remaining_answer in answers[1:]:
            answer_one = answer_one.intersection(remaining_answer)

        total += len(answer_one) 
    return total
def main():
    raw_data = get_data()
    part_one = get_distinct_answers(raw_data)
    part_two = get_common_answers(raw_data)
    print(f"The first answer is: {part_one}")
    print(f"The second answer is: {part_two}")

if __name__ == "__main__":
    main()