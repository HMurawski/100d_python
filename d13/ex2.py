number = int(input('pick a number: '))

if number % 2 == 0:
    print('even')
else:
    print('odd')




year = int(input('pick a year: '))

if year % 4 == 0 or year % 100 ==0 or year % 400 == 0:
    print('leap year')
else:
    print('not leap year')



target = int(input('give a random number: '))

for number in range (1,target +1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 ==0:
        print('fizz')
    elif number %5 ==0:
        print('buzz')
    else:
        print(number)