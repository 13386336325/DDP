t=open('jisuan.txt','r')
p=open('jieguo.txt','w')
txt=t.readlines()
for i in txt:
    
    if "+" in i:
        s=i.find("+")
        a=eval(i[0:s])+eval(i[s+1:])
        a1=str("{:.2f}".format(a))
        p.write(a1)
        p.write('\n')
    if "-" in i:
        s=i.find("-")
        b=eval(i[0:s])-eval(i[s+1:])
        b1=str("{:.2f}".format(b))
        
    
        p.write(b1)
        p.write('\n')
        
        
t.close()
p.close()
