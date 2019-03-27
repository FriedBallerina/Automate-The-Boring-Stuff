import time
from random import *
start = time.time()

number = randint(1, 100)
#int(input("Insert the number for the calculation of total sum of the number and the preceding numbers: "))
print('Number is ' + str(number))
def Sum(user_input):
    total = int((number ** 2 + number) / 2)
    print('The sum is: ' + str(total))
    
Sum(number)

end = time.time()
print(end - start)