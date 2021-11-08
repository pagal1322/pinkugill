
r=1
while r<=5:
	c=1
	while c<=9:
		if (r==1 and c==4):
			print('s',end=' ')
		elif (r==2 and c==4) or (r==2 and c==5) or(r==2 and c==6):
			print('a',end=' ')
		elif (r==3 and c==3) or (r==3 and c==4) or (r==3 and c==5) or (r==3 and c==6) or (r==3 and c==7):
			print('p',end=' ')
		elif(r==4 and c==2) or (r==4 and c==3) or (r==4 and c==4) or (r==4 and c==5) or (r==4 and c==6) or (r==4 and c==7) or (r==4 and c==8):
				print('n',end=' ')
		elif(r==5 and c==1) or (r==5 and c==2) or (r==5 and c==3) or (r==5 and c==4) or (r==5 and c==5) or (r==5 and c==6) or (r==5 and c==7) or (r==5 and c==8) or (r==5 and c==9):
				print('a',end=' ')
		c=c+1
	print()
	r=r+1



num=int(input("enter a number"))
i=1
a=[]
while i<=num:
	j=0
	b=[]
	while j<=10:
		x=i*j
		b.append(x)
		j=j+1
	a.append(i)
	a.append(b)
	i=i+1
print(a)
4:08 PM
Forwarded
row=1
start=9
while row<=5:
	print(" "*start,end=" ")
	column=row
	while column>1:
		print(row,end=" ")
		column=column-1
	kounter=1
	while kounter<=row:
		print(row,end=" ")
		kounter=kounter+1
	print()
	start=start-2
	row=row+1



num=int(input("enter a number"))
i=1
while i<10:
	j=1
	while j<num:
		print(j*num,"=",i*num)
		j=j+1
	i=i+1
	
	Table💝💝💝
  
  
  
r=1
while r<=5:
	c=1
	while c<=9:
		if (r==1 and c==4):
			print('s',end=' ')
		elif (r==2 and c==4) or (r==2 and c==5) or(r==2 and c==6):
			print('a',end=' ')
		elif (r==3 and c==3) or (r==3 and c==4) or (r==3 and c==5) or (r==3 and c==6) or (r==3 and c==7):
			print('p',end=' ')
		elif(r==4 and c==2) or (r==4 and c==3) or (r==4 and c==4) or (r==4 and c==5) or (r==4 and c==6) or (r==4 and c==7) or (r==4 and c==8):
				print('n',end=' ')
		elif(r==5 and c==1) or (r==5 and c==2) or (r==5 and c==3) or (r==5 and c==4) or (r==5 and c==5) or (r==5 and c==6) or (r==5 and c==7) or (r==5 and c==8) or (r==5 and c==9):
				print('a',end=' ')
		else:
			print(' ',end=' ')
		c=c+1
	print()
	r=r+1


a=int(input("enter a number"))
i=2
b=10
while i<9:
	print(b,i,end=" ")
	i=i+2
	b=b+10
print(i)



i=1
while i<100:
	j=1
	c=0
	while j<=i:
		if i%j==0:
			c=c+1
		j=j+1
	if c==2:
		print(i)
	i=i+1
1 to 100 tak prime no👍👍👍



i=1
while i<=10:
	if i==5:
		break
	print(i)
	i=i+1
Break 💓💓�


n=int(input("enter a number of rows"))
for i in range(n):
	print((chr(65+i)+' ')*(i+1))
	Ascii value 🥰🥰🥰🥰abcdprint


i=1
k=1
while i<=4:
	j=1
	while j<=5:
		print(k,end=" ")
		k+=1
		j+=1
	print()
	i+=1
Counting horizontal,🌺🌺🌺🌺🌺
4:08 PM
Forwarded
i=1
while i<=10:
	if i%2==0:
		print("even",i)
	else:
		print("odd",i)
	i=i+1
Even and odd no💓💓💓💓



n=int(input("enter a value"))
n1=n
i=1
sum=0
while i<n1:
	sum=sum+(n1%10)
	n1=n1//10
if sum==n:
	print("hersad no")
else:
	print("not hersad")

	Hersad👍👍👍



a=5
c=6
a=c
print(c)
print(a)
Ak hi line ki updating value



s=0
n=int(input("enter the number"))
for i in range(1,n+1):
	s=s+(1/i)
print(s)
Series q 1/1+1/2+1/3+1/4+1/5......n



i=1
while i<=1000:
	j=1
	sum=0
	while j<i:
		if i%j==0:
			sum=sum+j
		j=j+1
	if sum==i:
		print(i)
	i=i+1



num=int(input("enter a number"))
i=1
sum=0
while i<=num:
	if num%i==0:
		sum=sum+i
	i=i+1
if num==sum:
	print("perfect no")
else:
	print("not perfect")
Perfect 🙏🏾🙏🏾🙏🏾🙏🏾



n=int(input("enter a no"))
i=1
sum=0
while i<=n:
	if n%i==0:
		sum+=1
	i+=1
if sum==2:
	print("prime")
else:
	print("not")



r=1
while r<=5:
	c=1
	while c<=r:
		print(c,end=" ")
		c=c+1
	r=r+1
	print(" ")


1
12
123
1234
12345



user=input("enter any string")
i=0
lowercase=0
uppercase=0
while i<len(user):
	if user[i]>="a" and user[i]<="z":
		lowercase+=1
	elif user[i]>="A" and user[i]<="Z":
		uppercase+=1
	i+=1
print("lowercase:",lowercase)
print("uppercase:",uppercase)



user=input("enter any string")
i=0
lowercase=0
uppercase=0
digit=0
while i<len(user):
	if user[i]>="a" and user[i]<="z":
		lowercase+=1
	elif user[i]>="A" and user[i]<="Z":
		uppercase+=1
	elif user[i]>="1" and user[i]<="9":
		digit+=1
	i+=1
print("lowercase:",lowercase)
print("uppercase:",uppercase)
print("digit:",digit)
4:17 PM
10/28/2021
KBC



a=0
b=1
sum=0
i=1
while i<=10:
	print(sum,end=" ")
	a=b
	b=sum
	sum=a+b
	i=i+1



Feboneci series
11:37 PM
i=int(input("enter your number"))
sum=0
x=i
while i>0:
	sum=sum+(i%10)(i%10)(i%10)
	i=i//10
if sum==x:
	print("number is armstrong")
else:
	print("number is not armstrong")


Armstrong number



# a="pinku gill"
# print(len(a))

# p=("50000")
# g=input("ek student number")
# r=input("ek student ka kharcha")
# if r<=p:
#     print("bjt k andr h")
# else:
#     print("bjt m nhi h")


# i =1
# while i<=1000:
# 	if i%3==0:
# 		print("nav")
# 	if i%7==0:
# 		print("gurukul")
# 	if i%21==0:
# 		print("navgururkul")
# 	else:
# 		("nathing")
# 	i=i+1

# : a=int(input("enter your number frist"))
# b=int(input("enter your number secend"))
# c=int(input("enter your number tisra"))
# if a>b and a>c:
# 	print("max number",a)
# elif b>a and b>c:
# 	print("max number=",b)
# else:
# 	print("max number=",c)

# num=int(input("enter your number"));
# rem=sum=0;
# n=num;
# while(num>0):
#     rem=num%10;
#     sum=sum+rem;
#     num=num//10;
#     if(n%sum==0):
#         print(str(n)+" true");
#     else:
#         print(str(n)+"false");

# i=2
# n=int(input("enter your number"))
# k=10
# while i<n:
# 	print(k,i,end=' ')
# 	i+=2
# 	k+=10

# n=int(input("enter your number "))
# count=0
# i=1
# while i<=n:
# 	if (n%i==0):
# 		count=count+1
# 	i=i+1
# if (count==2):
# 	print("prime number")
# else:
# 	print("composite number")

#  num=int(input("enter a number"))
# user=int(input('enter:'))
# n=1
# c=0
# while n<=num:
# 	sum=0
# 	i=1
# 	while i<=num:
# 		if n%i==0:
# 			sum+=1
# 		i+=1
# 	if sum==2:
# 		c+=1
# 		print(n)
# 	if c==user:
# 		break
# 	n+=1

# n=int(input("enter your number"))
# i=1
# while i<n:
# 	j=1
# 	c=0
# 	while j<=i:
# 		if i%j==0:
# 			c=c+1
# 		j=j+1
# 	if c==2:
# 		print(i)
# 	i=i+1

# n=int(input("enter a number"))
# i=1
# c=0
# while i<=n:
# 	if n%i==0:
# 		c=c+1
# 	i=i+1
# if c==2:
#     	print("it is prime number")
# else:
#     	print("it is not prime number")

# i=0
# while i<5:
# 	if i==3:
# 		break
# 	print(i)
# 	i+=1
# else:
# 	print("over")
# 4:53 PM
# i=0
# while i<3:
# 	j=1
# 	while j<i:
# 		print(j)
# 		j+=1
# 	i+=1

# num=int(input("enter a number"))
# i=1
# a=[]
# while i<=num:
# 	j=0
# 	b=[]
# 	while j<=10:
# 		x=i*j
# 		b.append(x)
# 		j=j+1
# 	a.append(i)
# 	a.append(b)
# 	i=i+1
# print(a)












