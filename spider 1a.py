l=int(input())
s=input()

sb=int(s,2)



s1=bin(sb-1).replace("0b","")
s2=bin(sb+1).replace("0b","")


if len(s1)==len(s2)==l:
    print(s1," ",s2)
else:
    print(-1)




