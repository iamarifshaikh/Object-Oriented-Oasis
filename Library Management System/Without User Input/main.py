import csv

class Book:
    def __init__(self, title:str, author:str, copies:int):
        self.title = title
        self.author = author
        self.copies = copies
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.copies}')"
    
class Member:
    borrow = []
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        
    def borrowBook(self,title:str) -> str:
        self.borrow.append(title)
    
    def returnBook(self,title:str) -> str:
        self.borrow.remove(title)
        
    def __repr__(self):
        return f"Member('{self.id}', '{self.name}', {self.borrow})"
    
class Library:
    books = []
    members = []
    
    def __init__(self,name:str):
        self.name = name
    
    def addBooks(self, book:Book):
        self.books.append(book)
    
    def registerMember(self, member:Member):
        self.members.append(member)
        
    def borrowBook(self, book_title: str, memberId:int):
        book = next((b for b in self.books if b.title == book_title),None)
        member = next((m for m in self.members if m.id == memberId),None)
        
        if book and member and book.copies > 0:
            member.borrow_book(book_title)
            book.copies -=1
            return f"Book '{book_title}' has been borrowed by member '{member.name}'"
        else:
            return f"Book '{book_title}' is not available"
        
    def returnBook(self,book_title:str, memberId:int):
        book = next((b for b in self.books if b.title == book_title),None)
        member = next((m for m in self.members if m.id == memberId),None)
        
        if book and member and book_title in member.borrowed_books:
            member.return_book(book.title)
            book.copies += 1
            return f"Book '{book_title}' has been returned by member '{member.name}'"
        else:
            return f"Book '{book_title}' is not borrowed by member '{member.name}'"
            
    @classmethod    
    def FromCSV(cls):
        # Create a new instance of Library
        library = cls("My Library")
        
        # Read books from the CSV file and add them to the library
        with open("book.csv",'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                library.addBooks(Book(row['title'],row['author'],int (row['copies'])))
            # Other alternative instead of using for loops to read books and add them to the library by using list comprehension
            # [library.add_book(Book(row['title'], row['author'], int(row['copies']))) for row in reader]
            
        # Read members from the CSV file and add them to the library
        with open("member.csv",'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                library.registerMember(Member(int(row['id']),row['name']))  
            # Other alternative instead of using for loops to read members and add them to the library but by using list comprehension
            # [library.registerMember(Member(int(row['id']),row['name'])) for row in  reader]  
        
        # Return the fully initialized Library instance
        return library
    
    def writeToCSV(self):
        # Write books to CSV
        with open('book.csv','w',newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'author', 'copies'])
            writer.writeheader()
            for book in self.books:
                writer.writerow({"title": book.title, "author": book.author,"copies": book.copies})

        # Write members to CSV
        with open('member.csv','w',newline="") as file:
            writer = csv.DictWriter(file,  fieldnames=["id","name"])
            writer.writeheader()
            for member in self.members:
                writer.writerow({"id": member.id, "name": member.name})
                    
    def __repr__(self) -> str:
        return f"Library('{self.name}', Books: {self.books}, Members: {self.members})"

if __name__ == "__main__":
    
    #Initialize library
    library = Library.FromCSV()
    
    # Register a new memeber in library
    new_member = Member(1,"Arif")
    library.registerMember(new_member)
    
    # Add new books to library
    new_book = Book("The Emperor Of All Maladies","Siddhartha Mukherjee", 5)
    library.addBooks(new_book)
    
    # write the current state library to csv file
    library.writeToCSV()
    
    # Print library details
    print(library)