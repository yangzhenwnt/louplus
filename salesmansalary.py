#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
num = int(input("Enther the number of inputs sold: "))
price = float(input("Enter the price of camera: "))

bonus = (bonus_rate * num)
commission = (commission_rate * price * num)

print("Bonus  = {:6.2f}".format(bonus))
print("Commission = {:6.2f}".format(commission))
print("Gross salary = {:6.2f}".format(basic_salary + bonus + commission))
