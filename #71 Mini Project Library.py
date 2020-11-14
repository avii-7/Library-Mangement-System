import time
import sys

def func():
    pt = time.ctime(time.time())
    return str(pt)

def filefunc(user_name,book_name):
    with open('booklend.txt','a') as fp:
        fp.write(user_name + ' -- ' + book_name + ' -- ' + func() + '\n')

class Library:
    books = ['The Hobbits:The Two Tower','Dark Knight','Two States','Mr.India','The Cheems']
    lend_books_dict = {}

    def display_books(self,yn):
        for index,items in enumerate(self.books,1):
            print(index,items)
        if(yn == 'Yes' ):
            ch = input("Do Your Want To Lend Any Book (Y/N): ")
            ch = ch.upper()
            if(ch == 'Y'):
                self.lend_books()
            elif(ch == 'N'):
                pass
            else:
                print('Invalid Input')

    def lend_books(self):
        print("\nHere Are Books\n")
        self.display_books('NO')
        lb = int(input("\nEnter Your Choice Here: "))
        lend_book = self.books[lb - 1]
        if lend_book in self.lend_books_dict:
            print(f"Books Is Already Lended By: {self.lend_books_dict[lend_book]}")
        else:
            user_name = input("Please Enter Your Name: ")
            self.lend_books_func(lend_book,user_name)
            filefunc(user_name,lend_book)
            #self.remove_book(lb-1)
            print("You Lended Book Successfully...\nThank You")



    @classmethod
    def add_book(cls):
        add_a_new_book = input("Enter The Name Of Book\n")
        cls.books.append(add_a_new_book)
        print("Book Added Sucessfully !!")

    @classmethod
    def return_book(cls):
        return_a_book = input("Enter The Name Of Book\n")
        if return_a_book in cls.lend_books_dict:
            del cls.lend_books_dict[return_a_book]
            print("Book Returned Sucessfully !!")
        else:
            print("This Book Is Not From Our library.\nOr You Enetered Incorrect Details.")

    @classmethod
    def remove_book(cls,lb):
        del cls.books[lb]

    @classmethod
    def lend_books_func(cls,lend_book,user_name):
        cls.lend_books_dict[lend_book] = user_name

    def lend_book_dic_display(self):
        print("Lended Books Users Details")
        for key,value in self.lend_books_dict:
            print(key,value)

if __name__ == '__main__':
    obj = Library()
    while(True):
        choice = input("\nPress\n1.Display Books\n2.Lend Books\n3.Add Book\n4.Return Book\n5.Exit\nAnswer: ")
        if choice == '1':
            obj.display_books('Yes')
        elif choice == '2':
            obj.lend_books()
        elif choice == '3':
            Library.add_book()
        elif choice == '4':
            Library.return_book()
        elif choice == '5':
            sys.exit()
        else:
            print("Invalid Input.\nTry Again...!")





