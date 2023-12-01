def productExceptSelf(nums):
    length = len(nums)
    answer = []
    for i in range(length):
        product = 1
        for j in range(length):
            if i != j:
                product *= nums[j]
        answer.append(product)

    return answer


productExceptSelf([1, 2, 3, 4])  # [24, 12, 8, 6]
