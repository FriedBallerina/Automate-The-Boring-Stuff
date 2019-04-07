message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1
    
print(count)