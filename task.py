#1 Задана строка. Необходимо посчитать количество символов
# print("Enter your string: ")
# strr = input()
# n = 0

# for i in strr:
# 	n+=1

# print("Number of symbols is:", n)

#2 Измените порядок символов в строке на обратный.
# print("Enter your string: ")
# strr = input()

# strr = strr[::-1]

# print("New string:", strr)


#3 Найдите подстроку, заключенную в двойных кавычках в строке.

# print("Enter your string: ")
# str1 = input()
# n = False

# for i in str1:
# 	if i == "'":
# 		n = not n
# 	if n and i != "'":
# 		print(i, end="")

#1 В строке записаны два числа, разделенные пробелом. Поменяйте их местами и напечатайте результат.

# print("Enter your string: ")
# str1 = input()
# n = False
# i = 0

# while i < len(str1):
# 	if n:
# 		print(str1[i], end="")
# 	if str1[i] == ' ':
# 		n = not n
# 	i+=1

# i = 0
# print(" ", end="")

# while str1[i] != ' ':
# 	print(str1[i], end="")
# 	i+=1

#2 Из почтового адреса нужно достать логин

# print("Enter your string: ")
# str1 = input()

# for i in str1:
# 	if i == '@':
# 		break
# 	print(i, end="")

#3 Человек вводит на сайте номер телефона, ему позволено для удобства использовать кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы. Уберите их из ввода.

# print("Enter your string: ")
# str1 = input()

# for i in str1:
# 	if i == '-' or i == '(' or i == ')' or i == ' ':
# 		continue
# 	print(i, end="")

#1 Вводится строка. Разделитель слов – пробел. Вывести все слова (на отдельных строках).

# print("Enter your string: ")
# str1 = input()

# for i in str1:
# 	if i == ' ':
# 		print('\n')
# 		continue
# 	print(i, end="")


#2 Вам дана строка, состоящая только из букв английского алфавита и пробелов. Напишите программу, которая определит, является ли строка палиндромом.

# print("Enter your string: ")
# str1 = input()
# i = 0
# j = len(str1)
# b = True

# while i < round(len(str1)/2):
# 	while j > round(len(str1)/2):
# 		if (str1[i] == str1[j-1]):
# 			i+=1
# 			j-=1
# 			break
# 		else: 
# 			b = False
# 			break
# 	break

# if b:
# 	print("Yes")
# else:
# 	print("No")			