import time
start = time. time()

num = 0
Sum = 0

while num < 101:
    Sum = Sum + num
    num += 1

print(Sum)

end = time. time()
print(end - start)