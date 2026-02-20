class LibrarySystem:
    def __init__(self):
        self.members = {}
        self.books = {}
        self.books_quantity = {}
        self.borrowing = {}
    # adding a new member
    def add_member(self):
        while True:
            print("Adding a new member:", end="\n")
            member_name = input("Please enter a new member name:\n")
            member_id = 1001
            if len(self.members) > 0:
                member_id = list(self.members)[-1] + 1
            self.members[member_id] = member_name
            # print(self.members)
            print("Member [" + member_name + "] has been created with member ID: [", member_id, "]")
            sub_opt = input("Would you like to [a]dd a new member or go-[b]ack to the previous menu?\n ")
            if sub_opt == "a":
                continue
            if sub_opt == "b":
                break
            else:
                break

    # adding a new book
    def add_book(self):
        print("Adding a new book:")
        while True:
            book_name = input("Please enter a new book title:\n")
            if book_name in self.books.values():
                print("Book already exists")
                while (True):
                    for bid, bname in self.books.items():
                        if book_name == bname:
                            print("Book Id:", bid)
                            print("Book Title", bname)
                            print("Number of copies: ", self.books_quantity[bid])
                    break
            else:
                book_id = 1
                if len(self.books) > 0:
                    book_id = list(self.books)[-1] + 1
                self.books_quantity[book_id] = int(input("Enter the number of copies: \n"))
                print("New book added")
                self.books[book_id] = book_name
                # print(self.books)
                print("Book ID:" + str(book_id))
                print("Book Title: ", book_name)
                print("Number of copies: ", self.books_quantity[book_id])
            sub_opt = input("Would you like to [a]dd a new book or go-[b]ack to the previous menu?\n ")
            if sub_opt == "a":
                continue
            if sub_opt == "b":
                break
            else:
                break

    # function to tackle borrowing process
    def borrowingProcess(self):
        while True:
            # loop to check for member id
            while True:
                member_id = int(input("Please enter a valid member ID:\n"))
                if member_id in self.members:
                    break
                else:
                    print("Member does not exist.")
            name = self.members[member_id]
            # loop to check for book id
            while True:
                book_id = int(input("Please enter a valid book ID for borrowing by member [" + name + "]:\n"))
                if book_id in self.books:
                    break
                else:
                    print("Book does not exist.")
            if self.books_quantity[book_id] > 0:
                if member_id in self.borrowing.keys():
                    if book_id in self.borrowing[member_id]:
                        print("Sorry!!! Book titled [", self.books[book_id], "] is already borrowed by the member.",
                              self.members[member_id])
                    else:
                        self.borrowing[member_id].append(book_id)
                        self.books_quantity[book_id] -= 1
                        print("*** Borrowing processed successfully***")
                        print("Member:", self.members[member_id])
                        print("Borrowed Book title: ", self.books[book_id])
                        print("Number of books remaining:", self.books_quantity[book_id])
                else:
                    self.borrowing[member_id] = [book_id]
                    self.books_quantity[book_id] -= 1
                    print("*** Borrowing processed successfully***")
                    print("Member:", self.members[member_id])
                    print("Borrowed Book title: ", self.books[book_id])
                    print("Number of books remaining:", self.books_quantity[book_id])
            else:
                print("Sorry!!! Book titled [", self.books[book_id], "] is currently not available for borrowing.")

            sub_opt = input("Would you like to [P]rocess a new borrowing or go-[b]ack to the previous menu?\n")
            if sub_opt == "p":
                continue
            if sub_opt == "b":
                break
            else:
                break

    # function to tackle returning process
    def returningProcess(self):
        while True:
            # loop to check for member id
            while True:
                member_id = int(input("Please enter a valid member ID:\n"))
                if member_id in self.members:
                    break
                else:
                    print("Member does not exist.")
            name = self.members[member_id]
            # loop to check for book id
            while True:
                book_id = int(input("Please enter a valid book ID returned by: [" + name + "]:\n"))
                if book_id in self.books:
                    break
                else:
                    print("Book does not exist.")
            if self.books_quantity.get(book_id, 0) > 0:
                if book_id in self.borrowing[member_id]:
                    print("*** Returning processed successfully ***")
                    print("Member:", self.members[member_id])
                    print("Book returned:", self.books[book_id])
                    print("After returning, number of books [", self.books[book_id], "] available in stock:",
                          self.books_quantity[book_id]+1)
                    self.books_quantity[book_id] += 1
                    self.borrowing[member_id].remove(book_id)
                else:
                    print("Book was not borrowed.")
            else:
                print("Book is not available for borrowing.")

            sub_opt = input("Would you like to [p]rocess a new returning or go-[b]ack to the previous menu?\n ")
            if sub_opt == "p":
                continue
            if sub_opt == "b":
                break
            else:
                break

    # view member status
    def member_status(self):
        while (True):
            # loop to check for member id
            while (True):
                member_id = int(input("Please enter a valid member ID:\n"))
                if member_id in self.members:
                    break
                else:
                    print("Member does not exist.")
            print("Member [", member_id, "]", self.members[member_id])
            bkk = self.borrowing.get(member_id, [])
            print("Borrowed Books:", end=" ")
            if len(bkk) > 0:
                for j in bkk:
                    print(self.books[j], end=" ")
            else:
                print("None")
            sub_opt = input("\nWould you like to view a new member’s [s]tatus or go-[b]ack to the previous menu?\n ")
            if sub_opt == "s":
                continue
            if sub_opt == "b":
                break
            else:
                break

    # view book status
    def book_status(self):
        while (True):
            # loop to check for book id
            while (True):
                book_id = int(input("Please enter a valid book ID:\n"))
                if book_id in self.books:
                    break
                else:
                    print("Book does not exist.")
            c = 0
            while (True):
                print("Book [", book_id, "]", self.books[book_id])
                print("Available number of copies:", self.books_quantity[book_id])
                print("List of Members borrowing:", end=" ")
                for key, value in self.borrowing.items():
                    if book_id in value:
                        print(self.members[key], end=" ")
                        c = c + 1
                # print("List of Members borrowing:", borrowing[member_id])
                if c == 0:
                    print("None", end=" ")
                print(end="\n")
                break
            sub_opt = input("Would you like to view a new book [s]tatus or go-[b]ack to the previous menu?\n ")
            if sub_opt == "s":
                continue
            if sub_opt == "b":
                break
            else:
                break

    # Main menu function
    def run_code(self):
        while True:
            print("Main Menu - please select an option:")
            print("1) Add new member")
            print("2). Add new book")
            print("3) Process borrowing")
            print("4) Process returning")
            print("5) View member status")
            print("6) View book status")
            print("7) Quit")
            option = int(input(" "))
            if option>7 or option<1:
                print("Value must be between 1 and 7")
            else:
                if option == 1:
                    self.add_member()
                elif option == 2:
                    self.add_book()
                elif option == 3:
                    self.borrowingProcess()
                elif option == 4:
                    self.returningProcess()
                elif option == 5:
                    self.member_status()
                elif option == 6:
                    self.book_status()
                elif option == 7:
                    print("Thanks for using ITECH5403 Library System!")
                    break


print("------------------------------------------------")
print("-------Welcome to ITECH5403 Library System------")
print("------------------------------------------------")
library_system = LibrarySystem()  # object creation
library_system.run_code()  # access main menu