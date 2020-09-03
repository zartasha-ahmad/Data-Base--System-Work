def sort(List_num):

    for i in range (0,2):
    for i in range (2):
        mini = i
        for j in range (i,3):
            if List_num [j] < List_num [mini]:
                mini = j
        temp = List_num [i]
        List_num [i]= List_num [mini]
        List_num [mini] = temp
        print(List_num)
List_num = [8,5,2]
sort(List_num)
print(List_num)