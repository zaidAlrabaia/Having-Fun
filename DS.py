from typing import List
from collections import deque
nums1 = [1,2,3,4234234,523523,2,12341234,5,4,4,4]
nums2 = [4,5,6,1,234423244,234213423424,432432,4,4,4]


def intersection(list1, list2):
    result = []
    list1Len = len(list1)
    list2Len = len(list2)

    shorter = list1 if list1Len <= list2Len else list2
    longer = list1 if list1Len > list2Len else list2

    for num in shorter:
        if num in longer:
            result.append(num)
    final = set(result)
    return final

print(intersection(nums1,nums2))

class stack:
    def __init__(self):
        self._list = []

    def pop(self):
        node = self._list[-1]
        del self._list[-1]
        return node

    def push(self, val):
        self._list.append(val)

    def top(self):
        return self._list[-1]
    

def bs (list1: list[float]):
    evenNums = []
    oddNums = []
    for num in list1:
        if num % 2 == 0.0:
            evenNums.append(num)
        elif num % 2 != 0 and num > 10:
            oddNums.append(num)
    evenNums.sort()
    
    return tuple(evenNums, oddNums)

def bs2 (x:str) -> bool:
    myStack = []
    for i in x:
        if i == "(":
            myStack.append(i)
        elif len(myStack) == 0:
            return False
        else:
            myStack.pop()
    return len(myStack) == 0

def dq (tasks: List[str]):
    q = deque(tasks)
    while q:
        print("Processing: " + tasks.popleft())

def dic (sentence: str):
    myDict = {}
    for word in sentence.split():
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def idktbh (sList):
    Dict = {}
    for name, score in sList:
        if name is sList:
            Dict[name] += score
        else:
            Dict[name] = score





        

        

