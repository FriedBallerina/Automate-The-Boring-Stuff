def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return (number)
    else:
        number = 3 * number + 1
        print(number)
        return (number)
    
users_number = int(input('Enter number:\n'))

result = collatz(users_number)
while result != 1:
    result = collatz(result)