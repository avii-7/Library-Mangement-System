import time
import sys

def loading():
    time.sleep(0.4)
    print('.', end='')
    time.sleep(0.4)
    print('.', end='')
    time.sleep(0.4)
    print('.', end='')
    time.sleep(0.4)
    print('.', end='')
    time.sleep(0.4)
    print('.', end='')


def date_func():
    pt = time.ctime(time.time())
    return str(pt)

def filefunc(user_name,book_name):
    with open('booklend.txt','a') as fp:
        fp.write(user_name + ' -- ' + book_name + ' -- ' + date_func() + '\n')

class Admin_Panel:
    def lend_book_users(self):
        with open('booklend.txt') as fp:
            print('\n\nLend Book Users:\n')
            print(fp.read())
        input('Press \'AnyKey + Hit Enter\' For Menu...\n')
    def clear_records(self):
        with open('booklend.txt','w') as fp:
            fp.write('')
        print('Clearing Records',end='')
        loading()
        print('Record Cleared Successfully')
        time.sleep(0.4)


class Library:
    def __init__(self,name,list):
        self.lib_name = name
        self.book_list = list
        self.lend_book_dict = {}   # {book_name:user}

    def display_books(self,yn):
        print('\n\nHere Are The Books\n')
        for index,items in enumerate(self.book_list,1):
            print(index,items)
        if(yn == 'Yes' ):
            while True:
                ch = input("Do Your Want To Lend Any Book (Y/N): ")
                ch = ch.upper()
                if(ch == 'Y'):
                    self.lend_books('No')
                    break
                elif(ch == 'N'):
                    time.sleep(0.3)
                    break
                else:
                    print('Invalid Input')
                    time.sleep(0.7)

    def lend_books(self,option):
        if (option == 'run_dis'):
            self.display_books('NO')
        while True:
            try:
                lb = int(input("Select Book To Lend: "))
                lend_book = self.book_list[lb - 1]
                break
            except Exception as e:
                print('Invalid Value !!')
        if lend_book in self.lend_book_dict:
            print(f"Books Is Already Lended By: {self.lend_book_dict[lend_book]}")
        else:
            user_name = input("Please Enter Your Name: ")
            self.lend_books_func(lend_book,user_name)
            self.remove_book(lb-1)
            filefunc(user_name,lend_book)
            print("\nYou Lended Book Successfully !!\nThank You....")
            time.sleep(0.7)

    def add_book(self):
        add_a_new_book = input("Enter The Name Of Book\n")
        if add_a_new_book in self.book_list:
            print('Sorry,We Already Have This Book.')
            time.sleep(0.5)
        else:
            self.book_list.append(add_a_new_book)
            print("Book Added Sucessfully !!")
            time.sleep(0.5)

    def return_book(self):
        return_a_book = input("Enter The Name Of Book\n")
        if return_a_book in self.lend_book_dict:
            del self.lend_book_dict[return_a_book]
            print("Book Returned Sucessfully !!")
            time.sleep(0.8)
        else:
            print("This Book Is Not From Our library.\nOr You Enetered Incorrect Details.")
            time.sleep(0.5)

    def remove_book(self,lb):
        del self.book_list[lb]

    def lend_books_func(self,lend_book,user_name):
        self.lend_book_dict[lend_book] = user_name

    def lend_book_dic_display(self):
        print("Lended Books Users Details")
        for key,value in self.lend_book_dict:
            print(key,value)

if __name__ == '__main__':
    name = input('--> Enter The Name Of Library.\n--> ')
    books = ['The Hobbits:The Two Tower', 'Dark Knight', 'Two States', 'Mr.India', 'The Cheems']
    print('Digital Library System Is Loading', end="")
    loading()
    print(f'\n\n\nWelcome To {name}')
    obj = Library(name,books)
    obj2 = Admin_Panel()
    while(True):
        choice = input("\nPress\n1.Display Books\n2.Lend Book\n3.Add Book\n4.Return Book\n5.AdminPanel\n6.Exit\nAnswer: ")
        if choice == '1':
            obj.display_books('Yes')
        elif choice == '2':
            obj.lend_books('run_dis')
        elif choice == '3':
            obj.add_book()
        elif choice == '4':
            obj.return_book()
        elif choice == '5':
            key = input('\n--> Enter The Password To Access Admin Panel\n--> ')
            if (key == 'familyislove'):
                while True:
                    a_choice = input('Press\n1.View Records\n2.Clear Records\nAnswer: ')
                    if a_choice == '1':
                        obj2.lend_book_users()
                        break
                    elif a_choice == '2':
                        obj2.clear_records()
                        break
                    else:
                        print('Invalid Input !!')
                        time.sleep(0.3)
                        print('\n')
            else:
                print('Wrong Passord !!')
                time.sleep(0.2)
                print('Going Back To Main Menu...')
                time.sleep(0.4)
        elif choice == '6':
            sys.exit()
        else:
            print("Invalid Input.\nTry Again...!")
            time.sleep(1.5)
