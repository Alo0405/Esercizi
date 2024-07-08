def is_valid_parenthesis(s: str) -> bool:
    
    queue: list =[]
    for read in s:
        queue.append(read)
    ptr: int = 0
    cso: int = 0
    csc: int = 0
    cco: int = 0
    ccc: int = 0

    while (ptr < len(queue)):
        if queue[ptr] == '(':
            ptr += 1
        elif queue[ptr] == '[':
            ptr += 1
            cso += 1
        elif queue[ptr] == '{':
            ptr += 1
            cco += 1
        elif (queue[ptr] == ')') and (queue[ptr - 1] == '('):
            ptr += 1
        elif (queue[ptr] == ']') and (queue[ptr - 1] == '[') or (cso > csc):
            ptr += 1
            csc += 1
        elif (queue[ptr] == '}') and (queue[ptr - 1] == '{') or (cco > ccc):
            ptr += 1
            ccc += 1
        else:
            return False
        
        if (ptr == len(queue)):
            return True   
    if (ptr == len(queue)):
            return True
    

#2


class Queue:
    pass


class MyStack:
    def __init__(self) -> None:
        self.stack = []
    def push(self, x : int) -> None:
        self.stack.append(x)
    def pop(self) -> None:
        element = self.stack.pop()
        return element
    def top(self) -> None:
        return self.stack[-1]
    def empty(self) -> None:
        return len(self.stack) == 0
    

#3 


def merge(nums1, m, nums2, n):
    while m < len(nums1):
        nums1.pop()
    while n < len(nums2):
        nums2.pop()
    if m == 0:
        nums1.clear()
    if n == 0:
        nums2.clear()
    nums1 =+ nums2
    return nums1.sort()

