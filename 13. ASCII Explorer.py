print("="*30)
print("       ASCII EXPLORER")
print("="*30)
while True:
    print('''
    1. Character → ASCII
    2. ASCII → Character
    3. Exit''')
    print("="*30)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        char = input("Enter a character: ")
        print(f"ASCII Value: {ord(char)}")
    elif choice == 2:
        asc = int(input("Enter ASCII Value: "))
        if asc < 0 or asc > 127:
            print("Invalid ASCII Value")
        else:
            print(f"Character: {chr(asc)}")
    elif choice == 3:
        print("Thank you using our service.")
        break
    else:
        print("Invalid Input")