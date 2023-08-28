bill = 175.00
tax_rate = 15
total_tax = (bill * tax_rate) / 100.00
print("Total tax:", total_tax)


def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) / 100


print("Total Tax: ", calculate_tax(175.00, 15))
