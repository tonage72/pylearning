total = 4
count = 2
#main program
try:
    average = total / count
    print('Average is: ', average)
except ZeroDivisionError as e:
    print('Cannot divide zero', e)
finally:
    print('Save my progress')