"""Bus Seat"""
def main():
    """main"""
    row = int(input())
    seat = int(input())
    my_seat = int(input())
    check = 0
    for i in range(row,0,-1):
        for j in range(seat):
            if i + row * j == my_seat:
                print('XX',end='' if j == seat - 1 else ' ')
            else:
                print(f'{i + row * j:02d}',end='' if j == seat - 1 else ' ')
        check += 1
        if check == 2 and i != 1:
            check = 0
            print()
        print()
main()
