# second homework
#1
print(type(5))
print(type(6.5))
print(type("text"))
print(type({"a","b"}))
print(type(['a','b']))
#2
list1=list(input('введите числа: '))
list2=""
for el in range(len(list1)// 2):
    tmp = list1[el]
    list1[el]=list1[len(list1) - el -1]
    list1[len(list1) - el - 1]=tmp
list2=''.join(list1)
print(list2)
#3
month=int(input('введите номер месяца: '))
my_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
if month <= 0 or month >= 13:
    print('не правильно введен номер месяца')
elif month >0 and month < 13:
    print(my_dict.get(month))

#4
stroka = input('введите несколько слов: ')
slova = stroka.split()
for i, slova in enumerate(slova):
    print(i, slova[:10])

#5
list3 = [7, 5, 3, 3, 2]
zapros = int(input('введите число: '))
for index, number in enumerate(list3):
    if zapros <= list3[index]:
        continue
    list3.insert(index, zapros)
    print(list3)
    break
else:
    list3.append(zapros)
    print(list3)
