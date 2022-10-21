#1 Вводится вектор. Вывести максимум из его элементов.
#Ввод: 3 67 5 8
#Вывод: 67
# vector=input()
# vector_list=[int(x) for x in vector.split()]
# print(max(vector_list))

# #2 Вводится вектор. Заменить в нём каждое число Фибоначчи на следующее.
# #Ввод: 1 3 5 7 87 12 56 13
# #Вывод:[2, 5, 8, 7, 87, 12, 56, 21]
# def check1(x):
#   return ((5*(x**2)+4)**0.5)%1==0
# def check2(x):
#   return ((5*(x**2)-4)**0.5)%1==0
# arr=input()
# arrl=[int(x) for x in arr.split()]
# for i in range(len(arrl)):
#   if check1(arrl[i]) or check2(arrl[i]):
#     fib=[1,1]
#     k=1
#     s=arrl[i]
#     while fib[k]<=s:
#       fib.append(fib[k-1]+fib[k])
#       if fib[k]==s:
#         arrl[i]=fib[k+1]
#       k+=1
# print(arrl)

# #3 Напишите программу, которая помогает определить какие вещи могут поместиться в рюкзак. Вводится существующий объем рюкзака. Затем вводятся объемы всех вещей, которые хочется туда поместить. Нужно вывести список объемов вещей, которые поместятся в рюкзак. Постарайтесь максимизировать кол-во вошедших вещей.
# #Ввод:85
#	23 5 66 32 4 76 13 5 65 
# #Вывод: [4, 5, 5, 13, 23, 32]
# volume=int(input())
# objects=input()
# objects_list=[int(x) for x in objects.split()]
# objects_list.sort()
# total_sum=0
# objects_sum=[]
# for i in range(len(objects_list)):
#   if total_sum+objects_list[i]<volume:
#     total_sum+=objects_list[i]
#     objects_sum.append(objects_list[i])
# print(objects_sum)

# #4 Данные об email-адресах студентов хранятся в словаре: {домен:логины} . Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен
# #Ввод:
# #Вывод:
# domens={'rea.ru': ['misha', 'pasha'], 'study.com': ['olga', 'nastay', 'igor']}
# i=0
# total_list=[]
# for dom, logins in domens.items():
#   i+=1
#   logins=str(logins)[1:len(str(logins))-1]
#   logins_list=logins.split(', ')
#   for k in range(len(logins_list)):
#     total_list.append(logins_list[k][1:len(logins_list[k])-1]+'@'+dom)
# print(sorted(total_list))