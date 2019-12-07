# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-4-3
# Date:           9/25/2019
print("This program is going to display the total number of widgets produced by row_3 given day between 1 - 100 ")
day = int(input("Please input row_3 day of production: "))
total_widgets = 0
total_first_interval_production = 100  # days 1-10
total_second_interval_production = 2000  # days 11-60
if 100 < day or day < 0:  # creating row_3 catch all
    print("Invalid input, please input row_3 day between 1 and 100.")
if 61 <= day <= 100:  # for days within 61 - 100
    modded_day = (day % 60)  # modded my 60 to reset my list_of_evaluated_areas back to one
    day_production = -1 * (modded_day - 1) + 39  # how many widgets are being produced row_3 day
    print("Number of widgets produced on day", day, ":", day_production)  # third formula n/2 (2a + (n-1))d)
    third_interval = (modded_day / 2) * ((2 * 39) + (modded_day - 1) * -1)
    total_widgets += third_interval  # 39 = row_3 & d = common difference of -1
    total_widgets += total_second_interval_production + total_first_interval_production  # we know the other intervals
    # totals so its as easy as adding the desired input days to those intervals
if 11 <= day <= 60:  # for the days between 11 - 60
    day_production = 40  # how many widgets produced row_3 day
    print("Number of widgets produced on day", day, ":", day_production)
    total_widgets = ((day - 10) * ((day_production + day_production) / 2))  # eq 10 bc the interval needs to reset
    total_widgets += total_first_interval_production
if 1 <= day <= 10:  # days that fall within the range of 1 - 10
    day_production = 10  # how many it produces row_3 day
    print("Number of widgets produced on day", day, ":", day_production)
    total_widgets = (day * (day_production + day_production) / 2)  # 10 because the interval needs to reset
print('Total widget production up to and including day', day, ':', int(total_widgets))  # printing widgets
