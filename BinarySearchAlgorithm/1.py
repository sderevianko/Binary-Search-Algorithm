massive = list(range(1, 21))
key = input('Input number from 1 till 20:  ')
key = int(key)
last = len(massive)
print("last", last)
print("key", key)
print(massive)
first = massive[0]
average = (first + last) / 2
x = 0
while key != x and key != first and key != last and key != average:
    if key < average:
        last = round(average)
        if last == key:
            x = last
        if first == key:
            x = first
        if average == key:
            x = average
    if key > average:
        first = round(average)
        if first == key:
            x = first
        if last == key:
            x = last
        if average == key:
            x = average
    if key == average:
        x = average
    average = (first + last) / 2
if first == key:
    x = first
if last == key:
    x = last
if average == key:
    x = average
print("key =", key, "x =", round(x),"index x =", round(x-1))
