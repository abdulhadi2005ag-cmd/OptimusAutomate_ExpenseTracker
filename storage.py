import json
import os
#storing path of file
data_file="expenses.json"
#function for opening the file 
def load_expenses():
    if not os.path.exists(data_file):
        return[]   #it will return just empty list 
    with open(data_file,"r") as f:
        return json.load(f)
#function for adding expenses to it    
def save_expenses(expenses):
    with open(data_file, "w") as f:
        json.dump(expenses, f, indent=2)    
