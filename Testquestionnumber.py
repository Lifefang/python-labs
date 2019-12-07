items = []
price = []
with open('testing.txt', 'r')as f:
    next(f)
    for line in f:
        price.append(line[6:10])
        items.append(line[0:5])
price = [float(i) for i in price]
min = 9999999999
for i in price:
    if min > i:
        min = i

index_we_want = price.index(min)


print('The items that cost the least is', items[index_we_want], 'with a price tag of', min)
#---------------------------
# file_name = input('Please input the name of the file here:')
# data_entires = int(input('Please indicate how many entires there will be'))
# data = []
# names = []
# while len(data) != data_entires:
#     d = float(input('Please input the score you have in mind:'))
#     data.append(d)
#     n = input('Please input the name you would like to have  in relationship with that grade:')
#     names.append(n)
# mean = sum(data) / data_entires
# counter = 0
# data = [str(i) for i in data]
# with open(file_name, 'w')as f:
#     f.write('Name \t Score \n')
#     for i in range(len(data)):
#         f.write(names[counter] + '\t' + data[counter] + '\n')
#         counter += 1
# print('The avg of the test scores was %.1f' % mean)
# --------------------------------------------------------------------------
odd_list = []
input_1 = int(input('PLease input a single int to start from'))
input_2 = int(input('Please input the second int that the code will end on:'))
for i in range(input_1, input_2 + 1):
    if i % 2 == 1:
        odd_list.append(i)
prime_odd = []
for i in odd_list:
    if isPrime(i):
        prime_odd.append(i)
if len(prime_odd) == 0:
    print('no numbers found cuck')
else:
    print(prime_odd)
