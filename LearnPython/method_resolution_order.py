class Employee:
    def work(self):
        print('Employee is working')
        
class Manager(Employee):
    def work(self):
        print('Manager supervises works of fellow employees')
        
class Developer(Employee):
    def work(self):
        print('Developer maintains the companys website')
        
class TechHead(Manager, Developer):
    pass
    
a = TechHead()
a.work()