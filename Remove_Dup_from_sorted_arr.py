def removeDuplicates(nums):

    if len(nums) == 0:
        return 0

    i = 0

    for j in range(1, len(nums)):

        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1


nums = [1,1,2,2,3,4,4]

k = removeDuplicates(nums)

print(k)
print(nums[:k])

# Time Complexity
# O(n)
# Space Complexity
# O(1)



