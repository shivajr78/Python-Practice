class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailbleBooks(self):
        print("Books Availble in Library are : ")
        for books in self.books:
            print("* " + books) # * are used for just bullet point only not any logic here

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} Book, Keep it Safe. And Return it with in 30 Days\n")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry,This Book either not Availble or has already been issued by someone else. So, Keep wait until the book is not Returned\n")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returing the Book. Hope you enjoyed Reading it!")



class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you wants to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you wants to return : ")
        return self.book

if __name__ == "__main__": # In main always right file name
    centralLibrary = Library(["Python","DSA","Maths.3","DE","DBMS","EE"])
    #centralLibrary.displayAvailbleBooks() #For print all availble books in library

    student = Student()

    while(True):
        welcomeMsg = '''\n******* Welcome To Central Library *******


        Please Choose an Option :
        1. List of all the Books
        2. Request a Book
        3. Add/Return a Book
        4. Exit the Library
        
        '''

        print(welcomeMsg)


        a = int(input("Enter the choice : "))
        if a == 1:
            centralLibrary.displayAvailbleBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("----------> Thanks! For Your Valuble Time With Us. <----------")
            exit()
        else:
            print("Invaild Choice!")





        