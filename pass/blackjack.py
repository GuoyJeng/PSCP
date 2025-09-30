"""BlackJack"""
def main():
    """main"""
    x = int(input())
    score = 0
    ace = 0
    for _ in range(x):
        card = input()
        if card == "A":
            score += 1
            ace += 1
            continue
        if card in ("J","K","Q"):
            score += 10
            continue
        score += int(card)
    while ace > 0 and score + 10 <= 21:
        score += 10
        ace -= 1
    print(score)
main()
