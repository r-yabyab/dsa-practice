def main():
    print(read_nums())
    print(type(read_nums()))

def read_nums():
    with open("nums.txt") as f:
        content = f.read()

    return content

main()