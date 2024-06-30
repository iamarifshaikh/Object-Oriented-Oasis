import csv

# ASCII art for the library system
art = r"""
          _              _          _               _           _                   _    _        _   
        _\ \           /\ \       / /\            /\ \        / /\                /\ \ /\ \     /\_\ 
       /\__ \          \ \ \     / /  \          /  \ \      / /  \              /  \ \\ \ \   / / / 
      / /_ \_\         /\ \_\   / / /\ \        / /\ \ \    / / /\ \            / /\ \ \\ \ \_/ / /  
     / / /\/_/        / /\/_/  / / /\ \ \      / / /\ \_\  / / /\ \ \          / / /\ \_\\ \___/ /   
    / / /            / / /    / / /\ \_\ \    / / /_/ / / / / /  \ \ \        / / /_/ / / \ \ \_/    
   / / /            / / /    / / /\ \ \___\  / / /__\/ / / / /___/ /\ \      / / /__\/ /   \ \ \     
  / / / ____       / / /    / / /  \ \ \__/ / / /_____/ / / /_____/ /\ \    / / /_____/     \ \ \    
 / /_/_/ ___/\ ___/ / /__  / / /____\_\ \  / / /\ \ \  / /_________/\ \ \  / / /\ \ \        \ \ \   
/_______/\__\//\__\/_/___\/ / /__________\/ / /  \ \ \/ / /_       __\ \_\/ / /  \ \ \        \ \_\  
\_______\/    \/_________/\/_____________/\/_/    \_\/\_\___\     /____/_/\/_/    \_\/         \/_/                                                                                                       
"""

# Book class to represent a book in the library
class Book:
    def __init__(self,title: str, author: str, copies:int):
        self.title = title
        self.author = author
        self.copies = copies
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.copies}')"
    
# Member class to represent a library member
class Member:
    borrow = []
    def __init__(self,id: int,name: str):
        self.id = id
        self.name = name
        
    def borrowBook(self,title: str) -> str:
        self.borrow.append(title)
    
    def returnBook(self,title: str) -> str:
        self.borrow.remove(title)

    def __repr__(self) -> str:
        return f"Member('{self.id}, '{self.name}', '{self.borrow}')"
    
# Library class to represent the library system
class Library:  
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.members = []
    
    def addBook(self, book:Book):
        self.books.append(book)
    
    def registerMember(self, member:Member):
        self.members.append(member)
    
    def borrowBook(self, book_title: str, memberId:int):
        print(f"Searching for book: {book_title}")
        print(f"Current books: {self.books}")
        book = next((b for b in self.books if b.title.lower() == book_title.lower()), None)
        print(f"Found book: {book}")
        member = next((m for m in self.members if m.id == int(memberId)), None)
        print(f"Found member: {member}")
        
        if book and member and book.copies > 0:
            member.borrowBook(book.title)
            book.copies -= 1
            return f"Book '{book_title}' has been borrowed by member '{member.name}'"
        else:
            return f"Book '{book_title}' is not available"
    
    def returnBook(self):
        pass
    
    @classmethod
    def FromCSV(cls):
        # Create a new instance of Library
        library = cls("My Library")
        
        # Read books from the CSV file and add them to the library
        with open("book.csv",'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                library.addBook(Book(row['title'],row['author'],row['copies']))
            
            # Other alternative instead of using for loops to read books and add them to the library by using list comprehension
            # [library.addBook(Book(row['title'], row['author'], row['copies'])) for row in reader]
        
        with open("member.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                library.registerMember(Member(row['id'], row['name']))
                
            # Other alternative instead of using for loops to read members and add them to the library but by using list comprehension    
            # [library.registerMember(Member(row['id'],row['name'])) for row in reader]
    
    @staticmethod
    def writeToCSV(books,members):
        with open("F:/Object-Oriented-Oasis/Library Management System/With User Input/book.csv","w", newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["title","author","copies"])
            writer.writeheader()
            for book in books:
                writer.writerow({"title":book.title, "author":book.author, "copies":book.copies})
        
        with open("F:/Object-Oriented-Oasis/Library Management System/With User Input/member.csv","w",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["id","name"])
            writer.writeheader()
            for member in members:
                writer.writerow({"id":member.id,"name":member.name})
    
    def __repr__(self) -> str:
        return f"Library('{self.name}', Book:{self.books}, Member:{self.members})"

def main():                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    library = Library("My Library")
    print(art)
     
    # Main menu loop
    while True:
        print("\nMenu")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Update Book")
        print("6. Update Member")
        print("7. Display Library")
        print("8. Write to CSV")
        print("9. Exit\n")
        
        choice = input("Enter Your Choice:")
        
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input(f"Enter the author name of the '{title}': ")
            copies = int(input(f"Enter the copies you have for '{title}' by '{author}' : "))
            library.addBook(Book(title,author,copies))
            
        elif choice == "2":
            id = int(input("Enter the id: "))
            name = input("Enter the name of a member: ")
            library.registerMember(Member(id,name))
    
        elif choice == "3":
            title = input("Enter the title of the book you want to borrow: ")
            memberId = int(input("Enter the member id: "))
            print(library.borrowBook(title, memberId))
        
        elif choice == "4":
            title = input("Enter the title of the book you want to return: ")
            memberId = int(input("Enter the member id: "))
            print(library.returnBook(title, memberId))
            
        elif choice == "5":
            pass
        
        elif choice == "6":
            pass
        
        elif choice == "7":
            print(library)
        
        elif choice == "8":
            library.writeToCSV(library.books,library.members)
            print("Data written to the CSV file.")
        
        elif choice == "9":
            break
        
        else:
            print("Invalid Choice")
            
if __name__ == "__main__":
    main()