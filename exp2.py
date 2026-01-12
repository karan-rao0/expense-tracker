expenses = {
    "food": 0,
    "travel": 0,
    "education": 0
}
def add_expense(expenses, category, amount):
    expenses[category] += amount
def get_right_value():
     while True:
                 try:
                    return float(input("please enter amount").strip())
                    break
                 except ValueError:
                    print("invalid input please enter a float or an integer.")

budget = float(input("what is your budget?"))

while True:
     total_exp = sum(expenses.values())
    
     print ("1. add expense")
     print ("2. view breakdown")
     print ("3. check balance")
     print ("0. exit")
    
     selection = input("please select an option").strip().lower()

     if selection in ("1", "add expense"):
         print ("1. food")
         print ("2. travel")
         print ("3. education")

         exp_type = input("please select an expense type.").lower().strip()

         if exp_type in ("1", "food"):
             category = "food"
             amount = get_right_value()       
             add_expense(expenses, "food", amount)
             print("updated expenses:", expenses)
         elif exp_type in ("2", "travel"):
             category = "travel"
             amount = get_right_value()
             add_expense(expenses, "travel", amount)
             print("updated expenses:", expenses)
         elif exp_type in ("3", "education"):
             category = "education"
             amount = get_right_value()
             add_expense(expenses, "education", amount)
             print("updated expenses:", expenses)

     elif selection in ("2", "view breakdown"):
        print("breakdown: ", expenses)
     elif selection in ("3", "check balance"):
        balance = budget - total_exp
        print("balance", balance)
     elif selection in ("0", "exit"):
         break        
     else:
         print("invalid input please select one of those options or a number from 0-3")
