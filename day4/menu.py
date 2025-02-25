def technical_fest():
    print("Today is Technical Fest")

def cultural_fest():
    print("Today is Cultural Fest")

def sports_fest():
    print("Today is Sports Fest")

def ethnic_fest():
    print("Today is Ethnic Fest")

def main():
    while True:
        try:
            choice = int(input("1: Monday, 2: Tuesday, 3: Wednesday, 4: Thursday (-1 to Exit) Your choice: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice == -1:
            break
        match choice:
            case 1:
                technical_fest()
            case 2:
                cultural_fest()
            case 3:
                sports_fest()
            case 4:
                ethnic_fest()
            case _:
                print("Invalid choice entered")
    print("End of program")

if __name__ == "__main__":
    main()
