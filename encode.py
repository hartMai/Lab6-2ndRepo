#Tiffany Dang 2nd acc

def encode(uncoded):
    li = list(uncoded)
    coded = ""
    for num in li:
        num = int(num)
        num += 3
        coded += str(num)
    return coded