#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

list = [2, 3, 4, 5, 6]

def find_composition(list):
    new_list = []
    last = len(list) - 1 
    for i in range(0, (last//2) + 1):
        temp = list[i] * list[last]
        new_list.append(temp)
        last-=1
    return new_list

print(f'{list} => {find_composition(list)}')