# bill_total = 210
# discount1 = 10
# discount2 = 20

# if bill_total > 100 and bill_total < 200:
#     print("Bill is greateater than 100")
#     bill_total = bill_total - discount1
# elif bill_total > 200:
#     print("Bill is greater than 200")
#     bill_total = bill_total - discount2
# else:
#     print("Bill is less than 100")
# print("Total Bill: ", str(bill_total))

# current = False

# if current:
#     current = False
#     print("Turning light off")

# if not current:
#     current = True
#     print("Turning light on")

# current = False

# if current:
#     current = False
#     print("Turning light off")
# else:
#     current = True
#     print("Turning light on")

loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    # give 20% discount
    total_bill = total_bill - (float(total_bill) / 100) * 20
elif total_bill > 100:
    # give 10% discount
    total_bill = total_bill - (float(total_bill) / 100) * 10
else:
    # sorry no discount, 5% service charge applied.
    print("Sorry, no discount ...")

print("Total Bill: ", float(total_bill))
