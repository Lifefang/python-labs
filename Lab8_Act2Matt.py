# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-8 Act_2
# Date:           2/10/2019
#NODE 3: LINE EQUATION CALCULATIONS
numerator = ((numPlots) * (sumXtimesY) - (sumX) * (sumY)) # placing the code so that the slope can easily be read
denominator = ((numPlots) * (sumXsquared) - (sumX) ** 2) # whole problem needs to be squared

slope = numerator / denominator # slope = num / dem
intercept = ((sumY) - (slope) * (sumX)) / (numPlots) # intercept for the code
