"""orange"""
def main():
    floor = int(input())
    sold = int(input())
    count = 0
    num = 0
    for i in range(floor):
        count += i * i
    count -= sold
main()
