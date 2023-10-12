'''
This is a program that calculates the amount of time in months its going to take for the
user to save for the down payment. It calculates if the user is getting a raise in his
or her salary and also if he or she is not getting any raise.

It prompts the user to select option which suits him or her best, then it calculates 
everything.

'''
def no_increase():

    annual_salary = float(input("\nEnter your annual salary: "))
    percent_to_save = float(input("\nEnter the percent of your salary to save, as a decimal: "))
    cost_of_house = float(input("\nEnter the cost of your dream home: ")) #cost of the house

    monthly_salary = annual_salary / 12
    portion_down_payment = cost_of_house * (1/4)

    current_savings = 0
    num_of_months = 0

    while current_savings < portion_down_payment:
        current_savings += monthly_salary * (percent_to_save)
        current_savings += current_savings * ((4/100)/12)
        num_of_months += 1

    print (f"\nNumber of months: {num_of_months}")

def an_increase_every_six_months():

    starting_annual_salary = float(input("\nEnter your starting annual salary: "))
    percent_to_save = float(input("\nEnter the percent of your salary to save, as a decimal: "))
    cost_of_house = float(input("\nEnter the cost of your dream home: "))
    semi_annual_raise = float(input("\nEnter the semi-annual raise, as a decimal: "))

    monthly_salary = starting_annual_salary / 12
    portion_down_payment = cost_of_house * (1/4)

    current_savings = 0
    num_of_months = 0

    while current_savings < portion_down_payment:

        if num_of_months % 6 == 0 and num_of_months != 0:
            starting_annual_salary += starting_annual_salary * (semi_annual_raise)
            monthly_salary = starting_annual_salary / 12

        current_savings += monthly_salary * (percent_to_save)
        current_savings += current_savings * ((4/100)/12)
        num_of_months += 1

    print (f"\nNumber of months: {num_of_months}")

def an_increase_every_year():

    starting_annual_salary = float(input("Enter your starting annual salary: "))
    percent_to_save = float(input("Enter the percent of your salary to save, as a decimal: "))
    cost_of_house = float(input("Enter the cost of your dream home: "))
    annual_raise = float(input("Enter the annual raise, as a decimal: "))

    monthly_salary = starting_annual_salary / 12
    portion_down_payment = cost_of_house * (1/4)

    current_savings = 0
    num_of_months = 0

    while current_savings < portion_down_payment:

        if num_of_months % 12 == 0 and num_of_months != 0:
            starting_annual_salary += starting_annual_salary * (annual_raise)
            monthly_salary = starting_annual_salary / 12

        current_savings += monthly_salary * (percent_to_save)
        current_savings += current_savings * ((4/100)/12)
        num_of_months += 1

    print (f"\nNumber of months: {num_of_months}")

def main():
  print ("\nWelcome to the Down Payment Calculator!\n")
  print ("Select an option:\n")
  print ("1. Calculate for the user who is not getting a raise.\n")
  print ("2. Calculate for the user who is getting a raise every six months.\n")
  print ("3. Calculate for the user who is getting a raise per annum.\n")

  user_input = int(input("Enter your choice: "))
    
  if user_input == 1:
    print("\nYou have chosen to calculate for the user who is not getting a raise.\n")
    return no_increase()

  elif user_input == 2:
    print("\nYou have chosen to calculate for the user who is getting a raise every six months.\n")
    return an_increase_every_six_months()

  elif user_input == 3:
    print("\nYou have chosen to calculate for the user who is getting a raise per annum.\n")
    return an_increase_every_year()
  

main()