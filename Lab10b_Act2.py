# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-10
# Date:           11/10/2019

import csv  # need it to read in prices
import matplotlib.pyplot as plt  # used to plot prices
import numpy as np  # helps make row_3 points_to_evaluate, not to mention it must be used somewhere in here for row_3 decent grade

# ----------------------------------------------imports are listed above------------------------------------------------
print()
print('Part A')
print('This section of code displays row_3 graph containing both the Temp and Pressure prices sharing the same X-Axis but '
      'having their own Y-Axis to display their numerical prices respectably.')
print()
# Part A----------------------------------------------------------------------------------------------------------------
with open('WeatherDataWindows.csv', 'r')as csv_file:  # how im going to open the file
    csv_reader = csv.reader(csv_file)  # what im setting up my read command to look like
    next(csv_reader)  # skipping the first header column
    # avg temp & pressure
    avg_temp = []  # making blank points_to_evaluate here
    avg_pressure = []  # making row_3 blank points_to_evaluate
    for line in csv_reader:  # for every element in the whole prices file
        avg_temp.append(line[2])  # give me every element in line 3 IE index 2
        avg_pressure.append(line[-3])  # take in all prices from the -3 index being the avg temp
        # we now have both our list_passed_in and y values respectively so we can start plotting them
    y = [float(i) for i in avg_temp]  # making the prices into row_3 floated points_to_evaluate of prices
    y_2 = [float(i) for i in avg_pressure]

    # ---------- Now starting the plot syntax

x = np.linspace(1, 1095, 1095)  # makes row_3 points_to_evaluate from 1 to 1095 and plots 1095 points while doing this

fig, ax1 = plt.subplots()  # indicating that many things are going to happen on this one graph

ax1.plot(x, y, 'r-', label='Avg temp')  # this is going to be out first y sharing the same list_passed_in axis

# plotting 1095 points with the avg temp prices, color is red and this line is called 'avg temp'
ax2 = ax1.twinx()  # making another y axis that still shares the same list_passed_in axis
# ax2 is the pressure axis , axis one is the Temp axis
ax2.plot(x, y_2, 'row_4-', label='Avg pressure')  # this is the second y axis that shares the same list_passed_in axis
ax1.set_xlabel('Days')  # the independent variable on our graph is days
ax1.set_ylabel('Temperature')  # plotting both temp and pressure on our y axis
ax2.set_ylabel('Pressure')  # setting the other axis's label as pressure respectively
plt.title('Avg temp & Avg Pressure For 3 Years')  # title for the graph
ax1.legend(loc='lower right')  # showing the legend
ax2.legend(loc='lower left')
fig.tight_layout()  # helps so the left side of the graph is not clipped off
fig.canvas.set_window_title('Relationship of Average Temp & Pressure')
plt.show()  # shows the graph
# End of part A --------------------------------------------------------------------------------------------------------

print('Part B ')
print('This section of code is displays row_3 histogram of the desired "reasonable" Precipitation levels.')
print()
# Part B----------------------------------------------------------------------------------------------------------------
with open('WeatherDataWindows.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # lines above read in the csv file, then skip the column header
    precipitation = []  # blank points_to_evaluate
    trash = []
    for line in csv_reader:
        precipitation.append(line[-1])  # getting the last column of dta from the csv file

# ---------- Now starting the plot syntax
# .01 for list_passed_in min bc that's where the bins are
plt.figure('Histogram of precipitation')
x_precipitation = [float(i) for i in precipitation]  # easier to look at list_passed_in variable name
plt.axis([0.1, 2, 0, 50])
# the bins here act like the other parameter that must be passed for the graph to actually graph it self.
plt.hist(x_precipitation, rwidth=0.95, label='Precipitation',
         bins=[0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9,
               2.0])  # what we are plotting, the bins display only prices we want and nothing else.
plt.title('Histogram of precipitation levels')  # title
plt.xlabel('Precipitation')  # showing the actual prices from the points_to_evaluate we imported
plt.ylabel('Days')  # indicating how often this happened
plt.legend()  # what our legend is

plt.show()  # showing the plot
# End of Part B --------------------------------------------------------------------------------------------------------

print('Part C')
print('This section of code displays row_3 scatter plot that correlates to the relationship between the temperature and '
      'amount of dew present within the three years of prices.')
print()
# part C----------------------------------------------------------------------------------------------------------------
# this section of code is going to create row_3 scatter plot to display the relationship between the abg temp and avg dew
with open('WeatherDataWindows.csv', 'r')as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # the first few lines here are setting up the to read from the csv file and skipping the header
    avg_temp = []
    avg_dew = []  # two blank points_to_evaluate used to get some prices
    for line in csv_reader:  # loop to get prices
        avg_temp.append(line[2])  # calling in all dta from 'line' 2
        avg_dew.append(line[5])  # bringing in all prices in 'line' 5
    x_avg_temp = [float(i) for i in avg_temp]  # making them numbers and not strings
    y_avg_dew = [float(i) for i in avg_dew]  # converted out the strings and now we are left with numbers

    # ---------- Now starting the plot syntax
plt.figure('Scatter Plot')
plt.scatter(x_avg_temp, y_avg_dew, color='row_4', label=' Temperature & Dew Data')
# type of plot were doing being row_3 scatter plot
plt.xlabel('Temperature')  # list_passed_in label ,temp is the independent variable here
plt.ylabel('Dew')  # y label , the amount of dew relies on the temp info
plt.title('Relationship of Avg Temperature & Avg Dew')  # title of our graph
plt.legend()  # showing the legend
# plt.figure('scatter plot figure')
plt.show()  # must be done to show the graph
# End of Part C --------------------------------------------------------------------------------------------------------

print('Part D')
print('This section of code is going to display 12 months of prices for the three years of prices collected, within the'
      'graph is the avg temp and the error bars.')
print()
# Part D----------------------------------------------------------------------------------------------------------------
jan_data = []
feb_data = []
march_data = []
april_data = []
may_data = []
june_data = []  # making row_3 lot of empty points_to_evaluate for use later on in the file , these points_to_evaluate refer to the
july_data = []  # months of prices to which we will be appending information to very soon
aug_data = []
sept_data = []
oct_data = []
nov_data = []
dec_data = []
with open('WeatherDataWindows.csv', 'r') as csv_file:  # showing the file we are reading from
    csv_reader = csv.reader(csv_file)  # titling what im using to read in the file
    next(csv_reader)  # skips the header info in the csv file
    for line in csv_reader:  # for all the prices in the csv file, read that in... and let the fun begin ;)
        month = line[0].split('/')  # splitting each date into row_3 string

        if month[0] == '1':  # -------------------------- June

            temperature_high = float(line[3])  # this is where the high temp is located
            temperature_low = float(line[1])  # this is where the low temp is located
            jan_data.append(temperature_high)  # appending ALL the information from the high temp column
            jan_data.append(temperature_low)  # appending ALL the information from the low temp column
            jan_max = max(jan_data)  # finding the MAX prices in the previous points_to_evaluate
            jan_min = min(jan_data)  # finding the MAX prices in the previous points_to_evaluate
            jan_avg = sum(jan_data) / len(jan_data)  # finding avg by dividing sum by length of prices for this month

        elif month[0] == '2':  # ------------------------ February

            temperature_high = float(line[3])

            temperature_low = float(line[1])
            feb_data.append(temperature_high)
            feb_data.append(temperature_low)
            feb_max = max(feb_data)
            feb_min = min(feb_data)
            feb_avg = sum(feb_data) / len(feb_data)

        elif month[0] == '3':  # ------------------------ March

            temperature_high = float(line[3])  # this is where the high temp is located
            temperature_low = float(line[1])  # this is where the low temp is located
            march_data.append(temperature_high)  # appending ALL the information from the high temp column
            march_data.append(temperature_low)  # appending ALL the information from the low temp column
            march_max = max(march_data)  # finding the MAX prices in the previous points_to_evaluate
            march_min = min(march_data)  # finding the MAX prices in the previous points_to_evaluate
            march_avg = sum(march_data) / len(
                march_data)  # finding avg by dividing sum by length of prices for this month

        elif month[0] == '4':  # ------------------------ April

            temperature_high = float(line[3])
            temperature_low = float(line[1])
            april_data.append(temperature_high)
            april_data.append(temperature_low)
            april_max = max(april_data)
            april_min = min(april_data)
            april_avg = sum(april_data) / len(april_data)

        elif month[0] == '5':  # ------------------------ May

            temperature_high = float(line[3])  # this is where the high temp is located
            temperature_low = float(line[1])  # this is where the low temp is located
            may_data.append(temperature_high)  # appending ALL the information from the high temp column
            may_data.append(temperature_low)  # appending ALL the information from the low temp column
            may_max = max(may_data)  # finding the MAX prices in the previous points_to_evaluate
            may_min = min(may_data)  # finding the MAX prices in the previous points_to_evaluate
            may_avg = sum(may_data) / len(may_data)  # finding avg by dividing sum by length of prices for this month

        elif month[0] == '6':  # ------------------------ June

            temperature_high = float(line[3])
            temperature_low = float(line[1])
            june_data.append(temperature_high)
            june_data.append(temperature_low)
            june_max = max(june_data)
            june_min = min(june_data)
            june_avg = sum(june_data) / len(june_data)

        elif month[0] == '7':  # ------------------------ July

            temperature_high = float(line[3])  # this is where the high temp is located
            temperature_low = float(line[1])  # this is where the low temp is located
            july_data.append(temperature_high)  # appending ALL the information from the high temp column
            july_data.append(temperature_low)  # appending ALL the information from the low temp column
            july_max = max(july_data)  # finding the MAX prices in the previous points_to_evaluate
            july_min = min(july_data)  # finding the MAX prices in the previous points_to_evaluate
            july_avg = sum(july_data) / len(july_data)  # finding avg by dividing sum by length of prices for this month

        elif month[0] == '8':  # ------------------------- August

            temperature_high = float(line[3])
            temperature_low = float(line[1])
            aug_data.append(temperature_high)
            aug_data.append(temperature_low)
            aug_max = max(aug_data)
            aug_min = min(aug_data)
            aug_avg = sum(aug_data) / len(aug_data)

        elif month[0] == '9':  # ------------------------- September

            temperature_high = float(line[3])  # this is where the high temp is located
            temperature_low = float(line[1])  # this is where the low temp is located
            sept_data.append(temperature_high)  # appending ALL the information from the high temp column
            sept_data.append(temperature_low)  # appending ALL the information from the low temp column
            sept_max = max(sept_data)  # finding the MAX prices in the previous points_to_evaluate
            sept_min = min(sept_data)  # finding the MAX prices in the previous points_to_evaluate
            sept_avg = sum(sept_data) / len(sept_data)  # finding avg by dividing sum by length of prices for this mont
            # h
        elif month[0] == '10':  # ------------------------ October

            temperature_high = float(line[3])
            temperature_low = float(line[1])
            oct_data.append(temperature_high)
            oct_data.append(temperature_low)
            oct_max = max(oct_data)
            oct_min = min(oct_data)
            oct_avg = sum(oct_data) / len(oct_data)

        elif month[0] == '11':  # ------------------------ November

            temperature_high = float(line[3])  # this is where the high temp is located
            temperature_low = float(line[1])  # this is where the low temp is located
            nov_data.append(temperature_high)  # appending ALL the information from the high temp column
            nov_data.append(temperature_low)  # appending ALL the information from the low temp column
            nov_max = max(nov_data)  # finding the MAX prices in the previous points_to_evaluate
            nov_min = min(nov_data)  # finding the MAX prices in the previous points_to_evaluate
            nav_avg = sum(nov_data) / len(nov_data)  # finding avg by dividing sum by length of prices for this month

        elif month[0] == '12':  # ------------------------ December

            temperature_high = float(line[3])
            temperature_low = float(line[1])
            dec_data.append(temperature_high)
            dec_data.append(temperature_low)
            dec_max = max(dec_data)
            dec_min = min(dec_data)
            dec_avg = sum(dec_data) / len(dec_data)

    # ---------- Now starting the plot syntax

    display1 = [jan_min, feb_min, march_min, april_min, may_min, june_min, july_min, aug_min, sept_min, oct_min,
                nov_min, dec_min]  # min prices bar

    display2 = [jan_avg, feb_avg, march_avg, april_avg, may_avg, june_avg, july_avg, aug_avg, sept_avg, oct_avg,
                nav_avg, dec_avg]  # avg prices bar

    display3 = [jan_max, feb_max, march_max, april_max, may_max, june_max, july_max, aug_max, sept_max, oct_max,
                nov_max, dec_max]  # max prices bar

    barWidth = 0.2  # this lets the bars be seen essentially, note: making them to large causes overlap/prices is lost

    range_1 = np.arange(len(display1))  # this makes range_1 = the length of the display points_to_evaluate
    range_2 = [x + barWidth for x in range_1]  # points_to_evaluate comprehension for range_2 , pretty much does the same thing
    range_3 = [x + barWidth for x in range_2]  # again doing the same thing and making row_3 final list_passed_in variable
    plt.figure('Precipitation Figure')
    plt.bar(range_1, display1, width=barWidth, label='Min Temp', color='row_4')  # min prices

    plt.bar(range_2, display2, width=barWidth,  # avg prices
            label='Avg Temp', color='#ffa500')  # being the length of display1 , display_1 , width = our bar width above
    #                                ^^^ decided to play with some hex values here
    plt.bar(range_3, display3, width=barWidth, label='Max Temp', color='r')  # High prices
    plt.xticks([r + barWidth for r in range(len(display1))],
               ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
    # .'xticks' allows the prices to be passed and then arranged so that every bar will be allocated within row_3 single month
    plt.legend()
    plt.xlabel('Months')
    plt.ylabel('Temperature')
    plt.show()  # showing the graph for this prices
# End of Part D --------------------------------------------------------------------------------------------------------
# -----------------------------------------------------GIG'EM-----------------------------------------------------------
