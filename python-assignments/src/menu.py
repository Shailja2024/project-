"""
Menu Module

This module provides the main menu interface for the Employee Management System.
Users can interact with the application through the menu options, which include
adding, deleting, updating employee information, generating reports, and exiting
the application.
"""
# If you're using relative imports like in a package, ensure the parent package correctly imports these:
# from .employee_operations import add_employee, delete_employee, update_employee
# from .report_generation import generate_reports

# For demonstration, let's define these functions here to avoid import errors:
def add_employee():
    print("Add Employee Function")

def delete_employee():
    print("Delete Employee Function")

def update_employee():
    print("Update Employee Function")

def generate_reports():
    print("Generate Reports Function")

def main_menu():
    """
    Main Menu Function
    Displays the main menu for the Employee Management System and prompts the user for input.
    Based on the user's choice, it calls the corresponding functions to perform actions such as
    adding, deleting, or updating employee information, generating reports, or exiting the program.
    """
    menu_options = {
        1: add_employee,
        2: delete_employee,
        3: update_employee,
        4: generate_reports,
        5: 'exit'  # Placeholder for exit action
    }

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Generate Reports")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                if choice == 5:
                    print("Exiting the program. Goodbye!")
                    break
                menu_options[choice]()
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# This if statement prevents the main_menu function from being called automatically when this script is imported.
if __name__ == "__main__":
    main_menu()
