def r1(x):
    for i in range(x):
        print('*', end='')
def r2(y):
    for i in range(y):
        print(' ', end='')

def pattern(n):
  r1(n)
  print("\r")

  k = n // 2
  l = 1

  while k != 0:
     r1(k)
     r2(l)
     r1(k)
     print('\r')

     k -= 1
     l += 2

  u = 1
  v = n-4

  while u != n//2:
     r1(u+1)
     r2(v)
     r1(u+1)
     print('\r')

     u += 1
     v -= 2

  r1(n)

t=int(input())
a=[]
for i in range(t):
    size=int(input())
    a.append(size)

for i in range(t):
    pattern(a[i])
    print(end='\n')
