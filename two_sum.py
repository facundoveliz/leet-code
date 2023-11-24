def twoSum(nums, target):
    for index1, num1 in enumerate(nums):
        for index2, num2 in enumerate(nums):
            output = []
            if num1 + num2 == target and index1 != index2:
                output = [index1, index2]
                return output

print(twoSum([15, 7, 11, 2], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
