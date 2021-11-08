i=0
sum=0
mult=0
while i<(len(p)):
    a=p[i]
    if a%3==0:
        mult=mult*a
    else:
        sum=sum+a
        i=-i+1
    print("sum of number",sum)
    print("multiplication of number",mult)
