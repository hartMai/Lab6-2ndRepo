#added from first account
#2nd try

def decode(coded):
    li = list(coded)
    decoded = ""
    for num in li:
        num = int(num)
        num -= 3
        decoded += str(num)
    return decoded