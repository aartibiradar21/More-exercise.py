list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list1+=list2
list3=[]
for i in range(len(list1)):
    if list1[i] not in list3:
        list3.append(list1[i])
    i+=1
# list3.sort()
print(list3)


