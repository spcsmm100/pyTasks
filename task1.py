#На вход подается строка, состоящая из одного числа. Напишите программу, которая удваивает его.
# try:
#	str1 = int(input("Enter the number: "))
# 	print(str1 * 2)	
# except:
# 	print("This is not a number!")

#Вводится число. Вывести его квадрат.
# def square(num):
# 	return num*num
# try:
#	str1 = int(input("Enter the number: "))
# 	print(square(str1))
# except:
# 	print("This is not a number!") 

#Вводятся часы, минуты и секунды. Вывести, сколько секунд прошло с полуночи.
#Вывести, какая часть суток прошла (число от 0 до 1).
# try:
# 	h = int(input("Enter the hours: "))
# 	m = int(input("Enter the minutes: "))
# 	s = int(input("Enter the seconds: "))
# 	print("\nAmount of seconds: ", h*3600 + m*60 + s)
# 	print("Day part: %.4f" %((h*3600 + m*60 + s) / (24*3600)))
# except:
# 	print("You have entered bad!")

#Вводится число. Вывести, оканчивается ли оно на цифру 7, не используя приведение к строке и операции над строками
# try:
# 	num = int(input("Enter the number: "))
# 	print(num % 10 == 7)
# except:
# 	print("This is not a number!") 

#Вводятся коэффициенты уравнения ax2+bx+c=0. Вывести его корни(не забыть проверить, что a не равно 0)

# def discrim(a, b, c):
# 	return b*b - 4*a*c

# try:
# 	a = float(input("Enter a: "))
# 	b = float(input("Enter b: "))
# 	c = float(input("Enter c: "))
# except:
# 	print("You have entered not a numbers!")

# if a == 0:
# 	print("Not a quadratic equation!")
# 	exit()

# d = discrim(a, b, c)
# if d < 0:
# 	print("No roots!")
# 	exit()
# if d == 0:
# 	print("Root is: ", (-b/(2*a)))
# 	exit()

# d = d**0.5
# print("First root is: %.4f" %((-b-d)/(2*a)))
# print("Second root is: %.4f" %((-b+d)/(2*a)))


#Вводятся три числа. Вывести максимум из них.

# try:
# 	arr = [0, 0, 0]
# 	for i in range(3):
# 		arr[i] = float(input("Enter the number: "))
# 	print("Max is: %.0f" % max(arr))
# except:
# 	print("You have entered not a numbers!")


#Вводится число. Вывести среднее арифметическое (с точностью до двух знаков после запятой) тех чисел в диапазоне от единицы до введённого числа, которые делятся 5 или являются четными.

# try:
# 	num = int(input("Enter the number: "))
# 	summ = 0
# 	n = 0
# 	for i in range(num+1):
# 		if i % 5 == 0 or i % 2 == 0:
# 			summ += i
# 			n += 1
# 	n -= 1
# 	print('Sr ar is: %.2f' % (summ/n))
# except:
# 	print("You have entered not a number!")
