# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

max_weight = 1000 
lst = {'зажигалка' : 10, 'нож' : 200, 'вода' : 1000, 'еда' : 500,
        'одежда' : 400, 'кастрюля' : 2000, 'ноутбук' : 2500}
pos_items = []
for item, weight in lst.items():
    if weight <= max_weight:
        pos_items.append(item)
        max_weight -= weight
print(pos_items)
