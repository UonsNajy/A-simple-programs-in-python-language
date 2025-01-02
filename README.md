
import os

# مكتبة الكتب
books = []

# حلقة القائمة
while True:
    # مسح الشاشة قبل عرض القائمة
    os.system("cls" if os.name == "nt" else "clear")
    
    print("Menu:")
    print("1. Add book")
    print("2. Check out book")
    print("3. Check in book")
    print("4. Show list")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        while True:
            # إضافة كتاب
            os.system("cls" if os.name == "nt" else "clear")  # مسح الشاشة
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            books.append({"ISBN": isbn, "Title": title, "Author": author, "Available": True})
            print(f"\nThe book '{title}' by {author} (ISBN: {isbn}) has been added to the catalog.")

            # سؤال المستخدم إذا كان يريد إضافة كتاب آخر
            another = input("\nDo you want to add another book (y/n): ").lower()
            if another == "y":
                continue
            elif another == "n":
                break
            else:
                print("Invalid input. Returning to the menu.")
                break

    elif choice == "2":
        # استعارة كتاب
        os.system("cls" if os.name == "nt" else "clear")  # مسح الشاشة
        isbn = input("Enter ISBN of the book to check out: ")
        found = False
        for book in books:
            if book["ISBN"] == isbn:
                if book["Available"]:
                    book["Available"] = False
                    print(f"\nThe book '{book['Title']}' has been checked out successfully!")
                else:
                    print(f"\nThe book '{book['Title']}' is already checked out.")
                found = True
                break
        if not found:
            print("\nBook not found!")
        input("\nPress Enter to return to the menu...")

    elif choice == "3":
        # إعادة كتاب
        os.system("cls" if os.name == "nt" else "clear")  # مسح الشاشة
        isbn = input("Enter ISBN of the book to check in: ")
        found = False
        for book in books:
            if book["ISBN"] == isbn:
                if not book["Available"]:
                    book["Available"] = True
                    print(f"\nThe book '{book['Title']}' has been checked in successfully!")
                else:
                    print(f"\nThe book '{book['Title']}' is already available in the catalog.")
                found = True
                break
        if not found:
            print("\nBook not found!")
        input("\nPress Enter to return to the menu...")

    elif choice == "4":
        # عرض القائمة
        os.system("cls" if os.name == "nt" else "clear")  # مسح الشاشة
        if books:
            print("List of books:")
            for book in books:
                status = "Available" if book["Available"] else "Not Available"
                print(f"ISBN: {book['ISBN']}, Title: {book['Title']}, Author: {book['Author']} - availabe: {status}")
        else:
            print("No books available!")
        input("\nPress Enter to return to the menu...")

    elif choice == "5":
        # الخروج من البرنامج
        os.system("cls" if os.name == "nt" else "clear")  # مسح الشاشة
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
        input("\nPress Enter to return to the menu...")
