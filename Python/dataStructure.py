employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12458, "name": "Paul", "department": "House Floor"},
]


def get_employee(id):
    for employee in employee_list:
        if employee["id"] == id:
            return employee


print(get_employee(12458))

employee_dict = {
    12345: {"id": "12345", "name": "John", "department": "Kitchen"},
    12458: {"id": "12458", "name": "Paul", "department": "House Floor"},
}


def get_employee_from_dict(id):
    return employee_dict[id]


print(get_employee_from_dict(12458))
