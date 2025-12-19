#Write a program that displays a menu with options to square a number,
#cube a number, or exit. Use conditional statements to perform the 
#selected operation and repeat the menu until exit is chosen.

print("--- Number Options Menu ---")  #Title
while(True): #Runs again and again until we chose to exit
    print("1.Square of a number")
    print("2.cube of a Number")
    print("3.Exit")

    choice=int(input("Enter Your Choice (1/2/3)-")) #Asking user to select theie choice

    if choice==1:
        num=int(input("Enter a number-"))
        print(f"Square of a {num} is {num**2}") #square of a num
    elif choice==2:
        num=int(input("Enter a number-"))
        print(f"Cube of a {num} is {num**3}")#Cube of a num
    elif choice==3:
        print("Exiting Program. Thank you!") # we exit the program
        break
    else:
        print(f"{choice} is invalid.Please try again.") #only the choice is >3

