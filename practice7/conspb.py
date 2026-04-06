from insertpb import insert_from_console
from insertcsv import insert_from_csv
from updatepb import update_user
from selectpb import search
from deletepb import delete_user

def menu():
    while True:
        print("\n1. Insert (console)")
        print("2. Insert (CSV)")
        print("3. Update")
        print("4. Search")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_user()
        elif choice == "4":
            search()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            break

menu()