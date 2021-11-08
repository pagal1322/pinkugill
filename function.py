# def n(limit):
#     i=0
#     sum=0
#     while i<=limit:
#         if i%3==0:
#             sum+=i
#         elif i%5==0:
#             sum+=i
#         i=i+1
#     print(sum)
# n=int(input("enter your number"))
# n=n


# def is even():
#     if(12%2==0):
#         print("enen number")
#     else:
#         print("odd number")
# is even()


# def a():
#     num=[1,2,3,4,5]
#     print(sum(num))
# a():


# def fact():
# 	i=int(input("enter the mumber"))
# 	fac=1
# 	sum=0
# 	while i>0:
# 		fac=fac*i
# 		i=i-1
# 	print("factorial",fac)
# fact()


# def fact(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return(n*fact(n-1))
# n=int(input("enter no to find factorial"))
# z=fact(n)
# print("factorial=",z


# x=5
# def max(y):
# 	x=3
# 	result=x+y
# 	print(x)
# max(7)
# print(x)


# def convert(lst):
#     return (lst[0].split())
# lst =  ["navgurukul is an alternative to higher education reducing the barriers of current formal education system"]
# print( convert(lst))

# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter += 1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, ]

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list)

# def function():
#     i=1
#     while i<=100:
#         if i%3==0:
#             print(i,"nav")
#         if i%7==0:
#             print(i,"gurukul")
#         if i%21==0:
#             print(i,"navgurukul")
#         else:
#             print(i)
#         i+=1
# function()


# def isHappyNumber(num):    
#     rem = sum = 0;    
        
#     #Calculates the sum of squares of digits    
#     while(num > 0):    
#         rem = num%10;    
#         sum = sum + (rem*rem);    
#         num = num//10;    
#     return sum;    
        
# num = 82;    
# result = num;    
     
# while(result != 1 and result != 4):    
#     result = isHappyNumber(result);    
     
# #Happy number always ends with 1    
# if(result == 1):    
#     print(str(num) + " is a happy number");    
# #Unhappy number ends in a cycle of repeating numbers which contain 4    
# elif(result == 4):    
#     print(str(num) + " is not a happy number");


# def a():
# 	i=1
# 	while i<=1000:
# 		j=1
# 		sum=0
# 		while j<i:
# 			if i%j==0:
# 				sum=sum+j
# 			j=j+1
# 		if sum==i:
# 			print(i)
# 		i=i+1
# a(
# def hersad():
# 	i=1
# 	while i<=1000:
# 		sum=0
# 		n=i
# 		while n>0:
# 			r=n%10
# 			sum=sum+r
# 			n=n//10
# 		if  i%sum==0:
# 			print(i)
# 		i=i+1
# hersad()
