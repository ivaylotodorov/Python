for item in 'Hello':
    print(item)

for number in [1, 2, 3]:
    for letter in ['a', 'b', 'c']:
        print(number, letter)

print(" ")


my_list = list(range(1, 11))
counter = 0
for item in my_list:
    counter += item
print(counter)
