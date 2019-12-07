# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-3b-d
# Date:           9/16/2019
print("This program is going to request inputs from the user to calculate barrels per day.")
initial_oil_production_bpd_input = float(input("Please enter the initial oil production (bpd):"))  # bpd
arps_b_coefficient_input = float(input("Please enter the arps coefficient"))
initial_decline_rate_bpd_input = float(input("Please enter the initial decline rate(bpd):"))  # bpd
time_in_days_input = float(input("Please enter in the days(days):"))  # days
# Arps list_of_evaluated_areas = initial_oil_production_bpd
# /(1+arps_b_coefficient*initial_decline_rate_bpd*time_in_days)**(1/arps_b_coefficient)
arps_answer = initial_oil_production_bpd_input / (1 + arps_b_coefficient_input * initial_decline_rate_bpd_input *
                                                  time_in_days_input) ** (1 / arps_b_coefficient_input)
# getting row_3 fixed variable to preform the operation involving precision on.
arps_precision = '%.4f' % arps_answer
print('The Arps list_of_evaluated_areas foresees the production rate being:',
      arps_precision, 'barrels per day.')
# reformatted the line_number for readability
