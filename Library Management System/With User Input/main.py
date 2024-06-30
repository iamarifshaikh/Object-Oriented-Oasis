import csv

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

class Book:
    def __init__(self,title: str, author: str, copies:int):
        self.title = title
        self.author = author
        self.copies = copies
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.copies}')"
    
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
    
class Library:
    books = []
    members = []
    
    def __init__(self, name: str):
        self.name = name
    
    def registerMember():
        pass
    
    def borrowBook():
        pass
    
    def returnBook():
        pass
    
    def __repr__(self) -> str:
        return f"Library('{self.name}', Book:{self.books}, Member:{self.members})"

def main():                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    library = Library()
    while True:
        print(art)
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
            pass
        
        elif choice == "2":
            pass
    
        elif choice == "3":
            pass
        
        elif choice == "4":
            pass
        
        elif choice == "5":
            pass
        
        elif choice == "6":
            pass
        
        elif choice == "7":
            pass
        
        elif choice == "8":
            pass
        
        elif choice == "9":
            break
        
        else:
            print("Invalid Choice")
            
if __name__ == "__main__":
    main()