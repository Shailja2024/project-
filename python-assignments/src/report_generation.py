"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""

def generate_reports(employee_data):
    """
    Generate Reports Function

    This function generates various reports based on employee data, such as:
    - List of departments
    - List of all employees with ID, full name, and department
    - List of all departments with the average age and salary of employees
    - List of employees in each department with ID, full name, date of birth, salary,
      and total salary for department's employees

    Args:
        employee_data (list): A list of dictionaries containing employee data.
    """
    # List of departments
    departments = list(set(emp['department'] for emp in employee_data))

    # List of all employees with ID, full name, and department
    employees = [[emp['employee_id'], emp['full_name'], emp['department']] for emp in employee_data]

    # List of all departments with the average age and salary of employees
    dept_averages = []
    for dept in departments:
        dept_employees = [emp for emp in employee_data if emp['department'] == dept]
        total_age = sum(emp['age'] for emp in dept_employees)
        avg_age = total_age / len(dept_employees)
        total_salary = sum(emp['salary'] for emp in dept_employees)
        avg_salary = total_salary / len(dept_employees)
        dept_averages.append({'department': dept, 'avg_age': avg_age, 'avg_salary': avg_salary})

    # List of employees in each department with ID, full name, date of birth, salary,
    # and total salary for department's employees
    dept_emp_lists = {dept: [] for dept in departments}
    dept_total_salaries = {dept: 0 for dept in departments}

    for emp in employee_data:
        dept_emp_lists[emp['department']].append([emp['employee_id'], emp['full_name'], emp['date_of_birth'], emp['salary']])
        dept_total_salaries[emp['department']] += emp['salary']

    for dept in dept_emp_lists:
        dept_emp_lists[dept].append(dept_total_salaries[dept])

    return departments, employees, dept_averages, dept_emp_lists
