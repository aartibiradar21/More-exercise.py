# list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# length=len(list)
# i=0
# while i<length:
#     j=0
#     while j<len(list[i]):
#         print(list[i][j])
#         j+=1
#     i=i+1
 
list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
i=0
b=[]
while i<len(list):
    j=0
    max=list[i][j]
    while j<len(list[i]):
        if max<list[i][j]:
            max=list[i][j]
        j=j+1
    i=i+1
    print(max)




# i=0
# b=[]
# while i<len(list):
#     j=0
#     max=list[i][j]
#     while j<len(list[i]):
#         if max<len[i][j]:
#             max=list[i][j]
#         j=j+1
#     i=+1
#     print(list)