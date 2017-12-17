from binarySearchTree import *

tree = BinarySearchTree()
checkOptions = False
while checkOptions is False:
    try:
        option = int(input("================================= \n"
                           "What would you like to do? \n"
                           "enter 1 to insert \n"
                           "enter 2 to search \n"
                           "enter 3 to delete \n"
                           "enter 4 to print the tree \n"
                           "enter 5 to quit \n"
                           "================================= \n"))

        if option == 1:
            try:
                s = input("Enter a number or \n" +
                          "Enter multiple numbers using a spaces between each number: ")
                lst = s.split()

                for x in lst:
                    tree.insert(float(x))
            except ValueError:
                print("**********************************")
                print("Error: the input must be a number")
                print("**********************************")

        if option == 2:
            try:
                s = float(input("Enter a number to search: "))
                print("Conclusion: " + str(s) + " " + str(tree.search(s)))
            except ValueError:
                print("**********************************")
                print("Error: the input must be a number")
                print("**********************************")

        if option == 3:
            try:
                s = float(input("Enter a number to delete: "))
                tree.delete(s)
                print("The item has been deleted")
            except ValueError:
                print("**********************************")
                print("Error: the input must be a number")
                print("**********************************")

        if option == 4:
            for x in tree:
                print(x)

        if option == 5:
            print("Good Bye")
            checkOptions = True
    except ValueError:
        print("**********************************")
        print("Error: The value must be an integer")
        print("**********************************")
