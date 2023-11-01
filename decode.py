#added from first account
#edited to get a commit from first acc

def decode(coded):
    li = list(coded)
    decoded = ""
    for num in li:
        num = int(num)
        num -= 3
        decoded += str(num)
    return decoded