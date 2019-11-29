students={"Ashu":28}
print(students)
print(students["Ashu"])
students["Ashu"]= 29
print(students)
print(len (students))

#note If we have 3 items of same key then it will pick last value example {"Ashu":12,"Ashu":13,"Ashu":14}  it will print Ashu:14 (last value)
students["Rahul"]=21 #add another item to dictionary
print(students)
del students["Rahul"] #delete item from dictionary
print(students)