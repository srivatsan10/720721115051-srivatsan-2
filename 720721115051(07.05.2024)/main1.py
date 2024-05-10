def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target)) 
nums = [3, 3]
target = 6
print(twoSum(nums, target)) 
