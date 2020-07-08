#!/usr/bin/env python3
import csv
csv.register_dialect('empDialect', skipinitialspace=True, strict=True)


def read_employees(csv_file_location):

    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

def process_data(employee_file):
    department_list  = []
    for data in employee_file:
        department_list.append(data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
      for k in sorted(dictionary):
        f.write(str(k)+':'+str(dictionary[k])+'\n')
      f.close()



employee_list = read_employees('/home/student-04-776ec4128be1/data/employees.csv')
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

write_report(dictionary, '/home/student-04-776ec4128be1/test_report.txt')

