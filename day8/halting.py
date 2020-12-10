def get_input():
    with open("input.txt", "r") as file:
        operations = file.readlines()
        operations = [line.rstrip() for line in operations]
        return operations
        
def get_accumulator(operations):
    accmumulator = 0
    seen = set()
    iterator  = 0
    status = True
    while True: 

        # no loops
        if len(operations) - 1 == iterator :
            status = False

        if iterator  in seen:
            status = False
            return accmumulator, status

        operation, acc = operations[iterator ].split(" ")
        acc = int(acc)
        seen.add(iterator )

        if operation == "nop":
            iterator  += 1
        if operation == "acc":
            accmumulator += acc
            iterator  += 1 
        if operation == "jmp":
            iterator += acc
        if status == False:
            return accmumulator, True 
    return accmumulator, False

def switch_operations(lines):
    iterator = 0
    new_operations = lines.copy()
    for iterator in range(len(new_operations)):   
        operation, acc = lines[iterator].split(" ")
        acc = int(acc)

        if operation == "nop":
            operation = "jmp"
        elif operation == "jmp":
            operation = "nop"
        new_operations = lines.copy()
        new_operations[iterator] = " ".join((operation, str(acc)))
        acc, valid = get_accumulator(new_operations)
        if valid:
            return acc


def main():
    operations = get_input()
    accumulator = get_accumulator(operations)[0]
    print(f"The first answer is : {accumulator}")
    accumulator = switch_operations(operations)
    print(f"The second answer is : {accumulator}")

if __name__ == "__main__":
    main()