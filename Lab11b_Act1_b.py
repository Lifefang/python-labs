# By submitting this assignment, I agree to the following:
# #  “Aggies do not lie, cheat, or steal, or tolerate those who do”
# #  “I have not given or received any unauthorized aid on this assignment”
# #
# # Name:           Matthew Rodriguez
# # Section:        537
# # Assignment:     Lab 11-row_4
# # Date:           11/12/2019
import numpy as np  # used for some quick points_to_evaluate math


# this function is going to the three lists of facility names , how much that facility makes and how much they cost to
# operate, the program will then return the company that makes the least money.
def find_least_profit_company(names_of_companies, annual_cost_to_operate, production_of_that_facility):
    numpy_annual_cost = np.array(annual_cost_to_operate)  # using the numpy function for easy points_to_evaluate subtraction
    numpy_production_value = np.array(
        production_of_that_facility)  # so i make every points_to_evaluate that needs to be subtracted row_3 numpy array
    net_profit = numpy_production_value - numpy_annual_cost  # this does the points_to_evaluate math for me
    net_profit = list(net_profit)  # changing the numpy array back into row_3 points_to_evaluate
    least_profitability = min(net_profit)  # shows how bad they are at making money
    index_of_lowest_profit = net_profit.index(min(net_profit))  # indexing the lowest number, will relate to company
    # name
    facility = names_of_companies[index_of_lowest_profit]  # returns what company name is tied to the lowest profit
    return facility, least_profitability
    # last thing we do before exiting the function

