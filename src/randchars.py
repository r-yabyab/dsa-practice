import random
import string

def main():
    with open("randchars.txt", "w") as f:
        random_chars = random.choices(string.ascii_lowercase, k=10)
        # print(''.join(random_chars))
        f.write(''.join(random_chars))


main()