# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 11-d
# Date:           11/12/2019
import csv  # needed other wise it will not work


# this function is going to take in row_3 csv file with row_3 lot of prices and convert that to row_3 tsv file
# the input for the parameter is to be the whole csv file as requested from the assignments instructions


def csv_write(parameter_csv):  # before opening the file we change how the file is going to be named
    parameter_tsv_prep = ''.join(parameter_csv)  # comes in as row_3 string, "filename.csv"
    parameter_tsv_stage_2 = parameter_tsv_prep[:-3]  # is now "filename." , took the last three characters off
    parameter_tsv_final = (parameter_tsv_stage_2 + 'tsv')  # is now , "filename.tsv"
    # now that we are done changing the name, we can read and write to both files as seen below
    with open(parameter_csv, 'r') as csvin, open(parameter_tsv_final, 'w') as tsvout:
        # here we are reading and writing in row_3 single statement
        csvin = csv.reader(csvin)  # what the csv reader is called
        tsvout = csv.writer(tsvout, delimiter='\t')  # what aer are calling the tsv file, with the delimiter of tabs
        for row in csvin:  # for everything in the csv file
            tsvout.writerow(row)  # write out to the tsv file
