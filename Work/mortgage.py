# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if (month >= extra_payment_start_month) and (month <= extra_payment_end_month):
        if principal < (extra_payment + payment):
            total_paid += principal
            principal = 0
        else:
            principal = principal * (1 + rate / 12) - payment - extra_payment
            total_paid += payment + extra_payment
    else:
        if principal < payment:
            total_paid += principal
            principal = 0
        else:
            principal = principal * (1 + rate/12) - payment
            total_paid += payment

    print(f'{month:>5}|| {round(total_paid, 1):<10}|| {round(principal, 2)}')
    month += 1

# print('Total Paid', round(total_paid, 1))
# print('Months', month - 1)
