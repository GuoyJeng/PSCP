"""BTSMRT"""
def main():
    """main"""
    day = input()
    age = float(input())
    hei = float(input())
    if age < 14 and hei <= 140 and day == "Children Day":
        print("FREE")
    elif age < 14 and hei < 90:
        print("FREE")
    elif age >= 60 and day == "Senior Day":
        print("FREE")
    else:
        print("PAY")
main()
