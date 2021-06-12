n, r, x, y = map(int,input().split())
c = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]

rf=r

for i in range(n):
    if c[i]==1:
       if s[i]==1:
           rf+=x
       else:
           rf-=y

if rf>r:
    print("promoted")
elif rf==r:
    print("no change")
else:
    print("demoted")