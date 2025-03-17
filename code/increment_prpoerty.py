class Employee:
    salary = 12000
    increment = 10 # default increment
    # def __init__(self, increment):
    #     self.increment = increment
    @property
    def show(self):
        newsalary = self.salary + self.salary*self.increment/100
        return newsalary
    @show.setter # type: ignore
    def increment_value(self,newsalary):
       self.increment = (100*(newsalary-self.salary))/self.salary
        
        




ag = Employee()
print(ag.increment)
ag.increment_value = 14400
print(ag.increment)



        
