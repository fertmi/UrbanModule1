immutable_var = ('String', 10, 2.5, [9,5])
print('Кортеж: ', immutable_var)
# immutable_var[1] = 1 TypeError: 'tuple' object does not support item assignment. Сам кортеж неизменяемый
mutable_list = ['String', 10, 2.5, [9,5]]
print('Список: ',mutable_list)
mutable_list[0]='Change'
print('Измененный список: ',mutable_list)

