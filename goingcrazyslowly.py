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
    if nums[0] == element:
        return 0 
    sub_index = searching_index(nums[1:], element)
    if sub_index == -1:
        return -1
    else:
        return 1 + sub_index

def count_occurences (nums,element):
    if not nums:
        return 0
    return (1 if nums[0] == element else 0) + count_occurences(nums[1:], element)

def is_palindrome (s:str) -> bool:
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
    
def sum_list (nums):
    if not nums:
        return 0
    else:
        return nums[0] + sum_list(nums[1:])
    
def Fibonacci (num: int) -> int:
    if num <= 1:
        return
    else:
        return Fibonacci(num -1) + Fibonacci(num-2)

def binary_search (nums, element, left, right):
    if left > right:
        return -1
    middle = (right +  left) // 2
    if nums[middle] == element:
        return middle
    elif nums[middle] < element:
        return binary_search(nums, element, middle + 1, right)
    else:
        return binary_search(nums, element, left, middle -1)
    
    

    

listt = [1,2,3,4,5,6,7]

print(is_palindrome("False"))
print(searching_index(listt, 5))

    

