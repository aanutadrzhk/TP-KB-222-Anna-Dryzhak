<<<<<<< HEAD

=======
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
>>>>>>> d60b2a07cd248b17cc22ba954007576911d3c954
list = [
    {"name":"Bob", "phone":"0631234567", "age":"18", "gender":"man"},
    {"name":"Emma", "phone":"0631234567", "age":"20", "gender":"woman"},
    {"name":"Jon",  "phone":"0631234567", "age":"23", "gender":"man"},
    {"name":"Zak",  "phone":"0631234567", "age":"19", "gender":"man"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Age is " + elem["age"] + ", Gender is " + elem["gender"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    gender = input("Please enter student gender: ")
    newItem = {"name": name, "phone": phone, "age": age, "gender": gender}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    for item in list:
        if name == item["name"]:
            print("Student found. Please update the information:")
            new_name = input("Please enter new name: ")
            new_phone = input("Please enter new phone number: ")
            new_age = input("Please enter new age: ")
            new_gender = input("Please enter new gender: ")

            item["name"] = new_name
            item["phone"] = new_phone
            item["age"] = new_age
            item["gender"] = new_gender

            list.sort(key=lambda x: x["name"])
            print("Student information updated.")
            return

    print("Student not found.")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit")
                break
            case _:
                print("Wrong chouse")


<<<<<<< HEAD
main()
=======
main()
>>>>>>> d60b2a07cd248b17cc22ba954007576911d3c954
