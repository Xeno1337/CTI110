# A program that calculates profit
# 2/15/2019
# CTI-110 P2T1 - Sales Prediction
# Erik Villela
#
import time
print("This program does not accept symbols as input. Percentage is accepted as either a whole number or decimal.")
print("----------------------------------------------------------------------------------------------------------")
sales = float(input("What were the sales? "))
percent = float(input("What percentage of sales are profit? "))
if percent < 1:
    profit = sales * percent
if percent >= 1:
    profit = sales * (percent / 100)
rprofit = round(profit, 2)
print("You made", rprofit, "in profit")
time.sleep(3)
print("This program will close in 10 seconds")
time.sleep(10)