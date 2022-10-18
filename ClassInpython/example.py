# create class
class Company:
    # attributes
    name = 'abc'
    turnover = 500000
    revenue = 1000000000
    employee = 500
    # methods
    def productivity(self):
        return  Company.revenue/ Company.employee
company = Company()
print(company.name)
print(company.revenue)    