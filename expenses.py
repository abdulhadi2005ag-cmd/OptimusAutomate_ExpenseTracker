import uuid #generates unique id
from datetime import datetime
from storage import load_expenses,save_expenses
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Health", "Other"]
#function to add an expense
def add_expense(title,amount,category):
    expenses=load_expenses()
    #now dicionary for new expenses
    expense = {
        "id": str(uuid.uuid4())[:8],   #we taking first 8 numbers of random id
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(expense)  #add new expenses
    save_expenses(expenses)   #saving expenses as json
    print(f" Expense '{title}' of Rs {amount} added successfully")
#function for viewing the expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found")
        return    
    print("All Expenses:")
    for exp in expenses:   #loops through every expense
        print(f"ID: {exp['id']} , {exp['date']} , {exp['category']}")
        print(f"{exp['title']} — Rs {exp['amount']}")
#function to delete expense
def delete_expense(expense_id):
    expenses = load_expenses()
    new_expenses = []
    for exp in expenses:
        if exp["id"] != expense_id:
            new_expenses.append(exp)
    if len(new_expenses) == len(expenses):
        print(f"No expense found with ID: {expense_id}")
        return
    save_expenses(new_expenses)
    print("Expense deleted successfully!") 
#function for monthly summary
def monthly_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found")
        return
    summary = {}
    for exp in expenses:
        month = exp["date"][:7]   #we will only take month and year 
        if month not in summary:
            summary[month] = 0
        summary[month] += exp["amount"]  
    print("Monthly Summary:")
    for month, total in summary.items():
        print(f"{month} — Rs{total}")                
