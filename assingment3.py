gross_salary = int(input("Enter gross salary"))
if gross_salary <= 5999 and gross_salary > 0 :
    print("Monthly contribution is ksh: ", 150.00)
elif gross_salary >= 6000 and gross_salary <= 7999 :
     print("Monthly contribution is ksh: ", 300.00)
elif gross_salary >= 8000 and gross_salary <= 11999 :
     print("Monthly contribution is ksh: ", 400.00)
elif gross_salary >= 12000 and gross_salary <= 14999 :
     print("Monthly contribution is ksh: ", 500.00)
elif gross_salary >= 15000 and gross_salary <= 19999 :
     print("Monthly contribution is ksh: ", 600.00)
elif gross_salary >= 20000 and gross_salary <= 24999 :
     print("Monthly contribution is ksh: ", 750.00)
elif gross_salary >= 25000 and gross_salary <= 29999 :
     print("Monthly contribution is ksh: ", 850.00)
elif gross_salary >= 30000 and gross_salary <= 49999 :
     print("Monthly contribution is ksh: ", 1000.00)
elif gross_salary >= 50000 and gross_salary <= 99999 :
     print("Monthly contribution is ksh: ", 1500.00)
elif gross_salary >= 100000:
     print("Monthly contribution is ksh: ", 2000.00)
else :
     print("Invalid input")
