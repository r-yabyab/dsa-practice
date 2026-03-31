def main():
    make_pyramid()

def make_pyramid():
    # 5 --> *
    #       **
    #       ***
    #       ****
    #       *****

    # for i in range(1,6):
    #     s = ""
    #     for j in range(1, i + 1):
    #         s += "*"
    #     print(s)
    

    
    #*
    #**
    #***
    n = 5
    
    for i in range(1, n+1):
        s = ""
        for j in range(1, i+1):
            s += "*"
        print(s)


main()