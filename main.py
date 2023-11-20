'''
This is a program that calculates the amount of time in months its going to take for the
user to save for the down payment. It calculates if the user is getting a raise in his
or her salary and also if he or she is not getting any raise.

It prompts the user to select option which suits him or her best, then it calculates 
everything.

'''


def no_increase():

  annual_salary = float(input("\nEnter your annual salary: "))
  percent_to_save = float(
      input("Enter the percent of your salary to save, as a decimal: "))
  cost_of_house = float(
      input("Enter the cost of your dream home: "))  #cost of the house

  monthly_salary = annual_salary / 12
  portion_down_payment = cost_of_house * (1 / 4)

  current_savings = 0
  num_of_months = 0

  while current_savings < portion_down_payment:
    current_savings += monthly_salary * (percent_to_save)
    current_savings += current_savings * ((4 / 100) / 12)
    num_of_months += 1

  print(f"\nNumber of months: {num_of_months}")


def an_increase_every_six_months():

  starting_annual_salary = float(
      input("\nEnter your starting annual salary: "))
  percent_to_save = float(
      input("Enter the percent of your salary to save, as a decimal: "))
  cost_of_house = float(input("Enter the cost of your dream home: "))
  semi_annual_raise = float(
      input("Enter the semi-annual raise, as a decimal: "))

  monthly_salary = starting_annual_salary / 12
  portion_down_payment = cost_of_house * (1 / 4)

  current_savings = 0
  num_of_months = 0

  while current_savings < portion_down_payment:

    if num_of_months % 6 == 0 and num_of_months != 0:
      starting_annual_salary += starting_annual_salary * (semi_annual_raise)
      monthly_salary = starting_annual_salary / 12

    current_savings += monthly_salary * (percent_to_save)
    current_savings += current_savings * ((4 / 100) / 12)
    num_of_months += 1

  print(f"\nNumber of months: {num_of_months}")


def an_increase_every_year():

  starting_annual_salary = float(input("Enter your starting annual salary: "))
  percent_to_save = float(
      input("Enter the percent of your salary to save, as a decimal: "))
  cost_of_house = float(input("Enter the cost of your dream home: "))
  annual_raise = float(input("Enter the annual raise, as a decimal: "))

  monthly_salary = starting_annual_salary / 12
  portion_down_payment = cost_of_house * (1 / 4)

  current_savings = 0
  num_of_months = 0

  while current_savings < portion_down_payment:

    if num_of_months % 12 == 0 and num_of_months != 0:
      starting_annual_salary += starting_annual_salary * (annual_raise)
      monthly_salary = starting_annual_salary / 12

    current_savings += monthly_salary * (percent_to_save)
    current_savings += current_savings * ((4 / 100) / 12)
    num_of_months += 1

  print(f"\nNumber of months: {num_of_months}")


def calculate_savings_rate():
  starting_salary = float(input("Enter the starting salary: "))
  savings_rate, steps = calculate_savings_rate()

  total_cost = 1000000
  semi_annual_raise = 0.07
  annual_return = 0.04
  down_payment = 0.25 * total_cost
  months = 36

  low = 0
  high = 10000
  steps = 0

  while True:
    steps += 1
    savings_rate = (low + high) / 20000
    current_savings = 0
    annual_salary = starting_salary

    for month in range(1, months + 1):
      current_savings += (current_savings * annual_return /
                          12) + (annual_salary / 12 * savings_rate)
      if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

    if abs(current_savings - down_payment) <= 100:
      break
    elif current_savings < down_payment:
      low = savings_rate * 10000
    else:
      high = savings_rate * 10000

  print("Best savings rate:", round(savings_rate, 4))
  print("Steps:", steps)
  return savings_rate, steps


def get_and_validated_user_input():
  try:
    user_input = (input("\nEnter your choice: "))
    return int(user_input)

  except ValueError as f:
    print(F"\n{user_input} is an invalid input please choose a correct input")
    return get_and_validated_user_input()


def main():
  user_input = get_and_validated_user_input()

  if user_input == 1:
    print(
        "\nYou have chosen to calculate for the user who is not getting a raise."
    )
    return no_increase()

  elif user_input == 2:
    print(
        "\nYou have chosen to calculate for the user who is getting a raise every six months."
    )
    return an_increase_every_six_months()

  elif user_input == 3:
    print(
        "\nYou have chosen to calculate for the user who is getting a raise per annum."
    )
    return an_increase_every_year()

  elif user_input == 4:
    print("\nYou have chosen to find the right amount to save.")
    return calculate_savings_rate()

  else:
    print(F"{user_input} is out of range.")
    main()


def options_menu():
  print("Select an option:\n")
  print("1. Calculate for the user who is not getting a raise.")
  print("2. Calculate for the user who is getting a raise every six months.")
  print("3. Calculate for the user who is getting a raise per annum.")
  print("4. Finding the right amount to save away")


def get_option():
  makeAnOption = input(
      "\nDo you wish to make further calculations(y/n): ").strip()
  return makeAnOption


def welcome_menu():
  print("\nWelcome to the Down Payment Calculator!\n")
  options_menu()
  main()
  makeAnOption = get_option()

  if makeAnOption.lower() in ['y', 'yes', 'yep', 'yea', 'yeah']:
    return welcome_menu()

  elif makeAnOption.lower() in ['n', 'no', 'nah', 'nope']:
    exit()

  else:
    print('I did not understand your option')
    get_option()


if __name__ == "__main__":
  welcome_menu()
