class Heap:
    def __init__(self):
        self.heap = []

    def leftChildIndex(self, index):
        return(index * 2 + 1)
    
    def rightChildIndex (self, index):
        return (index * 2 + 2)
    
    def parentIndex(self,index):
        return (index - 1)// 2
    
    def peek(self):
        return self.heap[0]
    
    def swap(self,curIndex, parentIndex):
        self.heap[curIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[curIndex]
    
    def bubbleUp(self, index):
        while index > 0:
            parent = self.parentIndex(index)
            if self.heap[index] < self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break
    
    def push(self, element):
        self.heap.append(element)
        self.bubbleUp(len(self.heap) -1)
    
    def bubbleDown (self, root):
        heapSize = len(self.heap)

        while True:
            smallest = root
            rci = self.rightChildIndex(root)
            lci = self.leftChildIndex(root)

            if lci < heapSize and self.heap[lci] < self.heap[smallest]:
                smallest = lci
               
            if rci < heapSize and self.heap[rci] < self.heap[smallest]:
                smallest = rci
                
            
            if smallest == root:
                break

            self.swap(root,smallest)
            root = smallest
    
    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty")
        min_val = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.bubbleDown(0)


        return min_val
    
    def heapify(self, stupidList):
        self.heap = stupidList

        size = len(self.heap)
        lastParentIndex = (size // 2) - 1
        for i in range(lastParentIndex, -1, -1 ):
            self.bubbleDown(i)
        


def bubbleDis(self, index):
    smallest = index
    leftChildIndex = index * 2 + 1
    rightChildIndex = index * 2 + 2
    size = len(self.heap)
    
    while True:
        smallest = index

        if leftChildIndex < size and self.heap[leftChildIndex] > self.heap[smallest]:
            smallest = leftChildIndex
        
        if rightChildIndex < size and self.heap[rightChildIndex] > self.heap[smallest]:
            smallest = rightChildIndex
        
        if smallest == index:
            break
        
        self.swap(index, smallest)
        index == smallest
    


def ikims(nums):
    stack = []
    result = []
    size = len(nums)
    index = 0

    while stack:
        while index < size:
            if nums[index * 2 + 1]:
                stack.append(nums[index * 2 + 1])
                index = index * 2 + 1
            else:
                node = stack.pop()
                result.append(node)
                index = index * 2 + 2
    return result

def divide (a, b):
    try:
        answer = a / b
    except ZeroDivisionError:
        print("You cant divide by zero")
    except (TypeError, ValueError):
        print("Inputs must be numbers")
    
    return answer

def check_age (age):
    if age < 0:
        raise ValueError ("Age cannot be negative")
    if age >= 18:
        print("Allowed")
    if age < 18: 
        print("denied")

class TooMuchError(Exception):
    def __init__(self):
        print("Too many items")

square = lambda x : x*x
fullName = lambda x, y: x + " " + y

print(fullName("zaid", "eyad"))



