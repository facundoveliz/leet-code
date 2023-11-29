def topKFrequent(nums, k):
    numsFreq = {}
    for num in nums:
        if num in numsFreq:
            numsFreq[num] += 1
        else:
            numsFreq[num] = 1

    sorted_nums = sorted(numsFreq.items(), key=lambda x: x[1], reverse=True)
    top_two = sorted_nums[:2]
    top_two_numbers = [number for number, _ in top_two]

    return top_two_numbers


print(topKFrequent([4, 3, 1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1, 2, 3, 2, 4, 1, 3, 5, 1, 2, 4, 2], 2))
print(topKFrequent([1], 1))
