n,a=input().split(" ",1)
for p in a:
    if ord("a")<=ord(p)<=ord("z"):
        print(chr(ord("a")+(ord(p)-ord("a")+int(n))%26),end='')
    elif ord("A")<=ord(p)<=ord("Z"):
        print(chr(ord("A")+(ord(p)-ord("A")+int(n))%26),end='')
    else:
        print(p,end='')
        
