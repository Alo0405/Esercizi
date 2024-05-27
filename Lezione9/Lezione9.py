class Member:
    def __init__(self, member_id: str, name: str, borrowed_books: list[Book]) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

class Book:
    def __init__(self, book_id: str, name: str, author: str, is_borrowed: bool) -> None:
        self.book_id = book_id
        self.name = name
        self.author = author
        self.is_borrwed = False
    def borrow()->None:

    

class Library:
       def __init__(self, books: dict[str, Book], members: dict[str, Member]) -> None:
        self.books = {}
        self.members = {}

#1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    previous = None
    current = head
    while current:
        nodo_successivo = current.next
        current.next = previous
        previous = current
        current = nodo_successivo
    
    result = []
    while previous:
        result.append(previous.val)
        previous = previous.next
    return result

#2

def word_break(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    appoggio = [False] * (len(s) + 1)
    appoggio[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if appoggio[j] and s[j:i] in word_set:
                appoggio[i] = True
                break
    return appoggio[len(s)]

#3

def valid_sudoku(board: list[list[str]]) -> bool:
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = [set() for _ in range(9)]
    
    for riga in range(9):
        for colonna in range(9):
            num= board[riga][colonna]
            if (num != '.'):
                box_index = (riga // 3) * 3 + (colonna // 3)
                
                if(num in row[riga]):
                    return False
                if(num in col[colonna]):
                    return False
                if(num in box[box_index]):
                    return False
                    
                    
                row[riga].add(num)
                col[colonna].add(num)
                box[box_index].add(num)
    return True

#4

def anagram(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())