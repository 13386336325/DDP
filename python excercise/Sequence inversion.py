line= input()
ss=line.split()
sl=ss.pop(0)
num=int(sl)
ss.reverse()
for s in ss:
    print(s,end=" ")

