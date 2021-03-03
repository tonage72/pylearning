numbers = [1, 2, 3, 4]
letters = 'abcd'

#for number, letter in zip(numbers, letters):
#    print(number, letter)

#for number in numbers:
#    for letter in letters:
#        for i in range(10):
#            if letter == 'a' and number == 1:
#                for i in range(10):
#                    print(number, letter, i)

days = [
    list(range(3)),
    list(range(4)),
    list(range(5))
]

total = 0
for day in days:
    for sale in day:
        print(total, ': ', sale)
        total = total + sale
print(total)
