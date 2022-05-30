#Написать программу преобразования десятичного числа в двоичное

dec_num = int(input('Введите десятичное число - '))
 

bin_num = bin(dec_num)
print(f'Получено двоичное числол - {bin_num}')
   

# dec_num = int(input('Введите десятичное число - '))

# def find_binary(dec_num):
#     bin_num = ''
#     temp_num = dec_num
#     while temp_num != 0:
#         bin_num += str(temp_num % 2)
#         temp_num //= 2
#     bin_num = bin_num[::-1]
#     return bin_num

# print(find_binary(dec_num))

