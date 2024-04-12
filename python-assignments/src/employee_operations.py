def add_employee():
    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.
    """
    try:
        # Prompt the user to input the employee's name
        name = input("Enter the employee's name: ")

        # Prompt the user to input the employee's department
        department = input("Enter the employee's department: ")

        # Prompt the user to input the employee's salary
        salary = float(input("Enter the employee's salary: "))

        # Code to add a new employee
        # ...

        # Print a success message
        print(f"Employee {name} added successfully.")

    except ValueError:
        # Print an error message if the user inputs an invalid value
        print("Invalid input. Please enter a valid salary.")

    except Exception as e:
        # Print an error message for any other exceptions
        print(f"An error occurred: {e}")
