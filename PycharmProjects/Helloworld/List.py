shopList=["apple","Oranges","Bananas","Cheese"]
print(shopList)   #Print all the items
print(shopList[0]) # Output :- apple
print(shopList[1])
print(shopList[0:2])
shopList.append("Mango")  #add new item
print(shopList) # output:- apple,oranges,bananas,cheese
del shopList[3]  # delete the item at position 3 i.e. Cheese
print(shopList)
print(len(shopList)) #print length of list

list.reverse(shopList) # reverse the items
print(shopList)  #

print(shopList*2) # double the list of items of list

listnum=[1,4,45,8]
print(max(listnum))  #op 45
print(min(listnum))  # op 1
print(list.sort(listnum)) #
print(listnum)  # sorted list

