def main():
    # print(firstUniqueChar())
    print(sort_chars())

def read_chars():
    with open("randchars.txt", "r") as f:
        charArr = list(f.read().strip())
        print(charArr)
        return charArr
    
def firstUniqueChar():
    charArr = read_chars()
    charCount = {}

    for char in charArr:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    for i, char in enumerate(charArr):
        if charCount[char] == 1:
            return char, i

    return 0

def sort_chars():
    charArr = read_chars()
    print(sorted(charArr))
    charArr.sort(reverse = True)
    print(charArr , "sorted")
    # print(charArr)



    
main()