# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 3, Act 1
# Date:           9/10/2019

# This program converts number of pounds to number of Newtons
print("This program converts number of pounds to number of Newtons")
pounds_input = float(input("Please enter the number of pounds to be converted to Newtons:"))
# # float must be added because trying to multiply a string by a non-float int cant be complied.
Newtons_output = (pounds_input * 4.4482216)  # 1 pound is 4.4482216 Newtons
print(str(pounds_input)+" Pounds is equivalent to",str(Newtons_output)+"Newtons.")
