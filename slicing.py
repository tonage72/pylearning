letters = list('abcdefghijklmnop')

print(letters)

#How do I get the letter 'c' through 'f'?

selected = letters[2:6]
print(selected)

#How do I get every other letter from the list?

every_other = letters[::2]
print(every_other)

#Bonus: Reverse with Slices
reverse_letters = letters[::-2]
print('Reversed:', reverse_letters)