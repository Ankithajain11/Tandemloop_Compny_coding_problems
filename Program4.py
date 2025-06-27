l=[1,2,8,9,12,46,76,82,15,20,30]
res={}
for i in l:
    for j in range(1,10):
        if i%j==0:
            if j not in res:
                res[j]=1
            else:
                res[j]+=1
print(res)
