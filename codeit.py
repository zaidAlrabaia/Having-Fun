def maximumaceragesubarrayI(nums, k) -> float:
    max = float("-inf")
    cur_avg = 0

    for num in range(k):
        cur_avg += nums[num]
    max = cur_avg/k
    
    for num in range(k, len(nums)):
        cur_avg -= nums[num-k]
        cur_avg += nums[num]
        if cur_avg/k > max:
            max = cur_avg/k
    return max

def LSWSK (nums, k):
    maxLen = 0 
    left = 0
    cur_sum = 0
    for r in range (len(nums)):
        cur_sum += nums[r]

        while cur_sum > k:
            cur_sum -= nums[left]
            left += 1
            
        if (r - left + 1) > maxLen:
            maxLen = r - left + 1
    return maxLen

def cwmw(nums):
    max_height = float("-inf")
    left = 0
    right = len(nums) - 1
    
    while left < right:
        cur_height = min(nums[left], nums[right]) * (right - left)
        if cur_height > max_height:
            max_height = cur_height
        else:
            if nums[left] > nums[right]:
                right -= 1
            else:
                left += 1
    return max_height

def sirsa (nums, k):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == k:
            return middle
        
        elif nums[middle] >= nums[left] or k < nums[left]:
            if k > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        else:
            if k < nums[middle]:
                right = middle - 1
            else:
                if k > nums[right] or k < nums[middle]:
                    right = middle - 1 
                else:
                    left = middle + 1
    return None    


    




