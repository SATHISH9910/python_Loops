
def twoSum(nums, target):

    seen = {}

    for i in range(len(nums)):

        need = target - nums[i]

        if need in seen:
            return [seen[need], i]

        seen[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))




# Time Complexity
# O(n)
# Space Complexity
# O(n)