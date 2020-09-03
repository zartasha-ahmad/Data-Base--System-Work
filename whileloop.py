list =[1,2,4,5,3]
a=0
temp= 0
while a < len(list):
    b = a + 1
    while b < len(list):
        if list[a] > list[b]:
            temp = list[a]
            list[a]=list[b]
            list[b]=temp
        b = b + 1
    a = a + 1
print(list)