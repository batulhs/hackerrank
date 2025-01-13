n=int(input())
for i in range(n):
    s=input()
    l=[]
    b=True
    for char in s:
        if char in ["(","[","{"]:
            l.append(char)
        elif char==")" and l and l[-1]=="(":
            l.pop()
        elif char=="]" and l and l[-1]=="[":
            l.pop()
        elif char=="}" and l and l[-1]=="{":
            l.pop()
        else:
            b=False
            break
    if len(l)==0 and b:
        print("YES")
    else:
        print("NO")
