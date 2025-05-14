# class Employee with name, age and salary
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary})"
    
    def __repr__(self):
        return self.__str__()

# Create a list to store employees
employeeList = []

# Add employees to the list
employeeList.append(Employee("John", 25, 1000))
employeeList.append(Employee("Jane", 30, 2000))
employeeList.append(Employee("Bob", 35, 3000))
employeeList.append(Employee("Alice", 40, 4000))

# Function to get all employee names
def get_all_employees_names():
    return [employee.name for employee in employeeList]

# Print the result
print(get_all_employees_names())