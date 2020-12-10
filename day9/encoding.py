def get_input():
    with open("input.txt", "r") as file:
        raw_data = file.readlines()
        raw_data = [int(data) for data in raw_data]
        return raw_data

def find_exception(data, preamble):
    iterator = preamble + 1
    for number in data[preamble:]:
        flag = False
        sieve = data[iterator - preamble - 1: iterator - 1]
        for each in sieve:
            if number - each in sieve:
                flag = True
                break
        
        if not flag:
            return number
        
        iterator += 1


def main():
    data = get_input()
    PREAMBLE = 25
    exception = find_exception(data,PREAMBLE)
    print(f"{exception} is the first number breaking the preamble")
    
if __name__ == "__main__":
    main()
