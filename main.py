n=20
l=[]
sum=0
for i in range(2,n+1):
    if n%i==0:
        l.append(i)
for j in l:
    if j>1:
        for k in range(2, j):
            if j % k == 0:
                break
        else:
            sum += j
print(sum)

