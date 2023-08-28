class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_table(self):
        for employee in self.employees:
            print(employee.id,"\t\t\t",employee.name,"\t\t\t",employee.age,"\t\t\t",employee.salary)

    def sort_by_age(self):
        self.employees.sort(key=lambda x: x.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda x: x.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda x: x.salary)
if __name__ == "__main__":
    employee_table = EmployeeTable()

    employee_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    employee_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    employee_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    employee_table.add_employee(Employee("171E20", "Tejas", 30, 55000))    
    employee_table.add_employee(Employee("1171G30", "Ajay", 45, 4400))
    
    print("Select sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input())

    if choice == 1:
        employee_table.sort_by_age()
    elif choice == 2:
        employee_table.sort_by_name()
    elif choice == 3:
        employee_table.sort_by_salary()
    else:
        print("Invalid choice")

    print("Sorted Employee Table:")
    print("Employee_ID \t\t\t Name \t\t\t Age \t\t\t Salary(PM) ")
    employee_table.print_table()
    