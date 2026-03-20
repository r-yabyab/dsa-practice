def main():
    print(readnums())
    print(sortAscSelection())

def sortAscSelection():
    #   sort()
    nums, *rest = readnums()
    # print(sort()[2])
    print(nums)

    sorted = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[j]<nums[i]):
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
    
    return nums
    
    # for (int i = 0; i<nums.length; i++) {
    #     for (int j = i+1
    # }

    # [1, 2, 3, 4]
    # 12, 13, 14
    # 23, 24
    # 34


def readnums():
    nums = []
    numss = [1]
    numsss = [2]

    with open("nums.txt") as f:
        content = f.read()
        nums = content.split(",")

    # for num in nums:
    #     num = num.strip()

    for num in nums:
        print("1",num,"1", sep="")

    print(nums)

    for i in range(len(nums)):
        # print(nums[i])
        nums[i] = int(nums[i].strip())
        # nums[i] = nums[i].strip()

    for num in nums:
        print(num, sep="")

    print(nums)
    return nums, numss, numsss


main()