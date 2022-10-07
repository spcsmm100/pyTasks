#1
# print("Enter your string: ")
# strr = input()
# n = 0

# for i in strr:
# 	n+=1

# print("Number of symbols is:", n)

#2
# print("Enter your string: ")
# strr = input()

# strr = strr[::-1]

# print("New string:", strr)


#3

# print("Enter your string: ")
# str1 = input()
# n = False

# for i in str1:
# 	if i == "'":
# 		n = not n
# 	if n and i != "'":
# 		print(i, end="")

#1

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

#2

# print("Enter your string: ")
# str1 = input()

# for i in str1:
# 	if i == '@':
# 		break
# 	print(i, end="")

#3

# print("Enter your string: ")
# str1 = input()

# for i in str1:
# 	if i == '-' or i == '(' or i == ')' or i == ' ':
# 		continue
# 	print(i, end="")

#1

# print("Enter your string: ")
# str1 = input()

# for i in str1:
# 	if i == ' ':
# 		print('\n')
# 		continue
# 	print(i, end="")


#2

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