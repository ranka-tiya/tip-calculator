bill=float(input("Enter your bill amount"))
tip_percent=float(input("Enter your tip percentage"))
people=float(input("Enter number of people"))

tip_amount=bill*tip_percent/100
total_amount=bill+tip_amount
perperson=total_amount/people

print("Your total amount is:",total_amount)
print("Each person pays:",perperson)