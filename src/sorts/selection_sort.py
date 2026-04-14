
def main():
    data = []
    with open("../nums.txt", "r") as f:
        data = f.read().split(",")
        print(data)

        for i in range(len(data)):
            data[i] = int(data[i])

        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if (data[i] > data[j]):
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp
        print(data)

main()