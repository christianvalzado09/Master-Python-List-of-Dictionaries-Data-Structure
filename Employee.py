employee = [
   {"name" : "John Doe", "department" : "Sales", "ID" : 1, "age" : 30, "email" : "john.doe@company.com"},
   {"name" : "Jane Smith", "department" : "Human Resources", "ID" : 2, "age" : 25, "email" : "jane.smith@company.com"},
   {"name" : "Mark Johnson", "department" : "IT", "ID" : 3, "age" : 40, "email" : "mark.johnson@company.com"},
   {"name" : "Lisa Wong", "department" : "Marketing", "ID" : 4, "age" : 28, "email" : "lisa.wong@company.com"},
   {"name" : "Paul McDonald", "department" : "Finance", "ID" : 5, "age" : 35, "email" : "paul.mcdonald@company.com"}
]

for employee in employee:

    print(f"name: {employee['name']}, department: {employee['department']}, ID: {employee['ID']}, age: {employee['age']}, email: {employee['age']},")