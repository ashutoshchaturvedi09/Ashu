touple=('a','b')
print(touple)
#Note we can not modify the values
print(touple[0])  # a
print(touple[1]) #b
print(touple[0:1]) # ('a',)
print(touple[0:2]) # ('a','b')
touple1 = ('c','d')
print(touple1) # ('c','d')
touple3= touple+touple1
print(touple3)

del touple3 # will delete touple 3 toupls are immutable , sequantial and can be accessed using index , can add, multiply but not modify them


