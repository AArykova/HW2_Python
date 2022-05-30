#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 

list = [1.1, 1.2, 3.1, 5.5, 10.01]

def find_drob(list):
    new_list = []
    for i in list:
        new_list.append(round(i%1, 2))
    return new_list
print(f'Дробные части элементов -  {find_drob(list)}')

def find_max(new_list):
    max = new_list[0]
    for i in range(len(new_list)):
        if new_list[i] > max: max = new_list[i]
    print(f'Максимальный элемент -  {max}')
    return max

def find_min(new_list):
    min = new_list[0]
    for i in range(len(new_list)):
        if new_list[i] < min: min = new_list[i]
    print(f'Минимальный элемент -  {min}')
    return min

def find_diff(list):
    new_list = find_drob(list)
    # maxi = find_max(new_list)
    #mini = find_min(new_list)
    return find_max(new_list) - find_min(new_list) 

print(f'Разность между максимальным и минимальным - {find_diff(list)}') 