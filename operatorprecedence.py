#Memebership tests

edutainers = ['Vonne', 'Justin', 'Aubri', 'Ronnie']
print('Daniel in Edutainers:', 'Daniel' in edutainers)
print('Aubri in Edutainers:', 'Aubri' in edutainers)
print('Daniel not in Edutainers:', 'Daniel' not in edutainers)

#Identity tests
favorite_food = 'cheese'
lunch_today = 'cheese'
print(favorite_food is lunch_today)
other_edutainers = ['Vonne', 'Justin', 'Aubri', 'Ronnie']
print(edutainers is other_edutainers)
print(edutainers is edutainers)

#Not operator
print(not 1 == 1)
print(1 != 1)

#Precedence
print(4 * 3 + 1)