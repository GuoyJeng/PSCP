"""BloodDonation"""
def main():
    """main"""
    age = int(input())
    l = [age]
    if age == 17 or 70>= age >= 60:
        l.append(int(input()))
        l.append(int(input()))
        l.append(input())
    else:
        l.append(int(input()))
        l.append(int(input()))
    if len(l) == 4:
        check = False
        if l[0] == 17 and l[-1] == "True" and l[1] >= 45:
            check = True
        if 60 <= l[0] <= 70 and l[-1] == "True" and l[1] >= 45 and l[2]:
            check = True
        if check:
            print("Yes")
        else:
            print("No")
    elif len(l) == 3:
        if l[0] < 17 or l[0] > 70 or l[1] < 45 or (not l[-1] and l[0] > 55):
            print("No")
        else:
            print("Yes")
main()
