 allstudents=[]

def addstudent():
    print("Add student")
    while True :
        studentname=input("enter student's name")
        studentmarks=int(input("enter marks"))
        student={
            "name":studentname,
            "marks":studentmarks
            }
        allstudents.append(student)
        print(allstudents)
        choice=input("want to add one more student type ? yes or no ")
        if choice.lower()=="yes":
            pass
        else :
            print (allstudents,"record completed")
            break
    
def topper():
    print("Find topper")
    toppermarks=0
    toppername=[]
    for i in allstudents:
        if i["marks"]>toppermarks:
            toppermarks=i["marks"]
            toppername=[i["name"]]
        elif i["marks"]==toppermarks:
            toppername.append(i["name"])
    print("toppers are ",toppername)
    print("total marks obtained ",toppermarks)
            
def update():
    print("update student")
    name = input("enter students name")
    found = False
    for j in allstudents :
        if j["name"]==name:
            print(j)
            newmarks = int(input("enter new marks"))
            j["marks"]=newmarks
            print("updated student",j)
            found = True

    if found == False:
        print("Student not found")

    print("Updated list of all students:", allstudents)
    
    

def delete():
    print("delete student record")
    name=input ("enter student name")
    found=False
    for k in allstudents:
        if k["name"]==name:
            print(k)
            allstudents.remove(k)
            print("student record is deleted ")
            found=True
            break
    if found==False:
        print("student not found")
    
while True:
    print("\n","press 1 to add student")
    print("\n","press 2 to find topper")
    print("\n","press 3 to uppdate student")
    print("\n","press 4 to delete student")
    print("\n","press 5 to exit program")
    print("\n","press 6 to check current list")

    
    choice = input("enter your choice ")
    if choice=="1": 
        addstudent()
    elif choice=="2":
        topper()
    elif choice=="3":
        update()
    elif choice=="4":
        delete()
    elif choice=="5":
        print("program exited")
        break
    elif choice=="6":
        print(allstudents)
        break
    else:
        print("invalid choice")
        break

    
