list1 = [11,28,39,50,40,50,30,50,12,50,18]
list1.sort()

if len(list1) %2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2-1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)        