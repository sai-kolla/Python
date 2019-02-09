class Employee:
    emp_cnt = 0
    esal = 0

    def __init__(self, ename, family, esal, dept):
        self.name = ename
        self.family = family
        Employee.esal += esal
        self.dept = dept
        Employee.emp_cnt += 1

    def display(self):
        print("total employees = ", Employee.emp_cnt)

    def avg_sal(self):
        avg_sal = Employee.esal / Employee.emp_cnt
        print("average salary of employee :", avg_sal)

    def demo_function(self):
        print('calling member function of parent')


class Full_time_employee(Employee):
    def __init__(self, ename, family, esal, dept):
        print('this is the subclass: Full time employee')
        Employee.__init__(self, ename, family, esal, dept)


e1 = Employee('sai', 'A', 2000, 'D1')
e2 = Employee('kolla', "B", 8000, "D2")
e3 = Employee('nagarjuna', 'C', 8000, 'D3')
c = Full_time_employee('arjun', 'D', 5000, 'D4')
c.display()
c.avg_sal()
c.demo_function()