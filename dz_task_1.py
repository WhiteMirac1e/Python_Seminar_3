# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
lst = list(set([x for x in lst if lst.count(x) > 1]))
print(lst) 
