"""Palindrome"""
def main():
    n = int(input())
    x = input()
    result = x
    result = result.replace(result[len(x) - 1],x[0],-1)
    for i in range(n):
        
main()
