ef add_employee():
    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.
    """

    employees = [] # List to store employee information

    # Prompt the user for employee details
    employee_id = input("Enter employee ID: ")
    employee_name = input("Enter employee name: ")
    employee_department = input("Enter employee department: ")
    employee_salary = float(input("Enter employee salary: "))

    # Create a dictionary to store employee information
    new_employee = {
        "id": employee_id,
        "name": employee_name,
        "department": employee_department,
        "salary": employee_salary
    }

    # Add the new employee to the list
    employees.append(new_employee)

    print(f"Employee {employee_name} added to the system.")
