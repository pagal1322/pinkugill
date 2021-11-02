# dic1={1:10,2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic={}
# for i in dic1:
# 	for j in dic2:
# 		for k in dic3:
# 			if i==j:
# 				dic[i]=dic1[i]+dic2[j]
# 			else:
# 				dic[i]=dic1[i]
# 				dic[j]=dic2[j]
# 				dic[k]=dic3[k]
# print(dic)


# a=[[1,2,3,4,5],[5,6,7,8],[6,7,8,9]]
# b=[0,1,2]
# new={}
# for key in b:
# 	for value in a:
# 		new[key]=value
# 		break
# # print(str(new))

# m=[[1,2,3,4,5],[5,6,7,8],[6,7,8,9]]
# new=[]
# new2=[0,1,2]
# new3={}
# i=0
# while i<len(m):
# 	j=0
# 	sum=0
# 	while j<len(m[i]):
# 		sum=sum+m[i][j]
# 		j+=1
# 	new.append(sum)	
# 	i+=1
# for key in new2:
# 	for value in new:
# 		new3[key]=new[key]
# print(new3)



