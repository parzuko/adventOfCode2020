def find_row(boarding_id):
    low = 0
    high = 127
    index = 0
    for move in boarding_id:
        if move == "F":
            high = find_mid(low, high)
        if move == "B":
            low = find_mid(low, high) + 1
        if index == 6:
            return min (low, high)
        index += 1
        
def find_col(boarding_id):
    low = 0
    high = 7
    boarding_id = boarding_id[6:10]

    index = 0
    for move in boarding_id:
        if move == "R":
            low = find_mid(low, high) + 1
        if move == "L":
            high = find_mid(low, high)
        if index == 3:
            return(max(low, high))
        index += 1

def find_id(col, row):
    seat_id = (row * 8) + col
    return seat_id

def find_mid(low, high):
    mid = (high + low ) // 2
    return mid

def find_max_seat(raw_data):
    highest_id = float('-inf')
    for boarding_pass in raw_data:
        col = find_col(boarding_pass)
        row = find_row(boarding_pass)
        seat_id = find_id(col, row)
        highest_id = max(highest_id, seat_id)
    return highest_id



def get_data():
    with open("input.txt", "r+") as file:
        data = file.readlines()
    return data

def main():
    data = get_data()
    highest = find_max_seat(data)
    print(f"{highest} is the max seat id")


if __name__ == "__main__":
    main()