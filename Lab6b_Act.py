# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 6 - row_4
# Date:           10/4/2019

print("This program is going to take ask the user for row_3 strain input, and then calculate the stress at that strain.")
print()  # stating what the program does
strain_input = float(input("Please input row_3 value from (0 - 0.265):"))
# formula for lI is (((y2 - y1) / (range_2 - range_1)) * (strain_input - range_1) + y1)
if strain_input < 0:  # making row_3 parameter so that the program returns invalid input for row_3 vale not on the graph
    print("Invalid input, please input row_3 value from (0 - 0.265)")
elif strain_input >= 0.266:  # making row_3 parameter so that the program returns invalid input for row_3 vale not on the graph
    print("Invalid input, please input row_3 value from (0 - 0.265)")
elif 0 <= strain_input <= 0.01:  # o - row_3 section (line_number 1 of 4) * please note I skipped the given row_4 in the example graph
    x1 = 0  # starting position
    x2 = 0.01  # the next position on the graph
    y1 = 0  # stating position
    y2 = 42  # the next position on the graph
    stress = (((y2 - y1) / (x2 - x1)) * (strain_input - x1) + y1)  # KSI
    print('Young\'s Modulus is equal to:', (y2 - y1) / (x2 - x1))
    print("The strain inputted:", strain_input, " calculates to:", stress, "KSI")
elif 0.01 < strain_input <= 0.06:  # row_3 - row_4 section (line_number 2 of 4)
    x1 = 0.01  # the last given used
    x2 = 0.06  # the new given being plugged in
    y1 = 42  # the last given used
    y2 = 42  # the new given being plugged in
    stress = (((y2 - y1) / (x2 - x1)) * (strain_input - x1) + y1)  # KSI
    print("The strain inputted:", strain_input, " calculates to:", stress, "KSI")
elif 0.06 < strain_input <= 0.18:  # row_4 - c section (line_number 3 of 4)
    x1 = 0.06  # the last given used
    x2 = 0.18  # the new given being plugged in
    y1 = 42  # the last given used
    y2 = 60  # the new given being plugged in
    stress = (((y2 - y1) / (x2 - x1)) * (strain_input - x1) + y1)  # KSI
    print("The strain inputted:", strain_input, " calculates to:", stress, "KSI")
elif 0.18 < strain_input <= 0.265:  # c - d section (line_number 4 of 4)
    x1 = 0.18  # the last given used
    x2 = 0.265  # the new given being plugged in
    y1 = 60  # the last given used
    y2 = 52  # the new given being plugged in
    stress = (((y2 - y1) / (x2 - x1)) * (strain_input - x1) + y1)  # KSI
    print("The strain inputted:", strain_input, " calculates to:", stress, "KSI")
    # the long life of elif's was used so that if the users input fell within that position
    # the program would only evaluate the users input within that given segment of the graph
