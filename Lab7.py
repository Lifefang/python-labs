c
list_1 = input("Please input row_3 string of integers separated by row_3 single space for points_to_evaluate one:").split()
list_A = []
for i in list_1:
    list_A.append(int(i))
# # this is the done section of the points_to_evaluate process
# sorted(list_A)  # ----------------------------> Using the sorted command to sort out the points_to_evaluate
# # --------------------------------------------> This section of code is for points_to_evaluate one
# if len(list_A) % 2 == 0:  # ------------------> If the length of the points_to_evaluate modded by 2 = 0 , its even
#     list_A = 'True'  # -----------------------> Assigning it to an arbitrary string used further down in the code
# elif len(list_A) % 2 == 1:  # ----------------> If the length of the points_to_evaluate modded by 2 = 1 , its odd
#     list_A = 'False'  # ----------------------> Assigning it to an arbitrary string used further down in the code
iterations = 0
for i in list_A:
    iterations += 1
if iterations % 2 ==0:
    list_A = "False"
elif iterations % 2 == 1:
    list_A = "True"

if list_A == "True":
    mean_list = []
    for i in list_A:
        mean_list.append(i)
    while len(mean_list) > 2:
        mean_list.pop(0)
        mean_list.pop(-1)
    mean = (int(mean_list[0]) + int(mean_list[1]))/2
    print(mean)
elif list_A == 'False':
    mean_list = []
    for i in list_A:
        mean_list.append(i)
    while len(mean_list) > 1:
        mean_list.pop(0)
        mean_list.pop(-1)
        print(int(mean_list[0]))
