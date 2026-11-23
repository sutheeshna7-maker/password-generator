import secrets
import string

letters = string.ascii_letters
digits = string.digits
symbols = "!@#$%^&*()-_=+"

min_length = 8
max_length = 64


# keeps asking until the user types a proper number
def get_number(question, low, high):
    while True:
        text = input(question).strip()

        if text == "":
            print("Oops, you didn't type anything.")
        elif not text.isdigit():
            print("Numbers only please.")
        else:
            number = int(text)
            if low <= number <= high:
                return number
            print("Pick a number between", low, "and", high)


def make_password(length):

    chars = [secrets.choice(letters), secrets.choice(digits), secrets.choice(symbols)]
    all_chars = letters + digits + symbols


    while len(chars) < length:
        chars.append(secrets.choice(all_chars))


    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main():
    print("=== My Password Generator ===")

    while True:
        length = get_number("Password length (8-64): ", min_length, max_length)
        how_many = get_number("How many passwords (1-10): ", 1, 10)

        print()
        for i in range(1, how_many + 1):
            print(i, "->", make_password(length))
        print()

        again = input("Want more? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Bye!")
            break


main()