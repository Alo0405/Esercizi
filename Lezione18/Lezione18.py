#1
import math

def safe_sqrt(number: int):
    if number >= 0:
        return math.sqrt(number)
    else:
        raise Exception('il numero è negativo')

#2
class InvalidPasswordError(Exception):
    'invalid password'

def validate_password(password):
    maiusc: int = 0
    spec_char: int = 0
    show_spec_char: str = '#@\'[]()+*!$£&?^'

    for char in password:

        if (char.isupper() == True):
            maiusc += 1

        if (char in show_spec_char):
            spec_char += 1

    if (len(password) >= 20) and (maiusc >= 3) and (spec_char >= 4):
        print('password is valid')
    else:
        raise InvalidPasswordError

#3

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

############################################################

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
























