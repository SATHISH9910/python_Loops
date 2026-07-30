def singleNumb(nums):
    ans =0
    for i in nums:
        ans^=i

    return ans

nums=[3,53,53,4,4]
print(singleNumb(nums))