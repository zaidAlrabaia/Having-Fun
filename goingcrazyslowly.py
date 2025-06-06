def array_sum (nums) -> float:
    if len(nums) == 0:
        return 0
    
    return nums[0] + array_sum(nums[1:])

def maximus(nums) -> float:
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], maximus(nums[1:]))

def count_even(nums):
    if not nums:
        return 0
    if nums[0] % 2 == 0:
        return 1 + count_even(nums[1:])
    else:
        return count_even(nums[1:])
   
def searching(nums, element):
    if not nums:
        return False
    if nums[0] == element:
        return True
    return searching(nums[1:], element)

def searching_index (nums, element): #Fucked up this one
    if not nums:
        return -1
    if nums[0] != element:
        return 1 + searching_index(nums[1:], element)
    if nums[0] == element:
        return 0 

    

