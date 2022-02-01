employee_sections = {'<employee_id>':
                         {'1. Personal': ('First Name', 'Middle Name Initial',
                                          'Last Name', 'Street Address', 'City',
                                          'State', 'Country of Residence',
                                          'ZipCode', 'Personal Email',
                                          'Telephone Number', '_Username',
                                          '_Password', 'Date of Birth', 'Age',
                                          'Citizenship', 'National ID'),
                          '2. Employee': ('Employment Status', 'Subsidiary',
                                          'Manager', 'Department', 'Job Title',
                                          'Band', 'Contract Beginning',
                                          'Contract Type', 'Contract End',
                                          'Is Manager', 'Manager of Department',
                                          'FTE', 'Full-Time Salary')
                          }
                     }

employee_required_fields = ('First Name', 'Last Name',
                            'Contract Beginning', 'Contract End',
                            'FTE', 'Contract Type', 'Manager',
                            'Department', 'Job Title', 'Band',
                            'Full-Time Salary')


list_of_actions = ('Create New Employee', 'Find Employee', 'Remove Employee')

file_with_employees = 'employees.txt'
