import os
import random
import shutil
from datetime import date


from config import file_with_employees, employee_sections, list_of_actions
from display import format_table, make_table


def load_database(file_with_employees):
    with open(file_with_employees) as file:
        content = file.read()
    return eval(content)  # function eval() converts the content string into a dictionary.


def commit_changes(file_with_employees, data):
    with open(file_with_employees, 'w') as file:
        file.write(data)


def generate_header():
    menu = '| ' + ' | '.join(list(list_of_actions)) + ' |'
    line = '=' * len(menu)
    return '\n'.join([line, menu, line])


def create_new_employee(employees):
    """
       Create a new employee record with the employees dictionary
       Use the employee_sections dictionary template to create a
       new employee record.
    """
    subsidiary = input('Employee Subsidiary (SK, CZ):')
    employee_id = generate_employee_id(subsidiary, employees)
    employee = {}  # Storage for new employee
    print('Please, enter records for new employee ID: ' + employee_id)

    # Iterating over 'employee_sections'
    for section in employee_sections['<employee_id>']:
        # Inserting empty section
        employee[section] = {}
        for field in employee_sections['<employee_id>'][section]:
            _input = ''
            while not _input:
                _input = input(section + '/' + field + ': ')

                from config import employee_required_fields
                if not _input and field in employee_required_fields:
                    print('This field is required, please enter the value.')
                else:
                    employee[section][field] = _input
                    break

    print(employee)
    employees[employee_id] = employee

    print('Thank you, entry has been completed for ID: ' + employee_id)
    input('Press ENTER to continue')

    commit_changes(file_with_employees, str(employees))
    return employees


def generate_employee_id(subsidiary, employees):
    """
      Generate a new unique id in consisting of subsidiary
      and 6 digit number
    """
    while True:
        random_number = random.randint(100000, 999999)
        employee_id = subsidiary.upper() + str(random_number)
        if employee_id not in employees:
            return employee_id


def find_employee(employees, employee_id):
    employee = employees.get(employee_id, None)
    if employee:
        data = list(employee['1. Personal'].items()) \
               + list(employee['2. Employee'].items())

        table = make_table(data, 2)
        print('\n' + format_table(table, []), end='\n\n')
    else:
        print('Could not find the employee id: ' + employee_id)
    return employees


def remove_employee(employees, employee_id):
    if employee_id in employees:
        del employees[employee_id]
        print('Employee ' + employee_id + ' has been removed from the DB.')
    else:
        print('There is no such employee ' + employee_id + ' in database.')

    commit_changes(file_with_employees, str(employees))
    return employees


def db_backup():
    if not "Backup_dir" in os.listdir():
        os.mkdir("Backup_dir")
    file_backup_name = '{}_{}'.format(date.today(), file_with_employees)

    shutil.copy(file_with_employees, os.path.join(r"Backup_dir", file_backup_name))

    print('New back-up file created: {}'.format(file_backup_name))
