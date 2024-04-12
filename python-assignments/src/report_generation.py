The provided code has some minor errors and can be improved for readability and efficiency. Here's the revised version:

Python
def generate_reports(employee_data):
  """
  Generate Reports Function

  This function generates various reports based on employee data:

  - List of Departments: Unique department names.
  - List of All Employees: ID, full name, and department for each employee.
  - Departmental Averages: Average age and salary per department.
  - Employee Details by Department: ID, full name, date of birth, salary, and
    total department salary for each employee, grouped by department.

  Args:
      employee_data (list): A list of dictionaries containing employee data.

  Returns:
      dict: A dictionary containing the generated reports.
  """

  reports = {}

  # List of Departments (unique)
  departments = list(set(emp['department'] for emp in employee_data))
  reports['List of Departments'] = departments

  # List of All Employees
  all_employees = [
      {'id': emp['employee_id'], 'full_name': emp['full_name'], 'department': emp['department']}
      for emp in employee_data
  ]
  reports['List of All Employees'] = all_employees

  # Departmental Averages
  departmental_averages = []
  for dept in departments:
    dept_employees = [emp for emp in employee_data if emp['department'] == dept]
    if dept_employees:  # Check if there are employees in the department
      total_age = sum(emp.get('age', 0) for emp in dept_employees)  # Handle missing age
      avg_age = total_age / len(dept_employees)
      total_salary = sum(emp.get('salary', 0.0) for emp in dept_employees)  # Handle missing salary
      avg_salary = total_salary / len(dept_employees)
      departmental_averages.append({'department': dept, 'avg_age': avg_age, 'avg_salary': avg_salary})
  reports['Departmental Averages'] = departmental_averages

  # Employee Details by Department
  employee_details_by_dept = {}
  dept_total_salaries = {dept: 0 for dept in departments}
  for emp in employee_data:
    dept = emp['department']
    if dept not in employee_details_by_dept:
      employee_details_by_dept[dept] = []
    employee_details_by_dept[dept].append({
        'id': emp['employee_id'],
        'full_name': emp['full_name'],
        'date_of_birth': emp.get('date_of_birth'),
        'salary': emp.get('salary'),
    })
    dept_total_salaries[dept] += emp.get('salary', 0.0)  # Handle missing salary

  for dept, emp_list in employee_details_by_dept.items():
    emp_list.append({'Total Salary': dept_total_salaries[dept]})

  reports['Employee Details by Department'] = employee_details_by_dept

  return reports
