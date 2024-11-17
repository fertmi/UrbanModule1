grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=[] #создание пустого списка
students_list.extend(students) #добавление в список из множества
students_list.sort() #сортировка в списке по алфавиту
students_dict={}
students_dict.update({students_list[0]:sum(grades[0])/len(grades[0])}) #Добавление в словарь первого элемента
students_dict.update({students_list[1]:sum(grades[1])/len(grades[1])}) #Добавление в словарь второго элемента
students_dict.update({students_list[2]:sum(grades[2])/len(grades[2])}) #Добавление в словарь третьего элемента
students_dict.update({students_list[3]:sum(grades[3])/len(grades[3])}) #Добавление в словарь четвертого элемента
students_dict.update({students_list[4]:sum(grades[4])/len(grades[4])}) #Добавление в словарь пятого элемента
print(students_dict)