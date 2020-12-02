def parse_file():
    with open("input.txt", "r+") as file:
        data = file.readlines()
        list_of_input = list(data)
    return list_of_input

def get_range_from_input(password):
    first_number = ""
    second_number = ""
    flag = True
    for chars in password:
        if chars == " ":
            break
        if chars == "-":
            flag = False
            continue 
        if flag == True:
            first_number += chars
        else:
            second_number += chars
    return [int(first_number), int(second_number)]


def get_password_key(password):
    flag = False
    key = ""
    for chars in password:
        if flag == True:
            key += chars
            break  
        if chars == " ":
            flag = True
            continue
    return key

def get_password(password):
    flag = False
    answer = ""
    for chars in password:
        if chars == ":":
            flag = True
            continue
        if flag == True:
            answer += chars
    
    return answer[1:]

def get_valid_password_count(passwords):
    count = 0
    for password in passwords:
        numbers = get_range_from_input(password)
        key = get_password_key(password)
        actual_password = get_password(password)
        first = numbers[0]
        second = numbers[1] + 1

        if actual_password.count(key) in range(first, second):
            count += 1
    
    return count


# Second Solutions
def get_index_based_validity(passwords):
    count = 0
    for password in passwords:
        numbers = get_range_from_input(password)
        key = get_password_key(password)
        actual_password = get_password(password)
        first = numbers[0] - 1
        second = numbers[1] - 1

        if actual_password[first] == key and actual_password[second] != key:
            count += 1
        if actual_password[first] != key and actual_password[second] == key:
            count += 1
        
    return count


def main():
    list_of_input = parse_file()
    number_of_vaild_passwords = get_valid_password_count(list_of_input)
    print(f"There are {number_of_vaild_passwords} satisfying the first condition")
    
    number_of_index_based_passwords = get_index_based_validity(list_of_input)
    print(f"There are {number_of_index_based_passwords} satisfying the second condition")


if __name__ == "__main__":
    main()