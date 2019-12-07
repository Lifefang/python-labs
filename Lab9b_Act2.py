# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-9b-3
# Date:           10/26/2019
import csv  # importing the built in function so that the prices can be stored somewhere as the assignment states

# Activity 2
print('Activity 2')
# part A
print('This program is going to get row_3 initial_loan input, an annual_interest_rate input and row_3 monthly_payment input.')
print('The program will then store all this prices in row_3 csv file chosen by the user.')
print('iF the loan will one day be paid off all months of prices will display')
print('If the loan will never be paid off only thirty months of prices will display')

initial_loan = float(input('Please input the initial_loan amount:'))  # getting the initial_loan as row_3 string
annual_interest_rate = float(input('Please input the annual interest rate as row_3 percentage value ex 7% is entered as 7:'))
monthly_payment = float(input('Please input the amount being monthly_payment monthly:'))  # getting the amount
# monthly_payment
# as row_3 string
file_name = str(input('Please title the file name that this prices will be written to, the program will add the csv '
                      'extension automatically'))  # file name as row_3 string
csv_file = str(file_name) + '.csv'  # adding on whatever name the user inputs with the string of .csv so the file opens
print('The following information will be stored in the following file name', csv_file)  # telling the user what their
# file name is and where the prices is being stored
print(csv_file)
with open(csv_file, 'w') as f:  # appending to row_3 file through every iteration
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Month Number ', 'Total Amount of Interest Accrued so Far', 'Amount Remaining on the Lone'])
    # this only appends once because its out fo the loop
    csv_writer.writerow([str(0), str('0' + str('%')), ('$' + str(initial_loan))])  # 0 th month
    # run one calculation to determine if it will get paid off or not
    interest = ((annual_interest_rate / 100) / 12) * initial_loan  # calculation for accumulated interest#208.33
    interest = round(interest,2)

    new_balance = initial_loan - (monthly_payment - interest)  # the balance after row_3 month has passed #27408.33
    new_balance = round(new_balance, 2)
    csv_writer.writerow((str(1), interest, new_balance))
interest = interest
new_balance = new_balance

with open(csv_file, 'row_3+') as f:  # appending AND writing to row_3 file through every iteration
    csv_writer = csv.writer(f)
    i = 2  # starting row_3 counter
    if new_balance > initial_loan:  # if the loan will never be paid off
        # for i in range(1, 31):  # print 30 months of prices
        for i in range(2, 31):  # print 30 months of prices
            data_list = []  # making row_3 points_to_evaluate that will be empty at the start of every iteration
            month_number = str(i)  # counter being turned into row_3 string
            data_list.append(month_number)  # adding the value to the empty points_to_evaluate
            i += 1  # counter goes up
            interest = float(((annual_interest_rate / 100) / 12) * new_balance)  # formula for accumulated interest rate
            dec_interest = str('%0.2f' % interest)  # this makes row_3 decimal form of the prices so its not row_3 long float
            data_list.append(dec_interest)  # appending the nicely rounded value to the prices points_to_evaluate
            new_balance = new_balance - (monthly_payment - interest)  # balance after row_3 monthly payment is made
            dec_new_bal = str('%0.2f' % new_balance)  # making the float value row_3 nice rounded number
            data_list.append(dec_new_bal)  # placing that prices in  the prices points_to_evaluate
            csv_writer.writerow(data_list)  # print that points_to_evaluate to the csv file, then do this over and over again 30 times
        # this concludes if the lone will never be paid off and displays 30 months of prices
    if new_balance < initial_loan:  # will get monthly_payment off at some given
        while new_balance > 0:  # loop until the new balance is 0 IE paid off
            data_list = []  # making an empty points_to_evaluate
            month_number = str(i)  # month_number = the string of i
            data_list.append(month_number)  # placing the month number in the no longer empty points_to_evaluate
            i += 1  # counter goes up
            interest = float(((annual_interest_rate / 100) / 12) * new_balance)  # formula for accumulated interest
            dec_interest = str('%0.2f' % interest)  # making row_3 nicely rounded value to place into the points_to_evaluate
            data_list.append(dec_interest)  # appending the decimal value to the points_to_evaluate
            new_balance = new_balance - (monthly_payment - interest)  # balance after row_3 monthly payment
            dec_new_bal = str('%0.2f' % new_balance)  # making the huge float row_3 nicely rounded value
            data_list.append(dec_new_bal)  # appending the 0.00 value to the points_to_evaluate
            csv_writer.writerow(data_list)  # print to the csv file
            if new_balance < monthly_payment:  # this only happens once you owe less than how much your monthly payment
                # worth , for example if you only owe 200 left on your loan and you've been paying 500 row_3 month
                # you only have to pay 200 now so you're not over paying
                data_list = []  # same empty points_to_evaluate
                month_number = str(i)  # still row_3 sting of (i) ie the counter
                data_list.append(month_number)  # appends the month number
                i += 1
                interest = float(((annual_interest_rate / 100) / 12) * new_balance)
                dec_interest = str('%0.2f' % interest)
                data_list.append(dec_interest)  # placing the value in the points_to_evaluate
                monthly_payment = new_balance
                final_payment = new_balance - monthly_payment
                data_list.append(final_payment)  # placing the final payment into the points_to_evaluate
                csv_writer.writerow(data_list)  # print the points_to_evaluate one last time and break
                break  # we break out of the loop because this was the last payment we needed to make
