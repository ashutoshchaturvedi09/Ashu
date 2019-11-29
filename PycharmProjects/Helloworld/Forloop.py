List1 = ["apple", "bananas", "mangoes"]
touple1 = (1, 2, 3, 4, 5)

for item in List1:
    print(item)  # apple  bananas mangoes

for item in touple1:
    print(item)  # 1 2 3 4 5

for i in range(0, 10):
    print(i)  # 1 2 3 4 5 6 7 8 9

for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

for i in range(5, 51, 5):
    print(i)  # 5 10  15 20 25 30 35 40 45 50

# Nested for loop

for i in range(0, 5):
    for j in range(0, 5):
        print(i*j)
