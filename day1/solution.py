TARGET = 2020

def convert_input_to_int(list_of_inputs):
    number_of_inputs = len(list_of_inputs)
    for each in range(number_of_inputs):
        list_of_inputs[each] = int(list_of_inputs[each])
    return list_of_inputs

def make_complements(list_of_inputs):
    complements = {}
    for each in list_of_inputs:
        if each not in complements:
            complements[each] = abs(TARGET - each)

    return complements 

def find_two_numbers_whose_sum_is_target(list_of_inputs, complements):
    for each in list_of_inputs:
        if complements[each] in list_of_inputs:
            return (each, complements[each])


def main():
    with open("input.txt", "r+") as file:
        reader = file.readlines()
    list_of_inputs = convert_input_to_int(reader)
    complements = make_complements(list_of_inputs)
    the_numbers = find_two_numbers_whose_sum_is_target(list_of_inputs, complements)
    product_of_numbers = the_numbers[0] * the_numbers[1]
    print(product_of_numbers)

if __name__ == "__main__":
    main()