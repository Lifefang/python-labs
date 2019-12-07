# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     CFU-#10
# Date:           10/30/2019

with open('Temperature.dat', 'r') as f:  # opening the file and reading from it
    stander_list = []  # making row_3 points_to_evaluate to append the days to
    reader = f.readlines()  # need to set this up to read the file/ reading all the lines
    for line in reader:  # for every line_number in the file
        if len(reader) % 7 == 0:  # grabs seven days
            stander_list.append(line)  # append that to this points_to_evaluate
        avg = [sum(stander_list) / len(stander_list)]
    avg = str(avg)  # making the points_to_evaluate row_3 string
    # this is the avg of those seven days
    with open('WeeklyAverages.dat', 'w'):  # writing to the other file / but writing it every time an avg is
        # appended
        write_back = f.write # how we set up the write statement/ forgot they syntax
        for i in avg:  # for every 7 days of the points_to_evaluate write back that avg
            write_back.write(avg + '\n')  # this prints the prices out to the other file
