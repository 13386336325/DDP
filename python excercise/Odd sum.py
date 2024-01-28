m,n = input().split()
p = eval(m)
q = eval(n)
n = 0
x = 0
for i in range(1,p+1):
    if i%2!=0:
        n = n+i
        x = x+1
        if n >= q:
            print(n)
            print(x)
            print(i)
            break
        elif i == p or i == p+1:
            print(n)
            print(x)
            print(i)
        
        
