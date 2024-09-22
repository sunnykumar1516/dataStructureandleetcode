def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 1
    checker = int(len(nums) / 2)
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i + 1]:
            count = count + 1
            print(count, checker)
            if count > checker:
                return int(nums[i])
        
        elif nums[i] != nums[i + 1]:
            count = 1

a = [3,2,3]
x = majorityElement(a)
print(x)