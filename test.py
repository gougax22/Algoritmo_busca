from random import randint
v=[]
for i in range(0,5):
        sort=randint(0,10)
        v.append(sort)

def ordem(v,num):
    i=0
    pos=1
    n=len(v)
    while(i<=n-1) :
        if (v[i] == num):
            pos = i
        i+=1
        if 6 not in v:
             return 0
    return pos




print(v)
print(ordem(v,6))