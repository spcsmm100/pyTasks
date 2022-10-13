#На вход подается строка, состоящая из одного числа. Напишите программу, которая удваивает его.
# Input 646 Output 1292
# try:
#	str1 = int(input("Enter the number: "))
# 	print(str1 * 2)	
# except:
# 	print("This is not a number!")

#Вводится число. Вывести его квадрат.
# Input 23 Output 529
# def square(num):
# 	return num*num
# try:
#	str1 = int(input("Enter the number: "))
# 	print(square(str1))
# except:
# 	print("This is not a number!") 

#Вводятся часы, минуты и секунды. Вывести, сколько секунд прошло с полуночи.
#Вывести, какая часть суток прошла (число от 0 до 1).
#Input 19 54 12 Output 0.8293
# try:
# 	h = int(input("Enter the hours: "))
# 	m = int(input("Enter the minutes: "))
# 	s = int(input("Enter the seconds: "))
# 	t = h*3600 + m*60 + s
# 	print("\nAmount of seconds: ", t)
# 	print("Day part: ", round((t / (24*3600)), 4))
# except:
# 	print("You have entered bad!")

#Вводится число. Вывести, оканчивается ли оно на цифру 7, не используя приведение к строке и операции над строками
# Input 345437 Output TRUE
# try:
# 	num = int(input("Enter the number: "))
# 	print(num % 10 == 7)
# except:
# 	print("This is not a number!") 

#Вводятся коэффициенты уравнения ax2+bx+c=0. Вывести его корни(не забыть проверить, что a не равно 0)
#Input 0, 1, 2 Output -2.0
#Input 6, 16, 26 Output -3.8054 1.1387
#Input -4 28 -49 Output 3.5

# def discrim(a, b, c):
# 	return b*b - 4*a*c

# try:
# 	a = float(input("Enter a: "))
# 	b = float(input("Enter b: "))
# 	c = float(input("Enter c: "))
# except:
# 	print("You have entered not a numbers!")

# if a == 0:
# 	print("Root is: ", -c/b)
# 	exit()

# d = discrim(a, b, c)
# if d < 0:
# 	print("No roots!")
# 	exit()
# if d == 0:
# 	print("Root is: ", (-b/(2*a)))
# 	exit()

# d = d**0.5
# print("First root is: ", round(((-b-d)/(2*a)), 4))
# print("Second root is: ", round(((-b+d)/(2*a)), 4))


#Вводятся три числа. Вывести максимум из них.
#Input 4 14 5 Output 14
# try:
# 	arr = [0, 0, 0]
# 	for i in range(3):
# 		arr[i] = float(input("Enter the number: "))
# 	print("Max is: ", round(max(arr), 0))
# except:
# 	print("You have entered not a numbers!")


#Вводится число. Вывести среднее арифметическое (с точностью до двух знаков после запятой) тех чисел в диапазоне от единицы до введённого числа, которые делятся 5 или являются четными.
#Input 23 Output 11.69
# try:
# 	num = int(input("Enter the number: "))
# 	summ = 0
# 	n = 0
# 	for i in range(num+1):
# 		if i % 5 == 0 or i % 2 == 0:
# 			summ += i
# 			n += 1
# 	n -= 1
# 	print('Sr ar is: ', round((summ/n), 2))
# except:
# 	print("You have entered not a number!")
