#main.py

import encode
import decode


def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


if __name__ == '__main__':
    option = -1
    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encode.encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decode.decode(password)}\n")
        elif option == 3:
            exit()
