import random

def main():

    nums = []

    for x in range(5):
        # print(random.randint(-100,100))
        nums.append(random.randint(-100,100))
    
    for num in nums:
        print(num)

    with open("nums.txt", "w" ) as f:
        for num in range(len(nums) - 1):
            f.write(f"{nums[num]}, ")
        f.write(f"{nums[(len(nums) - 1)]}")


main()