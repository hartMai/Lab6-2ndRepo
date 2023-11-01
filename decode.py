#added from first account
#edit to get a commit from main acc

def decode(coded):
    li = list(coded)
    decoded = ""
    for num in li:
        num = int(num)
        num -= 3
        decoded += str(num)
    return decoded