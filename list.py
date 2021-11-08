list=[[1,2,3],[4,5,6],[7,8,9]]
i=0
sum=0
while i<len(list):
	j=0
	while j<len(list[i]):
		sum=sum+list[i][j]
		j+=1
	i+=1
print(sum)
Multiple list sum💝💝💝💝



list=[[1,2,3],[4,5,6],[7,8,9]]
i=0
while i<len(list):
	j=0
	sum=0
	while j<len(list[i]):
		sum=sum+list[j][i]
		j=j+1
	i=i+1
print(sum)
List ke sare last no ka add💕💕💕💕


def a():
	i=0
	sum=0
	while i<len(list):
		sum=sum+list[i]
		i=i+1
	print(sum)
list=[3,4,5,6,7]
a()


# list1 = [1, 10, 75, 23, 8,98]
# list2 = [75, 23, 98, 12,8, 78, 10, 1]
# new=[]
# i=0
# while i<(len(list1)):
#     if list1[i] not in new:
#         new.append(list1[i])
#     i=i+1
# print(new)


# p=[1,2,3,4,5,6,7,8,9]
# i=0
# sum=0
# while i<(len(p)):
#     if p[i]%2==0:
#         a=p[i]
#         sum=sum+a
#     i=i+1
# print(sum) even addition


# num=int(input("Enter a number:"))
# last_digit=num% 10
# if(last_digit% 3==0):
#     print("{} is divisible by 3 ".format(last_digit))
# else:
#     print("{} is not divisible by 3".format(last_digit))"""  """

# num=int(input("Enter a number:"))
# last_digit=num% 10
# if(last_digit% 3==0):
#     print("{} is divisible by 3 ".format(last_digit))
# else:
# #     print("{} is not divisible by 3".format(last_digit))"""  """
# alg alg element

# num=[8,2,3,0,7]
# def my_number(numbers):
# 	print(sum(numbers))
# my_number(num)
# list max no.


a=[20,18,17,5,7,8,9,99,66,6]
i=0
b=[]
c=[]
while i<len(a):
	if a[i]%2==0:
		b.append(a[i])
	else:
		c.append(a[i])
	i=i+1
print("even",b,'sum of even numbers is:',sum(b))
print("odd",c,'sum of odd numbers is ',sum(c))
Even,odd no print💝💝💝💝



n=[10,10,10,10,20,20,20,20,40,40,50,50,70]
i=0
b=[]
while i<len(n):
    if n[i]not in b:
        b.append(n[i])
        j=0
        c=0
        while j<len(n):
            if n[i]==n[j]:
                c=c+1
            j=j+1
        print(n[i],":",c)
    i=i+1
List me count kerna😘😘😘😘



num=[2,5,6,10,1]
i=0
min=num[i]
while i<len(num):
    if num[i]<min:
        min=num[i]
    i=i+1
print(min)
Minimum no 💓💓💓💓



def even(a,b):
	i=0
	while i<len(a) and len(b):
		if a[i]%2==0 and b[i]%2==0:
			print("dono even h")
		else:
			print("dono even nahi h")
		i=i+1
    
    
    
a=[2,6,18,10,3,75]
b=[6,19,24,12,3,87]
even(a,b)



a=[64,1,2,3,5,4,122,44]
i=0
b=[]
while i<len(a):
	j=0
	while j<len(a):
		if a[i]<a[j]:
			a[i],a[j]=a[j],a[i]
		j=j+1
	i=i+1
print(a)
Assecending order🌺🌺🌺🌺



a=[64,1,2,3,5,4,122,44]
i=0
b=[]
while i<len(a):
	j=0
	while j<len(a):
		if a[i]>a[j]:
			a[i],a[j]=a[j],a[i]
		j=j+1
	i=i+1
print(a)
Descending order🌺🌺🌺🌺🌺



list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
b=[]
i=0
while i<len(list1):
	if list1[i] not in list2:
		b.append (list1[i])
	i=i+1
print(b)
Duplicate remove 😂😂



list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
b=[]
i=0
while i<len(list1):
	if list1[i] in list2:
		b.append (list1[i])
	i=i+1
print(b)



list=['abc','xyz','aba','1221']
i=0
c=0
while i<len(list):
	if list[i][0]==list[i]:
		c=c+1
	print(i)
	i=i+1
Counting len 🥰🥰🥰🥰



list=['abc','xyz','aba','1221']
i=0
c=0
while i<len(list):
	if list[i][0]==list[i][-1]:
		c=c+1
	i=i+1
print(c)
	pinku 🤪🤪🤪🤪🤪



list=["abc","xyz","aba","1221"]
i=0
count=0
while i<len(list):
    j=0
    count1=0
    while j<len(list[i]):
        k=-1
        while k>=(-len(list[i])):
            if list[i][j]==list[i][k]:
                count1=count1+1
            if count1==2:
                count=count1
            k-=1
        j+=1
    i+=1
print(count)
pinku 🤪🤪🤪🤪🤪🤪



list=[[1,2,3],[4,5,6]]
print(list[0][0],list[1][0])
print(list[0][1],list[1][1])
print(list[0][2],list[1][2])
Indexing use💕💕💕💕



a=[1,2,[3,4],[5,6],[7],[8,9]]
i=0
b=[]
while i<len(a):
	if type(a[i])==list:
		b.extend(a[i])
	i=i+1
b.insert(0,1)
b.insert(1,2)
print(b)
List=[1,2,[3,4],[5,6],[7],[8,9]😍😍😍



a=[1,2,3,[4,5],6,7]
i=0
while i<len(a):
	if type(a[i])!=list:
		print(a[i],end=" ")
	else:
		b=0
		while b<len(a[i]):
			if type(a[i])==list:
				print(a[i][b],end=" ")
			b=b+1
	i=i+1
List=[1,2,3[4,5],6,7,8]



a="i am pinku"
b=" "
c=[]
i=0
while i<len(a):
	if b==" ":
		c.append(a[i])
		print(a[i])
	i=i+1
print(i)
	Char count with space
😘😘😘😘😘



a="i am gill saab"
b=" "
i=0
while i<len(a):
	if b==" ":
		print(a[i])
	i=i+1
	Without split function use



num=[2,5,6,10,1]
i=0
min=num[i]
while i<len(num):
	if num[i]<min:
		min=num[i]
	i=i+1
print(min)


j=0
smin=0
smin=num[i]
while j<len(num):
	if num[i]<smin:
		smin=num[i]
	i=i+1
print(smax)
Minimum😍😍😍😍


a="i am mohit"
b=" "
c=[]
i=0
while i<len(a):
	if b==" ":
		c.append(a[i])
		print(a[i])
	i=i+1
	
	Name aleg aleg split me use without split🍬🍬🍬🍬🍬
  
  
  
list=[[1,2,3],[4,5,6],[7,8,9]]
i=0
sum=0
while i<len(list):
	j=0
	while j<len(list[i]):
		sum=sum+list[i][j]
		j+=1
	i+=1
print(sum)
Multiple list sum💝💝💝💝



list=["abc","xyz","aba","1221"]
i=0
count=0
while i<len(list):
    j=0
    count1=0
    while j<len(list[i]):
        k=-1
        while k>=(-len(list[i])):
            if list[i][j]==list[i][k]:
                count1=count1+1
            if count1==2:
                count=count1
            k-=1
        j+=1
    i+=1
print(count)
Shalini 🤪🤪🤪🤪🤪🤪



a=[4,5,6,7,8]
i=0
b=[]
while i<len(a):
	if a[i]==5:
		b.append(a[i])
	i=i+1
print(b



list=[[1,2,3],[4,5,6],[7,8,9]]
print(list[0][0],list[1][0],list[2][0])
4:15 PM
list=[1,2,3,[4,5,6],7,[8,9]]
i=0
sum=0
while i<len(list):
	if type(list[i])!=list:
		sum=sum+(list[i])
	else:
		   j=0
		   while j<len(list[i]):
		   	 sum=sum+(list[i][j])
		   	 j=j+1
   i=i+1
print(sum)



n=[10,10,10,10,20,20,20,20,40,40,50,50,70]
i=0
b=[]
while i<len(n):
    if n[i]not in b:
        b.append(n[i])
        j=0
        c=0
        while j<len(n):
            if n[i]==n[j]:
                c=c+1
            j=j+1
        print(n[i],":",c)
    i=i+1



a=[20,18,17,5,7,8,9,99,66,6]
i=0
b=[]
c=[]
while i<len(a):
	if a[i]%2==0:
		b.append(a[i])
	else:
		c.append(a[i])
	i=i+1
print("even",b,'sum of even numbers is:',sum(b))
print("odd",c,'sum of odd numbers is ',sum(c))



n=[50,40,23,70,56,12,5,10,7]
i=0
max=0
smax=0
tmax=0
while i<len(n):
	if n[i]>max:
		max=n[i]
	j=0
	while j<len(n):
		if max>n[j] and smax<n[j]:
			smax=n[j]
		elif smax>n[j] and tmax<n[j]:
			tmax=n[j]
		j+=1
	i=i+1
print(tmax)



num=[2,5,6,10,1]
i=0
min=num[i]
while i<len(num):
    if num[i]<min:
        min=num[i]
    i=i+1
print(min)



num=[2,5,6,10,1]
i=0
min=num[i]
while i<len(num):
    if num[i]<min:
        min=num[i]
    i=i+1
print(min)



user=int(input ('enter the no'))
list=['p','q']
k=0
while k<len(list):
	i=1
	l=[]
	while i<=user:
		j=1
		c=[]
		if i==1 and j==1:
			l.append(c)
		else:
				while j<=i:
					c.append(j)
					j=j+1
					l.append(c)
		i=i+1
k=k+1
print(l)



n=[50,40,23,70,56,12,5,10,7]
i=0
max=0
smax=0
tmax=0
while i<len(n):
	if n[i]>max:
		max=n[i]
	j=0
	while j<len(n):
		if max>n[j] and smax<n[j]:
			smax=n[j]
		elif smax>n[j] and tmax<n[j]:
			tmax=n[j]
		j+=1
	i=i+1
print(tmax)



a=[1,1,0,1,1,0,0,0]
sum=0
i=-1
b=0
while i>=(-len(a)):
	sum=sum+a[i]2*b
	b=b+1
	i=i-1
print(sum)
Binary to decimal



list=["abc","xyz","aba","1221"]
i=0
count=0
while i<len(list):
    j=0
    count1=0
    while j<len(list[i]):
        k=-1
        while k>=(-len(list[i])):
            if list[i][j]==list[i][k]:
                count1=count1+1
            if count1==2:
                count=count1
            k-=1
        j+=1
    i+=1
print(count)



a=[19,20,1,5,7,15]
i=0
even=[]
odd=[]
while i<len(a):
	if a[i]%2==0:
		even.append(a[i])
	else:
		odd.append(a[i])
	i=i+1
print(even)
print(odd)	
eve_prime=[]
odd_prime=[]
if 2 in even:
	eve_prime.append(2)
else:
	j=0
	while j<len(odd):
		k=1
		c=0
		while k<=(odd[j]):
					if odd[j]%k==0:
						c=c+1
					k=k+1
		if c==2:
			odd_prime.append(odd[j])
		j+=1
	print(odd_prime)
	print(eve_prime)
			


Even odd ki prime number😇😇😇😇😇😇😇
4:15 PM
a=[2,3,4,5,6,7,8]
b=[8,9,4,3,6,7,8]
i=0
c=[ ]
while i<len(a):
	c.append(a[i]+b[i])
	i=i+1
print(c)



l=[99,88,64,73,92,97]
i=0
c=[ ]
while i<len(l):
	j=0
	s=" "
	a=str(l[i])
	while j<len(a):
		if (a[j])=='0':
			s=s+'zero'
		elif (a[j])=='1':
			s=s+'one'
		elif (a[j])=='2':
			s=s+'two'
		elif (a[j])=='3':
			s=s+'three'
		elif (a[j])=='4':
			s=s+'four'
		elif (a[j])=='5':
			s=s+'five'
		elif (a[j])=='6':
			s=s+'six'
		elif (a[j])=='7':
			s=s+'seven'
		elif (a[j])=='8':
			s=s+'eight'
		elif (a[j])=='9':
			s=s+'nine'
		j=j+1
	i=i+1
	c.append(s)
print(c)



str="mississippi"
c=0
b={}
for i in str:
	if i in b:
		b[i]+=1
	else:
		b[i]=1
print(b)



i=1
a=[]
while i<=100:
	j=2
	sum=0
	while j<=i//2:
		if i%j==0:
			sum=sum+1
			break 
		j+=1
	if sum==0 and i!=1:
		a.append(i)
	i+=1
print(a)
	
prime no in list 1 to 100



list=[1,2,3,4,5,6,7,8]
i=0
while i<len(list):
	j=0
	b=[]
	while j<2:
		b.append(list[j])
		j=j+1
	print(b)
	i=+1


n=int(input("write a num:   "))
n=n//10
m2=n%10
if m2==7:
	print("yes")
else:
	print("no")
4:15 PM
WEDNESDAY
a = "Hello, World!"
b = a.split(",")
print(b)
Split
      

p=[12,12,12,12,12,12,12,12,12,12]
i=0
sum=0
while i<(len(p)):
    a=p[i]
    sum=sum+a
    i=i+1
print(sum)   
      list sum

