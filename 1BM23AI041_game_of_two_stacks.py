g=int(input())
for i in range(g):
    t=input()
    t=t.split()
    aa=input()
    aa=aa.split()
    bb=input()
    bb=bb.split()
    n=int(t[0])
    m=int(t[1])
    maxSum=int(t[2])
    a=[]
    b=[]
    for j in range(n):
        a.append(int(aa[j]))
    for k in range(m):
        b.append(int(bb[k]))
    count=0
    maxcount=0
    sum=0
    x=0
    for p in range(n):
        if sum+a[p]>maxSum:
            break
        sum=sum+a[p]
        count+=1
        x+=1
    maxcount=count
    for q in range(m):
        sum=sum+b[q]
        count+=1
        while sum>maxSum and x>0:
            x-=1
            sum=sum-a[x]
            count-=1
        if sum<=maxSum:
            maxcount=max(maxcount,count)
    print(maxcount)
