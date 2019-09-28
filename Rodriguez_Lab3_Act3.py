# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-1B
# Date:           9/11/2019
# i hoped in my [color] car to go meet [famous person] in [city] [state]. [famous person] made me [food] but it was
# [temperature in degrees] degrees celsius too hot to eat.
Color = input("Enter your cars color:")
Famous_person = input("Enter your favorite celebrity's name:")
City = input("Enter a city you wish to travel to one day:")
State = input("Enter the state or country that city resides in:")
Food = input("Enter your favorite food:")
Fahrenheit_Input = float(input("enter a temperature in degrees fahrenheit:"))
Celsius_output = (Fahrenheit_Input - 32) * 5 / 9  # one degree in fahrenheit is equal to (F -32)* 5/9
print("\tI hoped in my \b", Color, "car to go meet \b", Famous_person, "\nin \b", City, str(State)+'. \b', Famous_person,
      "made us \b",
      Food,
      "but it was \b", int(Celsius_output), "degrees celsius\ntoo hot to eat.")
