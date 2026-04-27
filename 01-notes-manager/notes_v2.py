# Notes Manager CLI

while True:
    print("---Notes Manager---")
    print("1. Add Note")
    print("2. View Note")
    print("3. Delete Entire Note")
    print("4. Search Note")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_text = input("Enter your note: ").strip()
        with open("notes.txt","a") as f:
            f.write(add_text + "\n")
            print("Note added! \n")
    elif choice == "2":
        with open("notes.txt","r") as f:
            print(f.read())
    elif choice == "3":
        with open("notes.txt","w") as f:
            pass
        print("Note deleted!\n")
    elif choice == "4":
        search = input("Enter a word to search: ")
        with open("notes.txt","r") as f:
            content = f.read()
            if content in f:
                print(f"Found '{search}' in the note!\n")
            else:
                print(f"'{search}' not found in the note!\n")
    elif choice == "5":
        print("GoodBye!")
        break
    else:
        print("Invalid Choice! Try again.\n")
