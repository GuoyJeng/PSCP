"""SurprisingVote"""
def main():
    """main"""
    score = float(input())
    person_score = float(input())
    cal = max(0,score - person_score * 2)
    if person_score - cal > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
