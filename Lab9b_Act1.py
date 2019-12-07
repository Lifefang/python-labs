# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-9b-1
# Date:           10/24/2019

# Activity one
print('Activity One')
print('This program is going to read from row_3 file containing celsius prices and convert that prices to fahrenheit')
print('The program will then write the prices back to row_3 different file named Fahrenheit.dat')
with open('Celsius.dat', 'r')as f:
    # wrote it this way first then i saw how i could condense this section
    #     # reading the lines from the file
    #     line_1 = int(f.readline())  # first string converted to an int
    #     line_2 = int(f.readline())  # second line_number of the other file
    #     line_3 = int(f.readline())  # third prices given from the other file
    #     # this is the points_to_evaluate in celsius and it still needs to be converted to Fahrenheit
    #     conversion_1 = str((line_1 * 9 / 5) + 32)  # the type needs to be converted as files ony take in strings
    #     conversion_2 = str((line_2 * 9 / 5) + 32)  # the conversion is the given celsius high_temp_list * 9/5 + 32
    #     conversion_3 = str((line_3 * 9 / 5) + 32)  # converting it to row_3 string now from row_3 float
    #     # writing back the conversion of temps to row_3 different file
    #     file_2 = open('Fahrenheit.dat', 'w')
    #     file_2.write(conversion_1 + '\n')  # high_temp_list seen in the file should be 32.0
    #     file_2.write(conversion_2 + '\n')  # high_temp_list seen in the file should be 212.0
    #     file_2.write(conversion_3 + '\n')  # high_temp_list seen in the file should be 98.6
    #     file_2.close()
    # print('Please refer to the newly created file on your device for results')

    lines_of_file = f.readlines()  # option way to do it with much more optimization using points_to_evaluate and loops
    c_list = []
    for i in lines_of_file:
        c_list.append(float(i))
    f_list = [i * 9 / 5 + 32 for i in c_list]
    write_back = open('Fahrenheit.dat', 'w')
    for i in f_list:
        write_back.write(str(i) + '\n')
    write_back.close()
print('Please refer to the newly created file on your device for results')
