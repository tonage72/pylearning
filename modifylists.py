edutainers = ['Adam', 'Aubri', 'Daniel', 'Jo']

#How do I add an element to the end of a list?
print('Edutainers: ', edutainers)
edutainers.append('Justin')
print('Edutainers: ', edutainers)

#How do I remove an element from a list?
del edutainers[0]
print('Edutainers: ', edutainers)

#Remove elements from end of list?
special = edutainers.pop()
print('Edutainers: ', edutainers)
print('Special: ', special)

#Change element
edutainers[2] = 'Dan'
print('Edutainers: ', edutainers)