fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
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
def main():
    data = parse_input()
    number_of_valid_passports = check_if_fields_exist(data) 
    print(f" There are {number_of_valid_passports} valid passports according to part one")

if __name__ == "__main__":
    main()