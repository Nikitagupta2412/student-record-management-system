library=[]
def addbook():
    print (" Add a new book ")
    while True:
        bookname=input("enter book name")
        authorname=input("enter author name")
        curentstatus=input("enter current status")
        bookdetails={
            "Book":bookname,
            "Author":authorname,
            "Availability status":True
            }
        library.append(bookdetails)
        print(library,"book added successfully")
        choice=input("want to add more?")

        if choice.lower()!= "yes":
            break
        


def searchbook():
    print("search about a book")
    name=input("enter book name to search")
    found=False
    for i in library:
        if i["Book"]==name:
        print("book founded")
        print(i)
        found=True
        break

        else:
            print("book not founded")
            found=False

def availability():
    print("check availability status")
    name=input("enter name of the book you want to check availability of ")
    for j in library:
        if j["Availability status"]==True:
            print("book can be isued")
            j["Availability status"]==False
            break
            
        elif j["Availability status"]==False:
            print('someone already borrowed it ')

def returnbook():
    print("return your book")
    name=input("enter book name you borrowed")
    for k in library:
        if k["Book"]==name:
            print("book returned successfully")
            k["Availability status"]=True
            break
        else:
            print("No book found of this name")

def deletebook():
    print("want to delete a book")
    name =input ("enter the name of book you want to delete")
    for l in library:
        if l["Book"]==name:
            library.remove(l)
            print('book deleted successfully from the library')
        else:
            print("no book found with this name")

while True:
    print("\n","press 1 to add book")
    print("\n","press 2 to search book")
    print("\n","press 3 to check availability")
    print("\n","press 4 to delete book")
    print("\n","press 5 to exit program")
    print("\n","press 6 to check current library")

    
    choice = input("enter your choice ")
    if choice=="1": 
        addbook()
    elif choice=="2":
        searchbook()
    elif choice=="3":
        availability()
    elif choice=="4":
        deletebook()
    elif choice=="5":
        print("program exited")
        break
    elif choice=="6":
        print(library)
        break
    else:
        print("invalid choice")
        break

    




    
            
    
