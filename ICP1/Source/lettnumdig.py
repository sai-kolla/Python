
string = raw_input("Enter a string: ")
digits = 0
letters = 0

for c in string:
    if c.isdigit():
        digits=digits+1
    elif c.isalpha():
        letters=letters+1
    else:
        pass
print("number of words: ", len(string.split()))
print("no. of Letters: ", letters)
print("no. of Digits: ", digits)
