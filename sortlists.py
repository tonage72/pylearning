numbers = [31, 2, 43, 0, 9, 10]
letters = ['b', 'c', 'e', 'd']
edutainers = ['Jo', 'Justin', 'Vonne', 'Cherokee']

print('Numbers:', numbers)
print('Letters:', letters)
print('Edutainers:', edutainers)

#How do I put a list in "ascending" order?

#numbers.sort()
sorted_numbers = sorted(numbers)
print('Sorted Numbers:', sorted_numbers)
print('Numbers:', numbers)

sorted_edutainers = sorted(edutainers)
print('Sorted Edutainers:', sorted_edutainers)
print('Edutainers:', edutainers)

#List in decending order
sorted_letters = sorted(letters)
des_letters = sorted(letters, reverse=True)
print(letters)
print(sorted_letters)
print(des_letters)

#How do I flip a list? (Reversing)
reversed_edutainers = list(reversed(edutainers))
print(edutainers)
print(reversed_edutainers)

edutainers.reverse()
print(edutainers)
edutainers.reverse()
print(edutainers)