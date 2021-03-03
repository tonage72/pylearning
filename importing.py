import random

match_number = int(input('number? '))

secret_number = None
try_count = 0

while (match_number != secret_number):
    try_count = try_count + 1
    secret_number = random.randint(1, 1000000)
    print(try_count, secret_number)

print('done')