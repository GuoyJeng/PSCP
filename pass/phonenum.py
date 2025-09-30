"""Phone Number"""
def main():
    """main"""
    x = input()
    num_type = input()
    if num_type == "Domestic":
        if len(x) == 9:
            print(x[0],x[1:5],x[5::])
        if len(x) == 10:
            print(x[0:2],x[2:6],x[6::])
    elif num_type == "International":
        if len(x) == 9:
            print("+66",x[1:5],x[5::])
        if len(x) == 10:
            print("+66" + x[1],x[2:6],x[6::])
main()
