# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:51:48 2022

@author: dejong71
"""

#______________________________________________________________________________

import budget
from budget import create_spend_chart
from unittest import main
import os

#______________________________________________________________________________

# Change to Project folder and run unit tests automatically.
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

os.chdir(os.path.split(__file__)[0])
main(module='test_module', exit=False)

#______________________________________________________________________________