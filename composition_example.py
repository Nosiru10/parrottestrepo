class Employee:
   def __init__(self, name, department, salary):
       self.name = name 
       self.department = department
       self.salary = salary

       def check_salary(salar):
           return self.salary.check_salary()


           class salary:

               def __init__(self, amount, bonus):
                   self.amount = amount
                   self.bonus = bonus


                   def check_salary(self):
                       return f"Marketer's salary is {self.amount +(self.amount* self.bonus} with a bonus of {self.bonus}"


market_salary = salary('800000,'10)
market = employee('adams','marketing')

print(marketer_employee.check_salary())