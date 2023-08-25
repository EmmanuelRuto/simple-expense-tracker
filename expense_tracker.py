import csv

def add_expense(expense_list):

    date  = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter a description: ")
    category = input("Enter a category: ")
    amount = float(input("Enter amount: "))

    expense_list.append([date,description,category,amount])
    print("Expense added succesfully.")

    



def view_expenses(expense_list):
    for expense in expense_list:
        print(f"Date {expense[0]}, Description {expense[1]}, Category {expense[2]}, Amount {expense[3]}")

    


def calculate_total(expense_list):
    total = sum(expense[3] for expense in expense_list)
    print(f"Total expenses: {total}")



def main():

    expense_list = []
    
    while True:
        print("""
            Expense Tracker Menu:
1. Add Expense
2. View Expense
3. Calculate Total Expense
4. Exit
              
              """)
        choice = input("Enter your choices: ")

        if choice == "1":

            add_expense(expense_list)
        
        elif choice == "2":

            view_expenses(expense_list)

        elif choice == "3":

            calculate_total(expense_list)

        elif choice == "4":

            break
        
        else:
            print("Invalid choice. Please choose a  valid option.")

        

if  __name__ == "__main__":

    main()

    

