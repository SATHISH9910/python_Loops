def misssingNumbers(nums):
    n = len(nums)

    total = n*(n+1)//2
    actual = sum(nums)
    return total-actual

nums=[3,0,1]
print(misssingNumbers(nums))