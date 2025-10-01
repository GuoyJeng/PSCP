"""Name of Card"""
def main():
    """main"""
    card = input().upper()
    fisrt = {
        "D" : "Diamonds",
        "H" : "Hearts",
        "C" : "Clubs",
        "S" : "Spades"
    }
    second = {
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "10" : 10,
        "J" : "Jack",
        "Q" : "Queen",
        "K" : "King",
        "A" : "Ace"
    }
    print(f'{second[card[0] if len(card) == 2 else card[0:2]]} of {fisrt[card[-1]]}')
main()
