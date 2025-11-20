#loop it will keep going forever until we say stop
while True:
    # we are just saying here is the menu \n its to make it look nice
    print("\nmenu:")
    # these are the three choices
    print("1) say hello")
    print("2) add two numbers")
    print("3) quit")


# to ask your about your choice
    choice= input("choose 1,2 or3:")
    if choice == "1":
        print("hello!")
    elif choice == "2":
        a = float(input("input first number: "))
        b = float(input("input second number: "))
        print("The sum is: a + b")
    elif choice == "3":
        print("goodbye!")
        # to stop the loop
        break
    else:
        print("that is not 1, 2 or 3. please try again.")
        #this is in case you typed something else