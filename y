
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# dict={"name":"Raju","marks":56}
# x=input("enter any thing:")
# if x in dict:
# 	print("exist")
# else:
# 	print("not exist")


# my_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        } 
# sum=0
# for x in my_dict:
# 	sum=sum+my_dict[x]
# print(sum)


# dic= {
#         1: 'NAVGURUKUL',
#         2: 'IN',  
#         3:{    
#              'A' : 'WELCOME',
#              'B' : 'To',
#              'C' : 'DHARAMSALA'
#             }
#         }
# del dic[3] ["A"]
# print(dic)


# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# x={}
# for key in list1:
# 	for value in list2:
# 		x[key]=value
# 		break
# print(str(x))



# from collections import Counter
# def unique(list1):
#     print(*Counter(list1)) 
# list1 = {"1","2","1","5","5","9","7"}
# print("the unique values from 1st list is")
# unique(list1)


# count = {"M":0,"I":0,"S":0,"P":0}
# word = "MISSISSIPPI"
# for i in word:
# 	if i == "M":
# 		count['M'] = count['M']+1
# 	elif i == "I":
# 		count['I'] = count['I']+1
# 	elif i == "S":
# 		count['S'] = count['S']+1
# 	elif i == "P":
# 		count['P'] = count['P']+1
# print(count)



# list2=[1,2,3,4,5,]
# x={}
# for key in list1:
# 	for value in list2:
# 		x[key]=value
# 		list2.remove(value)
# 		break
# print(str(x))


# dict={"alex":["subji","subji2","subji3"],"david":["subji1","subji2"]}
# total=0
# for value in dict:
# 	value_list=dict[value]
# 	count=len(value_list)
# 	total+=count
# print(total)




# my_dict={1:1,2:4,3:9,4:16,5:25}
# my_dict.popitem( )
# my_dict.popitem( )
# print(my_dict)


#  my_dict={1:1,2:4,3:9,4:16,5:25}
# del my_dict[4]
# print(my_dict)




# my_dict={1:1,2:4,3:9,4:16,5:25}
# my_dict.clear()
# print(my_dict



#  my_dict={1:1,2:4,3:9,4:16,5:25}
# print(my_dict[4])



# dict={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# print(dict["x"][4])
# print(dict["y"][4])
# print(dict["z"][4])


# n=int(input("Input a number "))
# d = dict()
# for x in range(1,n+1):
#     d[x]=x*x
# print(d)


# dict1={1:2,2:3,3:4,4:5}
# print("The original dictionary is : " + str(dict1)) 
# res = sum(list(dict1.keys())) 
# print("The dictionary keys summation : " + str(res))




# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = {}
# for i,j in d1.items():
#     for x, y in d2.items():
#         if i == x:
#             d3[i]=(j+y)
# print(d3)



# str1= 'w3resource' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

# Create a dictionary from a string
(

# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_d = sorted(d.items(), key=operator.itemgetter(1))
# print(ascending: ',sorted_d)
# sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# print(descending:',sorted_d)


# key=int(input("enter a key:"))
# value=int(input("enter a value:"))
# d={}
# d.update({key:value})
# print("updated dictionary is:")
# print(d)


# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# dic4={}
# for d in (dic1,dic2,dic3):
# dic4.update(d)
# print (dic4)


# d={1:10,2:20,3:30,4:40,5:50,6:60}
# def is_key_present(x):
#     if x in d:
#         print("key is present in dict")
#     else:
#         print("key is not present in dict")
# is_key_present(5)
# is_key_present(9)



# dic1={"a":100,"b":200}
# dic2={"x":300,"y":200}
# d=dic1.copy()
# d.update(d2)
# print(d)


# dict={"a":"juice","b":"grill","c":"corn"}
# for key,value in dict.iteritem():
#     print(key,value)


# my_dict={"data1":100,"data2":-54,"data3":247}
# print(sum(my_dict.value()))


# dict={"x":20,"y":5,"z":60}
# total=1
# for key in dict:
#     total=total*dict[key]
# print(total)


dict={"a":1,"b":2,"c":3,"d":4}
dict={"x":20,"y":5,"z":60}
# total=1
# for key in dict:
#     total=total*dict[key]
# print(total)
# 
# dict={"x":20,"y":5,"z":60}
# total=1
# for key in dict:
#     total=total*dict[key]
# print(total)
# 
# 
# dict={"x":20,"y":5,"z":60}
# total=1
# for key in dict:
#     total=total*dict[key]
# print(total)


# dict={"a":1,"b":2,"c":3,"d":4}
# del.dict["a"]
# print(dict)
