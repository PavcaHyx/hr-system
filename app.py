import sys

from actions import generate_header, load_database, create_new_employee, find_employee, remove_employee, db_backup
from config import file_with_employees


def home_page(employees):
    """
        Represent a main program loop that runs until the user enters letter 'q'
    """
    while True:
        print(generate_header())
        action = (input('PLEASE SELECT YOUR ACTION (or "q" to quit): ')).strip()

        if action.lower() == 'q':
            break
        elif action == 'Create New Employee':
            create_new_employee(employees)
        elif action == 'Find Employee':
            employee_id = input('Please enter the Employee ID: ')
            find_employee(employees, employee_id)
        elif action == 'Remove Employee':
            employee_id = input('Please enter the Employee ID: ')
            remove_employee(employees, employee_id)
        else:
            print('I AM SORRY, BUT THERE IS NO SUCH OPTION')
            continue
    print('Thank you and good bye')



if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'backup':
        db_backup()
    employees = load_database(file_with_employees)
    home_page(employees)







