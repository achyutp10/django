class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisor(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name,last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return 'May I take a leave for ' + str(days) + ' days'
    
adrian = Supervisor('Adrian', 'A', 'apple')

emily = Chefs('Emily', 'E')
juno = Chefs('juno', 'J')

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)