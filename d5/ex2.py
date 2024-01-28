# for number in range(a,b):
#     print(number)
# all_sum = 0
# for num in range (1,101):
#     all_sum += num
# print(all_sum)


input_num = int(input("Give max-range number: "))

total = 0
for number in range(2, input_num + 1, 2):
    total += number
print(total)