"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

  balance - the outstanding balance on the credit card

  annualInterestRate - annual interest rate as a decimal

  monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

  -> Remaining balance: 813.41

  instead of

  -> Remaining balance: 813.4141998135 

  So your program only prints out one thing: the remaining balance at the end of the year in the format:

  -> Remaining balance: 4784.0

---
A summary of the required math is found below:

  Monthly interest rate = (Annual interest rate) / 12.0
  Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
  Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
  Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.
"""

balance = float(input('Balance (number): '))
annualInterestRate = float(input('interest rate (decimal format): '))
monthlyPaymentRate = float(input('minimum monthly rate (decimal format): '))

def makePayment(balance, monthlyInterestRate, monthlyPaymentRate):
  minMonthlyPayment = monthlyPaymentRate * balance
  monthlyUnpaidBalance = balance - minMonthlyPayment
  return monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

def balanceAfterYear(balance, annualInterestRate, monthlyPaymentRate):
  monthlyInterestRate = annualInterestRate / 12

  for month in range(0, 12):
    balance = makePayment(balance, monthlyInterestRate, monthlyPaymentRate)

  return round(balance, 2)

balance = balanceAfterYear(balance, annualInterestRate, monthlyPaymentRate)
print('Remaining balance:', balance)
