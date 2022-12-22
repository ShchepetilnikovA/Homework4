lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
lst2 = []
for i in lst:
    count = len(lst)
    for j in lst:
        if i != j:
            count -= 1
            if count < 2:
                lst2.append(i)
print(lst2)
