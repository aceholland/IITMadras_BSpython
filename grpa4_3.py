'''
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
'''

n=int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        if (j!=i):
            print(j, end=",")
        else:
         print (j)

for k in range(n-1, 0, -1):
   for l in range(1, k+1):
      if (l!=k):
         print(l, end=",")
      else :
         print(l)
