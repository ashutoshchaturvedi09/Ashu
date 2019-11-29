#condition 1
c = 0
while (c < 5):
    print(c)
    c = c + 1
# 0 1 2 3 4

#Condition 2
C=0
while (C < 5):
    print(C)
    if (C == 3):
        break;
    C = C + 1

#output 0,1,2,3

#conditon 3
d=1
while(d<7):
    d = d + 1
    if(d==3):
        continue
    print(d)
#output 2 4 5 6

#condition 4
e= 7
while(e<11):
    e=e+1
    if(e==8):
        pass
    print(e)

#output  9,10,11