TARGET = 2020

from secondsolution import find_triplet

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

def find_product_of_numbers(list_of_numbers):
    output = 1
    for each in list_of_numbers:
        output *= each
    return output

def main():
    with open("input.txt", "r+") as file:
        reader = file.readlines()
    list_of_inputs = convert_input_to_int(reader)
    complements = make_complements(list_of_inputs)
    the_numbers = find_two_numbers_whose_sum_is_target(list_of_inputs, complements)
    product_of_numbers = find_product_of_numbers(the_numbers) 
    print(f"{product_of_numbers} is the first answer")
    triplet_of_numbers = find_triplet(list_of_inputs, TARGET)
    product_of_triplet = find_product_of_numbers(triplet_of_numbers)
    print(f"{product_of_triplet} is the second answer")



if __name__ == "__main__":
    main()