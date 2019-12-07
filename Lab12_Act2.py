# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 12 act 2
# Date:           10/29/19
import numpy as np

function = input('Please enter a function as you would see it, example, x** 3 -x**2 + x -2 :')
# Getting the users functions
range1 = int(input('What is the starting point of the range?'))  # getting desired starting range
range2 = int(input('What is the endpoint of the range?'))  # getting desired end range


# -----------------------------------------------------------------------------------------------------------------------
# THIS IS FOR SECTION ONE Start of the graph
def method_one(x, range_1, range_2):
    list_of_areas_until_tol_met = []  # this is an empty list that will eventually become full of areas
    difference = 10 ** 6  # setting the difference to some high value for the first few iterations, will be subject to
    # change within a few iterations
    toleration = 10 ** -6  # this was the requested tolerance
    loop_counter = 0  # this is the number of how many times we have entered the loop. will be displayed at the end
    extra_counter = 0  # this extra counter is used withing a list to grab the lists index we want specifically
    num_rectangles = 10  # what we should start at
    while difference > toleration:  # this is where all the magic happens
        loop_counter += 1  # before anything is done at all, the counter is to go up

        if loop_counter > 2:  # after we have gone through 2 loops, and NOT BEFORE , we do this because you need two
            # things to get a difference from, so we wait until there are 2 areas to work with
            difference = (list_of_areas_until_tol_met[extra_counter] - list_of_areas_until_tol_met[extra_counter + 1])
            extra_counter += 1  # this is keeping track of the elements that are being subtracted above

        points_to_evaluate = np.linspace(range1, range2, num_rectangles + 1)  # evaluating all the points from the
        # first range to the second range, total_area number of times as the number of rectangles is going to
        # increase every time through the loop
        delta_x = points_to_evaluate[1] - points_to_evaluate[0]  # delta tally_mark_input= element[1] - element[0]
        delta_x = round(delta_x, 8)  # Very important , we rounded here because the numbers become so massive that
        # python slows down tremendously, the point will converge without this rounding implements but it
        # significantly speeds up the time.
        index = [-1]  # syntax for getting rid of things with numpy
        points_to_evaluate = np.delete(points_to_evaluate, index)
        # getting rid of the last index, as it does not exist using this method

        area = []  # a blank list used to hold areas evey time we go through the loop
        for i in points_to_evaluate:
            x = i  # setting up the eval function
            doing_the_math = delta_x * eval(function)
            # this is evaluating all the points within the list of points to evaluate
            area.append(doing_the_math)  # getting a list off all the areas of all the rectangles

        total_area = list(area)
        # it was difficult to work with numpy on this one so area is converted to the class list and assigned to a
        # different variable name
        area_for_this_iteration = sum(total_area)
        # # sum of the list is the area we received for this many number of squares

        list_of_areas_until_tol_met.append(area_for_this_iteration)
        # will be used to get the difference
        num_rectangles += 1  # this needs to go up

    display = '%.2f' % list_of_areas_until_tol_met[-1]  # area number nicely rounded up
    return 'It took', loop_counter, 'iterations to achieve convergence and obtain an area of:', abs(display)
    # the return can never be a negitive value, this just means that the calculated area is on quadrant two


# This IS FOR SECTION TWO End
def method_two(x, range_1, range_2):
    list_of_areas_until_tol_met = []  # this is an empty list that will eventually become full of areas
    difference = 10 ** 6  # setting the difference to some high value for the first few iterations, will be subject to
    # change within a few iterations
    toleration = 10 ** -6  # this was the requested tolerance
    loop_counter = 0  # this is the number of how many times we have entered the loop. will be displayed at the end
    extra_counter = 0  # this extra counter is used withing a list to grab the lists index we want specifically
    num_rectangles = 10  # what we should start at
    while difference > toleration:  # this is where all the magic happens
        loop_counter += 1  # before anything is done at all, the counter is to go up

        if loop_counter > 2:  # after we have gone through 2 loops, and NOT BEFORE , we do this because you need two
            # things to get a difference from, so we wait until there are 2 areas to work with
            difference = (list_of_areas_until_tol_met[extra_counter] - list_of_areas_until_tol_met[extra_counter + 1])
            extra_counter += 1  # this is keeping track of the elements that are being subtracted above

        points_to_evaluate = np.linspace(range1, range2, num_rectangles + 1)  # evaluating all the points from the
        # first range to the second range, total_area number of times as the number of rectangles is going to
        # increase every time through the loop
        delta_x = points_to_evaluate[1] - points_to_evaluate[0]  # delta tally_mark_input= element[1] - element[0]
        delta_x = round(delta_x, 8)  # Very important , we rounded here because the numbers become so massive that
        # python slows down tremendously, the point will converge without this rounding implements but it
        # significantly speeds up the time.
        index = [0]  # syntax for getting rid of things with numpy
        points_to_evaluate = np.delete(points_to_evaluate, index)
        # getting rid of the last index, as it does not exist using this method

        area = []  # a blank list used to hold areas evey time we go through the loop
        for i in points_to_evaluate:
            x = i  # setting up the eval function
            doing_the_math = delta_x * eval(function)
            # this is evaluating all the points within the list of points to evaluate
            area.append(doing_the_math)  # getting a list off all the areas of all the rectangles

        total_area = list(area)
        # it was difficult to work with numpy on this one so area is converted to the class list and assigned to a
        # different variable name
        area_for_this_iteration = sum(total_area)
        # # sum of the list is the area we received for this many number of squares

        list_of_areas_until_tol_met.append(area_for_this_iteration)
        # will be used to get the difference
        num_rectangles += 1  # this needs to go up

    display = '%.2f' % list_of_areas_until_tol_met[-1]  # area number nicely rounded up
    return 'It took', loop_counter, 'iterations to achieve convergence and obtain an area of:', abs(display)
    # the return


# THIS IS FOR SECTION THREE THE MID INTERVAL
def method_three(x, range_1, range_2):
    list_of_areas_until_tol_met = []  # this is an empty list that will eventually become full of areas
    difference = 10 ** 6  # setting the difference to some high value for the first few iterations, will be subject to
    # change within a few iterations
    toleration = 10 ** -6  # this was the requested tolerance
    loop_counter = 0  # this is the number of how many times we have entered the loop. will be displayed at the end
    extra_counter = 0  # this extra counter is used withing a list to grab the lists index we want specifically
    num_rectangles = 10  # what we should start at
    while difference > toleration:  # this is where all the magic happens
        loop_counter += 1  # before anything is done at all, the counter is to go up

        if loop_counter > 2:  # after we have gone through 2 loops, and NOT BEFORE , we do this because you need two
            # things to get a difference from, so we wait until there are 2 areas to work with
            difference = (list_of_areas_until_tol_met[extra_counter] - list_of_areas_until_tol_met[extra_counter + 1])
            extra_counter += 1  # this is keeping track of the elements that are being subtracted above

        points_to_evaluate = np.linspace(range1, range2, num_rectangles + 1)  # evaluating all the points from the
        # first range to the second range, total_area number of times as the number of rectangles is going to
        # increase every time through the loop
        delta_x = points_to_evaluate[1] - points_to_evaluate[0]  # delta tally_mark_input= element[1] - element[0]
        delta_x = round(delta_x, 8)  # Very important , we rounded here because the numbers become so massive that
        mean_list_for_points_to_evaluate = []  # under the delta tally_mark_input
        mean_counter = 0  # used to calculate the mean list
        for i in points_to_evaluate:
            data = 1 / 2 * delta_x + delta_x * mean_counter  # formula = delta tally_mark_input +( delta tally_mark_input * length of rectangle
            # number)
            mean_counter += 1  # needs to go up every iteration
            mean_list_for_points_to_evaluate.append(data)  # points were going to actually use for the equation below

        area = []
        for i in points_to_evaluate:
            x = i  # setting up the eval function
            doing_the_math = delta_x * eval(function)
            # this is evaluating all the points within the list of points to evaluate
            area.append(doing_the_math)  # getting a list off all the areas of all the rectangles

        total_area = list(area)  # a blank list used to hold areas evey time we go through the loop
        # it was difficult to work with numpy on this one so area is converted to the class list and assigned to a
        # different variable name
        area_for_this_iteration = sum(total_area)
        # # sum of the list is the area we received for this many number of squares

        list_of_areas_until_tol_met.append(area_for_this_iteration)
        # will be used to get the difference
        num_rectangles += 1  # this needs to go up

    display = '%.2f' % list_of_areas_until_tol_met[-1]  # area number nicely rounded up
    return 'It took', loop_counter, 'iterations to achieve convergence and obtain an area of:', abs(display)
    # the return


# under this is method 4 of taking area of rhombuses
def method_four(x, range_1, range_2):
    list_of_areas_until_tol_met = []  # this is an empty list that will eventually become full of areas
    difference = 10 ** 6  # setting the difference to some high value for the first few iterations, will be subject to
    # change within a few iterations
    toleration = 10 ** -6  # this was the requested tolerance
    loop_counter = 0  # this is the number of how many times we have entered the loop. will be displayed at the end
    extra_counter = 0  # this extra counter is used withing a list to grab the lists index we want specifically
    num_rectangles = 10  # what we should start at
    while difference > toleration:  # this is where all the magic happens
        loop_counter += 1  # before anything is done at all, the counter is to go up

        if loop_counter > 2:  # after we have gone through 2 loops, and NOT BEFORE , we do this because you need two
            # things to get a difference from, so we wait until there are 2 areas to work with
            difference = (list_of_areas_until_tol_met[extra_counter] - list_of_areas_until_tol_met[extra_counter + 1])
            extra_counter += 1  # this is keeping track of the elements that are being subtracted above

        points_to_evaluate = np.linspace(range1, range2, num_rectangles + 1)  # evaluating all the points from the
        # first range to the second range, total_area number of times as the number of rectangles is going to
        # increase every time through the loop
        delta_x = points_to_evaluate[1] - points_to_evaluate[0]  # delta tally_mark_input= element[1] - element[0]
        delta_x = round(delta_x, 8)  # Very important , we rounded here because the numbers become so massive that
        # python slows down tremendously, the point will converge without this rounding implements but it
        # significantly speeds up the time.

        area = []  # a blank list used to hold areas evey time we go through the loop
        for i in points_to_evaluate:
            # splits into many different if statements due to how the formula is calculated
            # equation = 1 f(tally_mark_input) + 2f(tally_mark_input) .....until the last element always do times 2, 1 * f([-1)
            if i == points_to_evaluate[0]:  # if its the first element in the list
                x = i  # setting up the eval function
                doing_the_math = eval(function)  # evaluating the function at all points
                step_2_of_math = (1 / 2) * delta_x * doing_the_math  # broke this math up for neatness
                area.append(step_2_of_math)  # getting a list off all the areas of all the rectangles
            elif i == points_to_evaluate[-1]:
                x = i  # setting up the eval function
                doing_the_math = eval(function)  # evaluating the function at all points
                step_2_of_math = (1 / 2) * delta_x * doing_the_math  # broke this math up for neatness
                area.append(step_2_of_math)  # getting a list off all the areas of all the rectangles

            else:
                x = i  # setting up the eval function
                doing_the_math = 2 * eval(function)  # evaluating the function at all points * 2
                step_2_of_math = (1 / 2) * delta_x * doing_the_math  # broke this math up for neatness
                area.append(step_2_of_math)  # getting a list off all the areas of all the rectangles

        total_area = list(area)
        # it was difficult to work with numpy on this one so area is converted to the class list and assigned to a
        # different variable name
        area_for_this_iteration = sum(total_area)
        # # sum of the list is the area we received for this many number of squares

        list_of_areas_until_tol_met.append(area_for_this_iteration)
        # will be used to get the difference
        num_rectangles += 1  # this needs to go up

    display = '%.2f' % list_of_areas_until_tol_met[-1]  # area number nicely rounded up
    return 'It took', loop_counter, 'iterations to achieve convergence and obtain an area of:', abs(display)
    # the return


print(method_one(function, range1, range2))
print()
print(method_two(function, range1, range2))
print()
print(method_three(function, range1, range2))
print()
print(method_four(function, range1, range2))
