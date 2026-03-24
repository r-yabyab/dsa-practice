def main():

    # -81, 5, 96, 28, 17
    # -81 5
    # 5, 95
    # 96, 28 -> 28,96

    # start [0] len(arr)
    # 96, 4, 1, 3
        # 96, 4 -> 4, 96, 1, 3
        # 96, 1 -> 4, 1, 96, 3
        # ends 4, 1, 3, 96
    # start [0] len(arr) -1
    # 4, 1, 3, 96
        # 1, 3
        # 

    nums = []
    with open("../nums.txt", "r") as f:
        content = f.read()
        nums = content.split(",")
        for i in range(len(nums)):
            nums[i] = int(nums[i].strip())

    print(nums)
    
    for i in range(len(nums) -1):
        for j in range(len(nums) - i -1):
            if (nums[j] > nums[j+1]):
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
            print(nums, "index ", i)
    
    print(nums)

main()
        