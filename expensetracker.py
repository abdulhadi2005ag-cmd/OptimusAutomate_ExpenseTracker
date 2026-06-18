from expenses import add_expense, view_expenses, delete_expense, monthly_summary, CATEGORIES
#function for menu
def show_menu():
    print("----EXPENSE TRACKER----")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. Monthly Summary")
    print("5. Exit")
#function to get the category
def get_category():
    print("categories:")
    print("1.Food  2.Transport  3.Shopping  4.Bills  5.Health  6.Other")
    choice = input("Choose category (1-6): ")
    if choice == "1":
        return "Food"
    elif choice == "2":
        return "Transport"
    elif choice == "3":
        return "Shopping"
    elif choice == "4":
        return "Bills"
    elif choice == "5":
        return "Health"
    elif choice == "6":
        return "Other"
    else:
        print("Invalid choice, setting to Other!")
        return "Other"
#main function     
def main():
    print("Welcome to Expense Tracker")
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            title = input("Enter title: ")
            while True:
                amount = input("Enter amount (Rs): ")
                if amount.isdigit() and int(amount) > 0:
                    break
                print("Invalid amount")
            category = get_category()
            add_expense(title, int(amount), category)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_expenses()
            expense_id = input("Enter expense ID to delete:")
            delete_expense(expense_id)
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Goodbye...")
            break
        else:
            print("Invalid choice, please enter 1-5")
main()