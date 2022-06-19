# This program allows the user to choose between two calculators investment or bond
# Imports math library
import math

while True:
        print("\nChoose either 'investment' or 'bond' from the menu below to proceed:\n")
        print("investment\t- to calculate the amount of interest you'll earn on interest")
        print("bond\t\t- to calculate the amount you'll have to pay on a home loan")
        print("exit\t\t- to exit the program")
        # Commands the user to choose a calculator
        calc_choice = input("\nType your choice here: ").upper()

        # Checks the calculator choice
        if (calc_choice == "INVESTMENT"): 
                dep_amount = float(input("\nEnter the amount you depositing: R"))
                inter_rate = float(input("Enter the interest rate in percentage(only enter number): "))
                period = int(input("Please enter the number of years you plan on investing for: "))
                print("\nChoose either 'simple' or 'compound' interest:")
                
                # Commands the user to enter their choice whether simple or compound
                interest = input("\nType you choice here: ").upper() 
                if (interest == "SIMPLE"):
                         # Calculate the future amount using simple interest formula
                        future_amount =  dep_amount * (1 + ((inter_rate/100) * period))
                        # Displays the results rounded of to 2 decimal places
                        print("\nThe future amaount will be: R{}".format(round(future_amount,2))) 
                elif (interest == "COMPOUND"):
                         # Calculates the future amount using compound interest formula
                        future_amount = dep_amount * math.pow((1+(inter_rate/100)),period)
                         # Displays the results rounded of to 2 decimal places
                        print("\nThe future amaount will be: R{}".format(round(future_amount,2)))
                else:
                        print("\nPlease make sure you have typed a correct word!")
                        
        # Checks the calculator choice
        elif(calc_choice == "BOND"): 
                pres_value = float(input("Enter the present value of the house: R"))
                inter_rate = float(input("Enter the interest rate in percentage(only enter number): "))
                num_months = float(input("Enter the number of months you plan to take to repay the bond: "))
                i = inter_rate/12
                payments = (i*pres_value)/(1-((1+i)**-num_months))
                # Displays the results rounded of to 2 decimal places
                print("\nYou will have to pay R{} each month".format(round(payments,2)))
        elif (calc_choice ==  "EXIT"):
                        print("\nGood bye!!")
                        exit()
        else:
                print("\nPlease make sure you have typed a correct word. Try again..")

        print("\n========================================================")
	
