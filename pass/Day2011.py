"""Day2011"""
def main():
    """main"""
    day = int(input())
    month = int(input())
    check_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    check_days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    print(check_days[(sum(check_months[:month - 1]) + day) % 7])
main()
