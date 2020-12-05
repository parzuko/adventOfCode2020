fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
import re

def parse_input():
    with open("input.txt", "r+") as file:
        data = file.read()
        line_divided_list = list(data.split("\n\n"))
    return line_divided_list


def check_if_fields_exist(data):
    count = 0
    for each in  data:
        check = 0 
        for pre in fields:
            if pre in each:
                check += 1
            if check == 7:
                count += 1
    return count

def check_field_parameter(raw_data):
    regexps = [r'(byr:(19[2-8][0-9]|199[0-9]|200[0-2]))',
               r'(iyr:(201[0-9]|2020))',
               r'(eyr:(202[0-9]|2030))',
               r'(hgt:(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)',
               r'(hcl:#([0-9]|[a-f]){6})',
               r'(ecl:(amb|blu|brn|gry|grn|hzl|oth))',
               r'(pid:\d{9}(?!\S))']
    count = 0
    for passport in raw_data:
        check = 0
        for exp in regexps:
            if re.search(exp, passport):
                check += 1
            if check == 7:
                count += 1 
    return count

def main():
    data = parse_input()
    number_of_valid_passports = check_if_fields_exist(data) 
    print(f"There are {number_of_valid_passports} valid passports according to part one")

    valid_passport_with_parameters = check_field_parameter(data)
    print(f"There are {valid_passport_with_parameters} valid passports according to the second question")

if __name__ == "__main__":
    main()