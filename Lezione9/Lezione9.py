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







#5

class Book:
    
    def __init__(self, book_id: str, title: str, author: str) -> None:
        
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        
        self.is_borrowed = True
    
    def return_book(self):
        
        self.is_borrowed = False

class Member:
    
    def __init__(self, member_id: str, name: str) -> None:

        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):

        if (book in self.borrowed_books):
            pass
        else: 
            self.borrowed_books.append(book)
            book.borrow()

    def return_book(self, book: Book):

        if (book in self.borrowed_books):   
            self.borrowed_books.remove(book)
            book.return_book()
        
class Library:
    
    def __init__(self) -> None:

        self.books = {}
        self.members = {}
    
    def add_book(self, book_id: str, title: str, author: str):

        book: Book = Book(book_id, title, author)
        self.books.setdefault(book_id, book)

    def register_member(self, member_id: str, name: str):

        member: Member = Member(member_id, name)
        self.members.setdefault(member_id, member)

    def borrow_book(self, member_id: str, book_id: str):

        self.members[member_id].borrow_book(self.books[book_id])
    
    def return_book(self, member_id: str, book_id: str):

        self.members[member_id].return_book(self.books[book_id])
    
    def get_borrowed_books(self, member_id: str) -> list:

        return self.members[member_id].borrowed_books

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

#6

class Account:
    def __init__(self, account_id: str)->None:
        self.account_id = account_id
        self.balance = 0
    def deposit(self, amount: float)->None:
        self.balance = self.balance + amount 
    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self)->None:
        self.accounts = {}
    def create_account(self, account_id)->None:
        
        account: Account = Account (account_id)
        self.accounts.update({account_id: account})
        return account
        
    def deposit(self, account_id, amount)-> None:
        self.accounts[account_id].deposit(amount)
    def get_balance(self, account_id):   
        self.accounts[account_id].get_balance()