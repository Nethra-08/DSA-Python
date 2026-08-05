from collections import deque

def palindrome(s):
    q = deque(s)
    rev = ""

    while q:
        rev = q.popleft() + rev

    return s == rev

text = input("Enter a string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
