array = list(range(1, 21))
key = input('Input number from 1 till 20:  ')
key = int(key)
first = array[0]
last = len(array)
print(array)
average = (first + last) / 2
x = 0
while key != x and key != first and key != last:
    if key < average:
        last = round(average)
        if last == key:
            x = last
        if first == key:
            x = first
    if key > average:
        first = round(average)
        if first == key:
            x = first
        if last == key:
            x = last
    if key == average:
        x = average
    average = (first + last) / 2
if first == key:
    x = first
if last == key:
    x = last
print("key =", key, "x =", round(x),"index x =", round(x-1))
